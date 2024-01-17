import random
from base_car import BaseCar
from basisklassen import *

class SonicCar(BaseCar):
    def __init__(self):
        super().__init__()
        self._ultrasonic = Ultrasonic()    
    
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
                             max_distance: int=80,
                             loops: int=100, 
                             random_direction: bool=True,
                             high_speed: bool=True
                             ):
        
        self.speed = init_speed
        self.drive_forward(init_speed)
        for i in range(loops):
            distance = self.distance()                  
            self.__check_low_distance(init_speed, min_distance, distance)
            self.__check_normal_distance(init_speed, min_distance, max_distance, random_direction, distance)
            self.__check_far_distance(high_speed, max_distance, distance)
        
        self.drive_stop()
            
    def run_until_obstacle_detected(self, speed: int=40, min_distance: int=20, print_distance: bool=True):
        
        self.steering_angle = 110
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
            self.drive_forward(speed=init_speed)                     
            time.sleep(random.random() + 1)              
            self.steering_angle = 90                 
            self.drive_stop(self.speed)

    def __check_normal_distance(self, init_speed: int, min_distance: int, max_distance: int, random_direction: bool, distance: float):
        
        if (min_distance < distance <= max_distance) and random_direction:  
            self.speed = init_speed
            self.steering_angle = self.steering_angle + random.randint(-10, 10)

    def __check_far_distance(self, high_speed: bool, max_distance: int, distance: float):
        
        if (distance > max_distance or distance == -1) and high_speed:  
            self.steering_angle = 90  
            self.speed = min(self.speed + 5, 50)

        self.drive_stop()