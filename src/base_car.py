from basisklassen import *

class BaseCar():      
    
    __steering_angle = 90
    front_wheels = FrontWheels()
    back_wheels = BackWheels() 
    
    def __init__(self):
        self.front_wheels.turn(90)  
    
    @property
    def steering_angle(self) -> int:        
        print(f"Steering angle: {self.__steering_angle}°")
        return self.__steering_angle
    
    @steering_angle.setter
    def steering_angle(self, value) -> None:
        self.__steering_angle = value
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
        self.back_wheels.speed = 0
    
    def get_speed(self) -> int:
        return self.back_wheels.speed
    
    def get_direction(self) -> int:
        return self.back_wheels.forward_A
           
class Fahrparkur():
    car = BaseCar
        
    def __init__(self, car: BaseCar):     
        self.car = car
        
    def test_weels(self):
        fw = self.car.front_wheels
        fw.turn(45)
        time.sleep(.5)
        fw.turn(90)
        time.sleep(.5)
        fw.turn(130)
        time.sleep(1.5)
        
    def fahrparkur_1(self) -> None: 
        time.sleep(1)
        car = self.car
        car.front_wheels.turn(90)
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
        car.front_wheels.turn(90)
        car.drive_forward(40)   
        time.sleep(1)
        car.steering_angle = 45 
        car.front_wheels.turn(car.steering_angle)
        time.sleep(8)   
        car.steering_angle = 90
        car.front_wheels.turn(car.steering_angle)
        car.drive_stop()
        car.steering_angle = 90
        car.front_wheels.turn(car.steering_angle)
           
      
def start():    
    car = BaseCar()
    testdrive = Fahrparkur(car) 
    testdrive.test_weels()
    testdrive.fahrparkur_1()
    testdrive.fahrparkur_2()  

if __name__ == "__main__":
    start()