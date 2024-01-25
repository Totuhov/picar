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
        self._emergency_stop = False    
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

        
    def fahrparkur_1(self) -> None: 
        '''
        Forward and backward:
        
        The car drives slower Speed straight ahead for 3 seconds, stop for 1 second and travel for 3 seconds backward.
        ''' 
        def run():
            # Initialize timer
            timer = 0.0

            # Phase 1: Wait for 1 second
            while timer < 1:
                # Check for emergency stop condition
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2 

            # Reset timer for the next phase
            timer = 0.0

            # Phase 2: Set steering angle to 90 for 1 second
            self.steering_angle = 90
            while timer < 1:
                # Check for emergency stop condition
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2

            # Reset timer for the next phase
            timer = 0.0

            # Phase 3: Drive forward at speed 20 for 3 seconds
            self.drive_forward(20)  
            while timer < 3:
                # Check for emergency stop condition
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2

            # Reset timer for the next phase
            timer = 0.0

            # Phase 4: Stop for 1 second
            self.drive_stop() 
            while timer < 1:
                # Check for emergency stop condition
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2

            # Reset timer for the next phase
            timer = 0.0

            # Phase 5: Drive backward at speed 20 for 3 seconds
            self.drive_backward(20)  
            while timer < 3:
                # Check for emergency stop condition
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2

            # The entire sequence is completed, stop the car
            self.drive_stop() 

        # Run the defined function
        run()   
        self.drive_stop()       
    
    def fahrparkur_2(self) -> None: 
        '''
        Driving in a circle with maximum steering angle: 
        
        The car drives for 1 second straight ahead, then for 8 seconds with maximum steering angle clockwise and stops. The car should then follow this schedule in reverse and return to the exit. return to the starting point. The procedure should be the opposite for a trip be repeated clockwise.
        ''' 
        def run():
            timer = 0.0  # Initialize timer

            # Phase 1: Wait for 1 second
            while timer < 1:
                if self.emergency_stop:
                    return  # Exit function if emergency stop is activated
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 2: Set steering angle to 90 and drive forward at speed 40 for 1 second
            self.steering_angle = 90
            self.drive_forward(40)
            while timer < 1:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 3: Reduce steering angle gradually to 45 over time
            while self.steering_angle > 45:
                self.steering_angle -= 5
                time.sleep(0.1)

            # Phase 4: Wait for 4 seconds
            while timer < 4:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 5: Set steering angle to 46 and wait for 4 seconds
            self.steering_angle = 46
            while timer < 4:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 6: Stop the car
            self.drive_stop()
            while timer < 1:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 7: Set steering angle to 45 and drive backward at speed 40 for 5 seconds
            self.steering_angle = 45
            self.drive_backward(40)
            while timer < 5:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 8: Set steering angle to 46 and wait for 4 seconds
            self.steering_angle = 46
            while timer < 4:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 9: Stop the car
            self.drive_stop()
            self.steering_angle = 90  # Reset steering angle to 90

            # Phase 10: Increase steering angle gradually to 135 over time
            while self.steering_angle < 135:
                self.steering_angle += 5
                time.sleep(0.1)

            # Phase 11: Drive forward at speed 40 for 4 seconds
            self.drive_forward(40)
            while timer < 4:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 12: Set steering angle to 134 and wait for 4 seconds
            self.steering_angle = 134
            while timer < 4:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 13: Stop the car
            self.drive_stop()
            while timer < 1:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 14: Set steering angle to 135 and drive backward at speed 40 for 4 seconds
            self.steering_angle = 135
            self.drive_backward(40)
            while timer < 4:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 15: Set steering angle to 134 and wait for 4 seconds
            self.steering_angle = 134
            while timer < 4:
                if self.emergency_stop:
                    return 
                time.sleep(0.2)
                timer += 0.2
            timer = 0.0

            # Phase 16: Reset steering angle to 90
            self.steering_angle = 90

        run()
        self.drive_stop()
         