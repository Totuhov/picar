import time

from car_sensor import SensorCar

class Timer():
    """
        Initialize a Timer object.

        Args:
        car (SensorCar): An instance of the SensorCar class, representing the car
                        that the timer is associated with. Defaults to SensorCar.
        """
    def __init__(self, car=SensorCar):        
        self._car = car
    
    def timer(self, value):
        '''
        Run sleep timer and check for "emergency" flag 

        Args:
        value (int): Time in seconds for the timer to run.
        '''
        timer = 0.0
        c = self._car
        
        while timer < value:
            # Check for emergency stop condition
            if c.emergency_stop:
                raise Exception('Emergency Stop activated!') 
            time.sleep(0.2)
            timer += 0.2
        