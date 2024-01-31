from car_base import BaseCar
from utilities.data_service import DataService
from basisklassen import *

import time
import random
from datetime import datetime

class SonicCar(BaseCar):
    
    _data_service = DataService()
    
    def __init__(self):
        super().__init__()
                
        self._ultrasonic = Ultrasonic()                
        self._distance = self.distance()
            
    def distance(self, n: int=3, skip_errors: bool=False): 
               
        result = 0
        number_valid_measurements = 0
        
        for _ in range(n):
            d = self._ultrasonic.distance()
            if d < 0:
                if skip_errors:
                    continue
            else:
                result += d 
                number_valid_measurements += 1
        if number_valid_measurements > 0:
            return result / number_valid_measurements
        else:
            return -1
          

    def _check_low_distance(self, init_speed: int, min_distance: int, distance: float):
    
        if 0 < self._distance < min_distance:
            self.drive_stop()                            
            self.steering_angle = 45           
            self.drive_backward(init_speed)                     
            time.sleep(random.uniform(0.5, 2))              
            self.steering_angle = 135
            
    def _check_normal_distance(self, init_speed: int, min_distance: int, max_distance: int, random_direction: bool, distance: float):
        
        if (min_distance < distance <= max_distance) and random_direction:  
            self.set_speed(init_speed)
            self.drive_forward(self.get_speed())
            self.steering_angle = self.steering_angle + random.randint(-10, 10)
            
    def _check_far_distance(self, high_speed: bool, max_distance: int, distance: float):
        
        if (distance > max_distance or distance == -1) and high_speed:  
            self.steering_angle = 90  
            self.set_speed(min(self.get_speed() + 5, 50))
            self.drive_forward(self.get_speed()) 
              