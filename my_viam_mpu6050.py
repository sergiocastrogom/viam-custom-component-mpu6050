# See:
# https://python.viam.dev/examples/example.html#create-custom-components
# https://github.com/viamrobotics/viam-python-sdk
# using the MPU module in https://github.com/m-rtijn/mpu6050

from mpu6050 import mpu6050
import time
import asyncio
from typing import Any, Mapping
from viam.components.sensor import Sensor

class myviammpu6050(Sensor):
    def __init__(self, name: str):
        self.sensorMPU = mpu6050(0x68)
        self.accel_readings = self.sensorMPU.get_accel_data()
        self.gyro_readings = self.sensorMPU.get_gyro_data()
        self.temp_readings = self.sensorMPU.get_temp()
        super().__init__(name)

    async def get_readings(self, **kwargs) -> Mapping[str, Any]:
        self.accel_readings = self.sensorMPU.get_accel_data()
        self.gyro_readings = self.sensorMPU.get_gyro_data()
        self.temp_readings = self.sensorMPU.get_temp()
        return {'Accelerometer x': str(self.accel_readings['x']), 'Accelerometer y': str(self.accel_readings['y']), 'Accelerometer z': str(self.accel_readings['z']), 'Gyroscope x': str(self.gyro_readings['x']), 'Gyroscope y': str(self.gyro_readings['y']), 'Gyroscope z': str(self.gyro_readings['z']), 'Temperature': str(self.temp_readings)}
