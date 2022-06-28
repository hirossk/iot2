# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os
import asyncio
import json
#これ追加することでi2cから温度を取得できる
import smbus
from time import sleep
from azure.iot.device.aio import IoTHubDeviceClient

data = {
  "message" : "temperature",
  "value" : 0
  }

#i2cインタフェースの初期化
bus = smbus.SMBus(1)

async def main():
    # Fetch the connection string from an environment variable
    conn_str = os.getenv("IOTHUB")

    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str, websockets=True)

    # Connect the device client.
    await device_client.connect()

    #ここで繰り返し
    while True:
        #温度データの取り出し
        block = bus.read_i2c_block_data(0xXX, 0x00, 1)
        data['value'] = block[0]
        # Send a single message
        print("Sending message...")
        await device_client.send_message(json.dumps(data))
        print("Message successfully sent!")

    # Finally, shut down the client
    await device_client.shutdown()


if __name__ == "__main__":
    asyncio.run(main())

    # If using Python 3.6 use the following code instead of asyncio.run(main()):
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()
