
import time
from base_car import BaseCar

class Fahrparkur():
        
    def __init__(self, car: BaseCar):     
        self.car = car
        
    def test_weels(self):
        
        car = self.car        
        car.steering_angle = 45
        time.sleep(.5)
        car.steering_angle = 90
        time.sleep(.5)
        car.steering_angle = 115
        time.sleep(.5)
        car.steering_angle= 125
        time.sleep(.5)
        car.steering_angle = 135
        time.sleep(.5)
        car.steering_angle = 90
        
    def fahrparkur_1(self) -> None: 
        time.sleep(1)
        car = self.car
        car.steering_angle = 90
        time.sleep(1)
        car.drive_forward(20)   
        time.sleep(3)
        car.drive_stop() 
        time.sleep(1) 
        car.drive_backward(20)   
        time.sleep(3)      
        car.drive_stop()       
    
    def fahrparkur_2(self) -> None: 
        time.sleep(1)
        car = self.car
        car.steering_angle = 90
        car.drive_forward(40)   
        time.sleep(1)
        car.steering_angle = 45 
        time.sleep(4)
        car.steering_angle = 45 
        time.sleep(4)       
        car.steering_angle = 90
        car.drive_stop()
           