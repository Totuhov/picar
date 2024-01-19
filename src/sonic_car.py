import random
from base_car import BaseCar
from data_service import DataService
from basisklassen import *
import time
from datetime import datetime

class SonicCar(BaseCar):
    def __init__(self):
        super().__init__()
        
        self._ultrasonic = Ultrasonic()  
        self.data_service = DataService("drive_data.json")
        self.data_service.write_data(self.create_data()) 
    
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
        
    def run_exploration_tour(self, 
                             init_speed: int=30, 
                             min_distance: int=30, 
                             max_distance: int=100,
                             loops: int=100, 
                             random_direction: bool=True,
                             high_speed: bool=True
                             ):
        
        self.steering_angle = 90
        self.set_speed(init_speed)
        self.drive_forward(self.get_speed())      
        
        for i in range(loops):
            
            distance = self.distance()
               
            print(f"Obsticle detected at {distance} cm.")               
            self.__check_low_distance(init_speed, min_distance, distance)                            
            
            self.__check_normal_distance(init_speed, min_distance, max_distance, random_direction, distance)
            
            self.__check_far_distance(high_speed, max_distance, distance)                                
        
        print(i, 'Loops beendet.')
        self.data_service._save_to_file()
        self.drive_stop()
            
    def run_until_obstacle_detected(self, speed: int=40, min_distance: int=20, print_distance: bool=True):
        
        self.steering_angle = 90
        self.drive_forward(speed)
        distance = self.distance()
        
        while distance >= min_distance or distance == -1:
            if print_distance:
                print(distance)
            distance = self.distance()            
            
        self.drive_stop()

    def __check_low_distance(self, init_speed: int, min_distance: int, distance: float):
    
        if 0 < distance < min_distance:
            self.drive_stop()                            
            self.steering_angle = 45  
            self.data_service.write_data(self.create_data())              
            self.drive_backward(init_speed)                     
            time.sleep(random.uniform(0.5, 2))              
            self.steering_angle = 90
            self.data_service.write_data(self.create_data())
            

    def __check_normal_distance(self, init_speed: int, min_distance: int, max_distance: int, random_direction: bool, distance: float):
        
        if (min_distance < distance <= max_distance) and random_direction:  
            self.set_speed(init_speed)
            self.drive_forward(self.get_speed())
            self.steering_angle = self.steering_angle + random.randint(-10, 10)
            self.data_service.write_data(self.create_data())
            if self.steering_angle < 45:
                self.steering_angle = 45
                self.data_service.write_data(self.create_data())
            elif self.steering_angle > 135:
                self.steerin_angle = 135
                self.data_service.write_data(self.create_data())

    def __check_far_distance(self, high_speed: bool, max_distance: int, distance: float):
        
        if (distance > max_distance or distance == -1) and high_speed:  
            self.steering_angle = 90  
            self.set_speed(min(self.get_speed() + 5, 50))
            self.drive_forward(self.get_speed())
            self.data_service.write_data(self.create_data())
            
    def create_data(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S.%f")[:-3]
        data_obj = {
            "speed": self.get_speed(),
            "obsticle_dist": self.distance(),
            "wheels_angle": self.steering_angle,
            "direction": self.get_direction(),
            "time": formatted_time
            }
        return data_obj