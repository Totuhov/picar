from car_sensor import SensorCar

class ParcourThree():
    
    def __init__(self, car = SensorCar):
        self._car = car
        
    def run(self, speed: int=40, min_distance: int=20, print_distance: bool=True):
        
        c = self._car
        
        self.steering_angle = 90
        c.drive_forward(speed)
        self._distance = c.distance()
        print(c.emergency_stop) 
        try:
            while (self._distance >= min_distance or self._distance == -1):
                if c.emergency_stop:
                    raise Exception('Emergency Stop activated!')
                if print_distance:
                    print(self._distance)
                    self._distance = c.distance()         
        except Exception as e:                      
            print(e)
             
        print(self._distance)
        c.drive_stop()
        print('Parcour execution ended') 