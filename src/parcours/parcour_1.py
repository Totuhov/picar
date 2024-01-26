from utilities.timer import Timer
from car_sensor import SensorCar


class ParcourOne():
    
    def __init__(self, car = SensorCar):
        self._car = car
        self._timer = Timer(car)
    
    def run(self):
        '''
        Forward and backward:
        
        The car drives slower Speed straight ahead for 3 seconds, stop for 1 second and travel for 3 seconds backward.
        '''         
        # Set refference to Car and Timer
        c = self._car
        t = self._timer
        try:

            # Phase 1: Wait for 1 second            
            t.timer(1)                       

            # Phase 2: Set steering angle to 90 for 1 second
            self.steering_angle = 90
            t.timer(1)

            # Phase 3: Drive forward at speed 20 for 3 seconds
            c.drive_forward(20)  
            t.timer(3)

            # Phase 4: Stop for 1 second
            c.drive_stop() 
            t.timer(1)

            # Phase 5: Drive backward at speed 20 for 3 seconds
            c.drive_backward(20)  
            t.timer(3) 
        except Exception as e:          
            print(e)
            # The entire sequence is completed, stop the car
        c.drive_stop()
        print('Parcour execution ended')       
        