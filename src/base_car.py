from basisklassen import *

class BaseCar():              
    
    def __init__(self):             
        
        self.__steering_angle = 90 
        self.__speed = 0
        self.__direction = "P" 
        
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
        return self.__steering_angle
    
    @steering_angle.setter
    def steering_angle(self, value) -> None:
        if value < 45:
            value = 45
        elif value > 135:
            value = 135
        self.__steering_angle = value
        self.front_wheels.turn(value)
        print(f"Steering angle set to {value}°")
        
    def drive_forward(self, value: int = 0) -> None:
        '''
        Drive forwards
        Args:
        value (int): Speed
        '''
        self.__direction = "D"
        if value <= 0:
            raise Exception("The value of speed schould be positiv number")
        else:            
            self.back_wheels.forward()
            self.set_speed(value)
            self.back_wheels.speed = self.get_speed()
            print(f"Driving forwards with speed of {value}")
    
    def drive_backward(self, value: int = 0) -> None:
        '''
        Drive backwards
        Args:
        value (int): Speed
        '''
        self.__direction = "R"
        if value <= 0:
            raise Exception("The value of speed schould be positiv number")
        else:            
            self.back_wheels.backward()
            self.set_speed(value)
            self.back_wheels.speed = self.get_speed()
            print(f"Driving backwards with speed of {value}")
    
    
    def drive_stop(self) -> None:
        '''
        Stops motor        
        '''
        self.set_speed(0)
        self.__direction = "P"
        print("Car stops")
    
    def get_speed(self) -> int:
        return self.__speed
    
    def set_speed(self, value) -> None:
        self.__speed = value
        self.back_wheels.speed = self.__speed
    
    def get_direction(self) -> int:
        return self.__direction       

        
    def fahrparkur_1(self) -> None: 
        time.sleep(1)
        self.steering_angle = 90
        time.sleep(1)
        self.drive_forward(20)   
        time.sleep(3)
        self.drive_stop() 
        time.sleep(1) 
        self.drive_backward(20)   
        time.sleep(3)      
        self.drive_stop()       
    
    def fahrparkur_2(self) -> None: 
        time.sleep(1)
        self.steering_angle = 90
        
        # Das Auto fährt 1 Sekunde geradeaus
        self.drive_forward(40)   
        time.sleep(1)
        
        # dann für 8 Sekunden mit maximalen Lenkwinkel im Uhrzeigersinn
        self.steering_angle = 45 
        time.sleep(4)
        self.steering_angle = 46
        time.sleep(4)                
        self.drive_stop() # und stoppt.
        time.sleep(1)
        
        # Dann soll das Auto diesen Fahrplan in umgekehrter Weise abfahren und an den Aus‑gangspunkt zurückkehren
        self.steering_angle = 45 
        self.drive_backward(40)
        time.sleep(4)
        self.steering_angle = 46
        time.sleep(4) 
        self.drive_stop()
        time.sleep(1)
        
        # Die Vorgehensweise soll für eine Fahrt im entgegengesetzten Uhrzeigersinn wiederholt werden.
        self.steering_angle = 135
        self.drive_forward(40)
        time.sleep(4)
        self.steering_angle = 134
        time.sleep(4)
        self.drive_stop()
        time.sleep(1)
        
        self.steering_angle = 135
        self.drive_backward(40)
        time.sleep(4)
        self.steering_angle = 134
        time.sleep(4) 
        self.drive_stop()
        self.steering_angle = 90
        
    def test_front_wheels(self):
        self.steering_angle = 90
        time.sleep(0.5)
        self.steering_angle = 45
        time.sleep(0.5)
        self.steering_angle = 90
        time.sleep(0.5)
        self.steering_angle = 135
        time.sleep(0.5)
        self.steering_angle = 90
        time.sleep(0.5)
        self.steering_angle = 135
        time.sleep(0.5)
        self.steering_angle = 90
 