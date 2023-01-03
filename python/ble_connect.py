"""
UART Service
-------------
An example showing how to write a simple program using the Nordic Semiconductor
(nRF) UART service.
"""

import asyncio
from itertools import count, takewhile
from typing import Iterator
from queue import Queue
from kin_spp import *
import time

from bleak import BleakClient, BleakScanner
from bleak.backends.characteristic import BleakGATTCharacteristic
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

class BleConnection():
    _UART_SERVICE_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
    _UART_RX_CHAR_UUID = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E"
    _UART_TX_CHAR_UUID = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E"

    def __init__(self, q_send, q_receive, q_connection):
        self.device = None
        self.new_received_msg_flag = False
        self.q_send = q_send
        self.q_receive = q_receive
        self.q_connection = q_connection
        #threading.Thread.__init__(self)
        #self.start()
    
    async def connect(self):

        def match_nus_uuid(device: BLEDevice, adv: AdvertisementData):
            # This assumes that the device includes the UART service UUID in the
            # advertising data. This test may need to be adjusted depending on the
            # actual advertising data supplied by the device.
            if self._UART_SERVICE_UUID.lower() in adv.service_uuids:
                return True

            return False

        self.device = await BleakScanner.find_device_by_filter(match_nus_uuid)

        if self.device is None:
            print("No device found with UUID {}.\n Most likely because Nordic is not advertising.".format(self._UART_SERVICE_UUID))
        else:
            self.client = BleakClient(self.device, timeout=600, disconnected_callback=self._handle_disconnect)
            try:
                await self.client.connect()
                print("Connected.")
                while not self.q_connection.empty():
                    self.q_connection.get()
                self.q_connection.put(True)
            except:
                print("Could not connect.")
                while not self.q_connection.empty():
                    self.q_connection.get()
                self.q_connection.put(False)
                return

            await self.client.start_notify(self._UART_TX_CHAR_UUID, self._handle_receive)
            self.nus = self.client.services.get_service(self._UART_SERVICE_UUID)
            self.rx_char = self.nus.get_characteristic(self._UART_RX_CHAR_UUID)
    
    async def send_message(self):
        message = self.q_send.get()[0:4]

        if isinstance(message, str):
            message = bytes(message, 'utf-8')

        packet = SpacePacketProtocol()

        if message == b'ping':
            packet.setHeader(VersionNumber.DEFAULT, PacketType.TC, SecondaryHeaderFlag.F, ApplicationProcessIdentifier.GS | ApplicationProcessIdentifier.PING, SequenceFlag.US, 0)
        elif message == b'pong':
            packet.setHeader(VersionNumber.DEFAULT, PacketType.TC, SecondaryHeaderFlag.F, ApplicationProcessIdentifier.GS | ApplicationProcessIdentifier.PONG, SequenceFlag.US, 0)
        else:
            # TODO
            packet.setHeader(VersionNumber.DEFAULT, PacketType.TC, SecondaryHeaderFlag.F, ApplicationProcessIdentifier.GS | ApplicationProcessIdentifier.PONG, SequenceFlag.US, 0)

        packet.setData(message)
        data = packet.toBuffer()

        #if isinstance(message, str):
        #    message = bytes(message, 'utf-8')
        for s in self._sliced(data, self.rx_char.max_write_without_response_size):
            await self.client.write_gatt_char(self.rx_char, s)

        print("Message \'{}\' sent.".format(data))

    def _sliced(self, data: bytes, n: int) -> Iterator[bytes]:
        """
        Slices *data* into chunks of size *n*. The last slice may be smaller than
        *n*.
        """
        return takewhile(len, (data[i : i + n] for i in count(0, n)))

    def _handle_disconnect(self, _: BleakClient):
        print("Device was disconnected, goodbye.")
        while not self.q_connection.empty():
            self.q_connection.get()
        self.q_connection.put(False)
        # cancelling all tasks effectively ends the program
        for task in asyncio.all_tasks():
            task.cancel()
        
    def _handle_receive(self, _: BleakGATTCharacteristic, data: bytearray):
        print("received:", data)
        print("data only:", data[6:].decode("utf-8") )
        
        self.q_receive.put(data[6:].decode("utf-8") )
        #self.received_msg = data
        #self.new_received_msg_flag = True

    """ def run(self):
        self.loop = asyncio.new_event_loop()
        asyncio.run(self.connect())
        await ble_connection.send_message("ping1")
        await ble_connection.send_message("ping2")
        self.loop.run_forever()
        await ble_connection.send_message("ping1")
        await ble_connection.send_message("ping2")
        while True:
            pass """

#ble_connection = BleConnection()



async def main():
    q_send = Queue()
    q_receive = Queue()
    ble_connection = BleConnection(q_send,q_receive)
    await ble_connection.connect()
    q_send.put("ping")
    await ble_connection.send_message()
    q_send.put("pong")
    await ble_connection.send_message()
    q_send.put("ping")
    await ble_connection.send_message()
    q_send.put("pong")
    await ble_connection.send_message()
    q_send.put("ping")
    await ble_connection.send_message()
    q_send.put("pong")
    await ble_connection.send_message()
    q_send.put("ping")
    await ble_connection.send_message()
    q_send.put("pong")
    await ble_connection.send_message()
    #await ble_connection.send_message("ping3")
    #await ble_connection.send_message("ping4")
    #await asyncio.sleep(1)
    while True:
        await asyncio.sleep(0.1)

#if __name__ == "__main__":
    #asyncio.run(main())