import asyncio
from bleak import BleakScanner,BleakClient

ADDRESS = "EF:F5:8F:CC:B2:8D"
UUID = '6e400001-b5a3-f393-e0a9-e50e24dcca9e'

scanner = BleakScanner()

async def run():
    #device = await scanner.find_device_by_address("EF:F5:8F:CC:B2:8D")

    async with BleakClient() as client:
        model_number = await client.read_gatt_char()
        print("Model Number: {0}".format("".join(map(chr, model_number))))

loop = asyncio.get_event_loop()
loop.run_until_complete(run())