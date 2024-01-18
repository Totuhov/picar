
import time
from base_car import BaseCar

class Fahrparkur():
        
    def __init__(self, car: BaseCar):     
        self.car = car
        
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
         