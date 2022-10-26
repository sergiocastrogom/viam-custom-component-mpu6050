# my-python-robot/python_server.py

import asyncio
from viam.rpc.server import Server

from my_viam_mpu6050 import myviammpu6050

async def main():
    srv = Server([myviammpu6050('my-MPU6050')])
    await srv.serve()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        pass
    
# To use this custom server as part of a larger robot, you’ll want to add it as a remote in the config for your main part.

# [
#  {
#    "address": "localhost:9090",
#    "name": "my-own-robot",
#    "insecure": true
#  }
# ]
