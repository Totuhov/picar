
import time

from car_sensor import SensorCar


class ParcourOne():
    
    def __init__(self, car = SensorCar):
        self._car = car
    
    def run(self) -> None: 
        '''
        Driving in a circle with maximum steering angle: 
        
        The car drives for 1 second straight ahead, then for 8 seconds with maximum steering angle clockwise and stops. The car should then follow this schedule in reverse and return to the exit. return to the starting point. The procedure should be the opposite for a trip be repeated clockwise.
        ''' 
        def action():
                        
            try:     
                # Set refference to Car
                c = self._car         

                # Phase 1: Wait for 1 second
                self.timer(1)

                # Phase 2: Set steering angle to 90 and drive forward at speed 40 for 1 second
                c.steering_angle = 90
                c.drive_forward(40)                
                self.timer(1)

                # Phase 3: Reduce steering angle gradually to 45 over time
                while c.steering_angle > 45 and not c.emergency_stop:
                    c.steering_angle -= 5
                    time.sleep(0.1)

                # Phase 4: Wait for 4 seconds
                self.timer(4)

                # Phase 5: Set steering angle to 46 and wait for 4 seconds
                c.steering_angle = 46
                self.timer(4)

                # Phase 6: Stop the car
                c.drive_stop()
                self.timer(1)

                # Phase 7: Set steering angle to 45 and drive backward at speed 40 for 4 seconds
                c.steering_angle = 45
                c.drive_backward(40)
                self.timer(4)

                # Phase 8: Set steering angle to 46 and wait for 4 seconds
                c.steering_angle = 46
                self.timer(1)

                # Phase 9: Stop the car
                c.drive_stop()
                c.steering_angle = 90  # Reset steering angle to 90

                # Phase 10: Increase steering angle gradually to 135 over time
                while c.steering_angle < 135 and not c.emergency_stop:
                    c.steering_angle += 5
                    time.sleep(0.1)

                # Phase 11: Drive forward at speed 40 for 4 seconds
                c.drive_forward(40)
                self.timer(4)

                # Phase 12: Set steering angle to 134 and wait for 4 seconds
                c.steering_angle = 134
                self.timer(4)

                # Phase 13: Stop the car
                c.drive_stop()
                self.timer(1)

                # Phase 14: Set steering angle to 135 and drive backward at speed 40 for 4 seconds
                c.steering_angle = 135
                c.drive_backward(40)
                self.timer(4)

                # Phase 15: Set steering angle to 134 and wait for 4 seconds
                c.steering_angle = 134
                self.timer(4)

                # Phase 16: Reset steering angle to 90
                c.steering_angle = 90
            except Exception as e:          
                print(e)

        action()
        
        # The entire sequence is completed, stop the car
        self._car.drive_stop()       
        
    def timer(self, value):
        '''
        Run sleep timer and check for "emergency" flag 
        
        Args:
        value (int): time in seconds
        '''
        timer = 0.0
        c = self._car
        
        while timer < value:
            # Check for emergency stop condition
            if c.emergency_stop:
                raise Exception('Emergency Stop activated!') 
            time.sleep(0.2)
            timer += 0.2
        