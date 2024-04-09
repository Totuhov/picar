import datetime
import json
import threading
import time
import random

from car_sonic import SonicCar
from basisklassen import Infrared

class SensorCar(SonicCar):

    sensor = Infrared()
    

    def __init__(self):
        super().__init__()
        
        with open("./settings/config.json", "r") as f:
            self.settings = json.load(f)         
              
        self._sensor_values = self.sensor.read_analog()
        self._avg_ligth = float
        
        self._forward_sleep_index = self.settings['forward_sleep_index']
        self._backward_sleep_index = self.settings['backward_sleep_index']
        self._distance_from_start_avoid = self.settings['distanse_detection']
        
        # self.start_event = threading.Event()
        # self.stop_event = threading.Event()
        
    @property 
    def sensor_values(self) -> list:
        return self._sensor_values
    
    @sensor_values.setter
    def sensor_values(self, value) -> None:
        self._sensor_values = value
        
    @property 
    def avg_ligth(self) -> float:
        return self._avg_ligth
    
    @sensor_values.setter
    def avg_ligth(self, value) -> None:
        self._avg_ligth = value    
     
    @property 
    def forward_sleep_index(self) -> int:
        return self._forward_sleep_index
    
    @property 
    def backward_sleep_index(self) -> int:
        return self._backward_sleep_index
    
    @property 
    def distance_from_start_avoid(self) -> int:
        return self._distance_from_start_avoid
    
    @sensor_values.setter
    def sensor_values(self, value) -> None:
        self._sensor_values = value                  
        
    def obsticle_detected_mode(self):
        
        self._distance = self.distance()   
        self.drive_forward(20)    
        
        while self._distance < self.distance_from_start_avoid:
            if self.emergency_stop == True: 
                return
            
            while self.steering_angle < 135:
                self.steering_angle += 5
                time.sleep(0.1)
                    
            self._distance = self.distance()
                
        while self.steering_angle > 45:
            if self.emergency_stop == True: 
                return
            self.steering_angle -= 5
            time.sleep(0.1)                         
            
        self.sensor_values = self.sensor.read_analog() 
        
        while min(self.sensor_values) > 5: 
            if self.emergency_stop == True: 
                return  
            time.sleep(0.2)
            random_steering = random.choice([True, False])
            if random_steering:
                 self.steering_angle += 1
            else:   
                self.steering_angle -= 1                             
            self.sensor_values = self.sensor.read_analog()
         
        print(f'Min. sensor value: {min(self.sensor_values)} ---- time: {datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]}')
        return   
            
    def turn(self, argument):
        if argument == 0:
            self.steering_angle = 45
        elif argument == 1:
            self.steering_angle = 67
        elif argument == 2:
            self.steering_angle = 90
        elif argument == 3:
            self.steering_angle = 112
        elif argument == 4:
            self.steering_angle = 135            
 
        