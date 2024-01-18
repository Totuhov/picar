from basisklassen import *

class BaseCar():              
    
    def __init__(self):               
            
        self.front_wheels = FrontWheels()
        self.back_wheels = BackWheels() 
        self.front_wheels.turn(90)
        self.__steering_angle = 90 
        self.__speed = 0
        
    
    @property
    def steering_angle(self) -> int:        
        print(f"Steering angle: {self.__steering_angle}°")
        return self.__steering_angle
    
    @steering_angle.setter
    def steering_angle(self, value) -> None:
        self.__steering_angle = value
        self.front_wheels.turn(value)
        print(f"Steering angle set to {value}°")
        
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
            self.set_speed(value)
            self.back_wheels.speed = self.get_speed()
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
            self.set_speed(value)
            self.back_wheels.speed = self.get_speed()
            print(f"Driving backwards with speed of {value}")
    
    
    def drive_stop(self) -> None:
        '''
        Stops motor        
        '''
        self.set_speed(0)
        print("Car stops")
    
    def get_speed(self) -> int:
        return self.__speed
    
    def set_speed(self, value) -> None:
        self.__speed = value
        self.back_wheels.speed = self.__speed
    
    def get_direction(self) -> int:
        return self.back_wheels.forward_A         

    def test_weels(self):
        print("Start wheels test")
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
        print("End wheels test")
        
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
        
        # Das Auto fährt 1 Sekunde geradeaus
        car.drive_forward(40)   
        time.sleep(1)
        
        # dann für 8 Sekunden mit maximalen Lenkwinkel im Uhrzeigersinn
        car.steering_angle = 45 
        time.sleep(4)
        car.steering_angle = 46
        time.sleep(4)                
        car.drive_stop() # und stoppt.
        time.sleep(1)
        
        # Dann soll das Auto diesen Fahrplan in umgekehrter Weise abfahren und an den Aus‑gangspunkt zurückkehren
        car.steering_angle = 45 
        car.drive_backward(40)
        time.sleep(4)
        car.steering_angle = 46
        time.sleep(4) 
        car.drive_stop()
        time.sleep(1)
        
        # Die Vorgehensweise soll für eine Fahrt im entgegengesetzten Uhrzeigersinn wiederholt werden.
        car.steering_angle = 135
        car.drive_forward(40)
        time.sleep(4)
        car.steering_angle = 134
        time.sleep(4)
        car.drive_stop()
        time.sleep(1)
        
        car.steering_angle = 135
        car.drive_backward(40)
        time.sleep(4)
        car.steering_angle = 134
        time.sleep(4) 
        car.drive_stop()
        car.steering_angle = 90
    
    def fahrparkur_test(self) -> None:
        pass