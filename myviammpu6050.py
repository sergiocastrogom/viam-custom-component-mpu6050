# Based on https://github.com/viamrobotics/viam-python-sdk/blob/main/examples/server/v1/components.py
# using the module described in https://github.com/m-rtijn/mpu6050
from mpu6050 import mpu6050
import time 
import asyncio
from typing import Any, Dict, Optional
from viam.components.sensor import Sensor

class ExampleSensor(Sensor):
    def __init__(self, name: str):
        sensor = mpu6050(0x68) 
        x = 0
        y = 0
        z = 0
        self.num_readings = sensor.get_accel_data()
        super().__init__(name)

    async def get_readings(self, **kwargs) -> Mapping[str, Any]:
        return {"MPU6050 Readings"[idx]: sensor.get_accel_data() for idx in range(self.num_readings)}
