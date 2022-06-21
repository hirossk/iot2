# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import os
import asyncio
import json
from azure.iot.device.aio import IoTHubDeviceClient

data = {
  "message" : "hello",
  "value" : 123.0
  }


async def main():
    print(json.dumps(data))
    # Fetch the connection string from an environment variable
    conn_str = os.getenv("IOTHUB")

    # Create instance of the device client using the connection string
    device_client = IoTHubDeviceClient.create_from_connection_string(conn_str, websockets=True)

    # Connect the device client.
    await device_client.connect()

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
