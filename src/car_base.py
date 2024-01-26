from basisklassen import *

class BaseCar():              
    '''
    Fahrparcour 1: Forward and backward
    Fahrparcour 2: Driving in a circle with maximum steering angle   
    '''
    def __init__(self):             
        
        self._steering_angle = 90 
        self._speed = 0
        self._direction = "P" 
        self._emergency_stop = False
        
        with open("config.json", "r") as f:
            data = json.load(f)
            turning_offset = data["turning_offset"]
            forward_A = data["forward_A"]
            forward_B = data["forward_B"]            
        
        self._turning_offset = turning_offset
        self._forward_A = forward_A
        self._forward_B = forward_B
            
        self.front_wheels = FrontWheels(turning_offset=self._turning_offset)
        self.back_wheels = BackWheels(forward_A=self._forward_A, forward_B=self._forward_B) 
        self.front_wheels.turn(90)
    
    @property
    def steering_angle(self) -> int:  
        '''
        Front wheels' steerig angle        
        '''      
        return self._steering_angle
    
    @steering_angle.setter    
    def steering_angle(self, value) -> None:
        '''
        Args:
        
        value (int): steering angle (between 45 and 135)
        '''
        if not isinstance(value, int):
            raise Exception(f"The value of car's steering angle schould be 'int', but '{type(value).__name__}' is given")
        if value < 45:
            value = 45
        elif value > 135:
            value = 135
        self._steering_angle = value
        self.front_wheels.turn(value)
        print(f"Steering angle set to {value}°")
        
    def drive_forward(self, value: int = 0) -> None:
        '''
        Drive forwards
        
        Args:        
        value (int): speed
        '''
        self._direction = "D"
        if not isinstance(value, int):
            raise Exception(f"The value of speed schould be 'int', but '{type(value).__name__}' is given")
        if value <= 0 or value > 100:
            raise Exception(f"The value of speed schould be between 0 and 100")
        else:            
            self.back_wheels.forward()
            self.set_speed(value)
            self.back_wheels.speed = self.get_speed()
            print(f"Driving forwards with speed of {value}")
    
    def drive_backward(self, value: int = 0) -> None:
        '''
        Drive backwards
        
        Args:
        value (int): speed
        '''
        self._direction = "R"
        if value <= 0:
            raise Exception("The value of speed schould be positiv number")
        else:            
            self.back_wheels.backward()
            self.set_speed(value)
            self.back_wheels.speed = self.get_speed()
            print(f"Driving backwards with speed of {value}")
    
    
    def drive_stop(self) -> None:
        '''                 
        Set _speed to 0  
        
        Set _direction to 'P'        
        '''
        self.set_speed(0)    
        self.emergency_stop = False    
        self._direction = "P"
        print("Car stops")
      
    @property  
    def emergency_stop(self):
        '''
        Emergency Stop
        '''
        return self._emergency_stop
    
    @emergency_stop.setter
    def emergency_stop(self, value = True):
        '''
        Args:        
        value (bool): default True
        '''
        if not isinstance(value, bool):
            raise Exception(f"The value of speed schould be 'bool', but '{type(value).__name__}' is given")           
        self._emergency_stop = value
    
    def get_speed(self) -> int:
        return self._speed
    
    def set_speed(self, value) -> None:
        self._speed = value
        self.back_wheels.speed = self._speed
    
    @property 
    def speed(self) -> int:
        '''
        Car Speed
        '''
        return self._speed
    
    @speed.setter
    def speed(self, value: int = 0) -> None:
        '''
        Args:        
        value (int): default 0
        '''
        self._speed = value
        self.back_wheels.speed = self._speed
    
    
    def get_direction(self):
        '''
        Returns: Driving Direction
        
        'P' -> None
        
        'D' -> Forward
        
        'R' -> Reverse 
        '''
        return self._direction