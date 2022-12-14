from ble_connect import BleConnection
from ble_gui import BleGui

from queue import Queue
import asyncio
import threading

class BleGuiCommunication():
    def __init__(self):
        self.q_send = Queue()
        self.q_receive = Queue()
        self.ble_connection = BleConnection(self.q_send,self.q_receive)
        self.gui = BleGui(self.q_send,self.q_receive)
        
    async def main(self):  
        await self.ble_connection.connect()
        while True:
            await self.gui_update()

        #loop = asyncio.get_event_loop()
        #self.gui.window.after(10, lambda: loop.run_until_complete(self.gui_update()))
        #self.gui.window.mainloop()

    async def gui_update(self):
        #if self.gui.new_msg_to_send_flag:
        if not self.q_send.empty():
            #self.gui.new_msg_to_send_flag = False
            await self.ble_connection.send_message()#self.gui.msg)
            #self.gui.msg = ""
        
        #if self.ble_connection.new_received_msg_flag:
        if not self.q_receive.empty():
            #self.ble_connection.new_received_msg_flag = False
            self.gui.show_received_msg()#self.ble_connection.received_msg)
            #ble_connection.received_msg = ""

        await asyncio.sleep(1)
        
if __name__ == "__main__":
    ble_gui_comm = BleGuiCommunication()
    asyncio.run(ble_gui_comm.main())