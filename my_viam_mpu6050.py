# See:
# https://python.viam.dev/examples/example.html#create-custom-components
# https://github.com/viamrobotics/viam-python-sdk
# using the MPU module in https://github.com/m-rtijn/mpu6050

from mpu6050 import mpu6050
import time 
import asyncio
from typing import Any
from viam.components.sensor import Sensor

class myviammpu6050(Sensor):
    def __init__(self, name: str):
        self.sensor = mpu6050(0x68) 
        self.num_readings = sensor.get_accel_data()
        super().__init__(name)

    async def get_readings(self, **kwargs) -> Mapping[str, Any]:
        return {"MPU6050 Accel Readings"[idx]: sensor.get_accel_data() for idx in range(self.num_readings)}
