# my-python-robot/python_server.py

import asyncio
from viam.rpc.server import Server

from my_viam_mpu6050 import myviammpu6050

async def main():
    srv = Server([myviammpu6050('my-MPU6050')])

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        pass
