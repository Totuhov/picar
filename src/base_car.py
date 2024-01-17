from basisklassen import *

class BaseCar():              
    
    def __init__(self):
        self.__steering_angle = 95 
        self.front_wheels = FrontWheels()
        self.back_wheels = BackWheels() 
    
    @property
    def steering_angle(self) -> int:        
        print(f"Steering angle: {self.__steering_angle}°")
        return self.__steering_angle
    
    @steering_angle.setter
    def steering_angle(self, value) -> None:
        self.__steering_angle = value
        self.front_wheels.turn(value)
        print(f"Sreering angle set to {value}°")
        
    def drive_forward(self, value: int = 0) -> None:
        '''
        Drive forwards
        Args:
        value (int): Speed
        '''
        if value <= 0:
            raise Exception("The value of speed schould be positiv number")
        else:            
            self.back_wheels.forward()
            self.back_wheels.speed = value
            print(f"Driving forwards with speed of {value}")
    
    def drive_backward(self, value: int = 0) -> None:
        '''
        Drive backwards
        Args:
        value (int): Speed
        '''
        if value <= 0:
            raise Exception("The value of speed schould be positiv number")
        else:            
            self.back_wheels.backward()
            self.back_wheels.speed = value
            print(f"Driving backwards with speed of {value}")
    
    
    def drive_stop(self) -> None:
        '''
        Stops motor        
        '''
        self.back_wheels.speed = 0
        print("Car stops")
    
    def get_speed(self) -> int:
        return self.back_wheels.speed
    
    def get_direction(self) -> int:
        return self.back_wheels.forward_A         
