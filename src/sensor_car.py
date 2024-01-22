import time

from sonic_car import SonicCar
from basisklassen import Infrared

class SensorCar(SonicCar):
    def __init__(self):
        super().__init__()
        
        self.sensor = Infrared(self)
        self.__sensor_values = list
        
    @property 
    def sensor_values(self) -> list:
        return self.__sensor_values
    
    @sensor_values.setter
    def sensor_values(self, value) -> None:
        self.__sensor_values = value
        
    def test_run(self):
        self.drive_forward(10)
        for i in range(2):
            print(self.sensor.read_analog())
            time.sleep(0.2)
            i += 1

car = SensorCar()
car.test_run()
        