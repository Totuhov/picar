
from basisklassen import *

class Car():        
    front_wheels = FrontWheels()
    back_wheels = BackWheels()   
           
    def test_drive(self,f_speed: int = 0, f_time: int = 0, b_speed: int = 0, b_time: int = 0):
        """ test_drive
        Args:
        f_time (int): Time to drive forwards
        f_speed (int): Speed forwards
        b_time (int): Time to drive backwards
        b_speed (int): Speed backwards
        """          
        self.back_wheels.forward() 
        self.back_wheels.speed = f_speed        
        time.sleep(f_time)
        print(f"driving for {f_time} sec. forwards with {f_speed} speed")
        self.back_wheels.stop()
        time.sleep(2)
        self.back_wheels.speed = b_speed
        self.back_wheels.backward()
        time.sleep(b_time)
        print(f"driving for {b_time} sec. backwards with {b_speed} speed")
        self.back_wheels.stop()
      
def start():  
    car = Car() 
    car.test_drive(20, 3, 20, 3)    

if __name__ == "__main__":
    start()