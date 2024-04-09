from basisklassen import *
import datetime
import pandas as pd
import time
import json
import uuid

class BaseCar():
    """Class for a basic car.

    Args:
    config: config file for the car in json-format (see __init__)

    Attributes
    --------
    data dict: content of config file
            turning_offset : offset for computing the angle
            forward_A : rotating direction of wheel A
            forward_B : rotating direction of wheel B
    speed : speed of the car
    direction : driving direction of the car
    steering_angle : steering angle of the car
    logDict : dict for logging

    Methods
    --------
    drive(speed,direction): method for driving the car straight forwards or backwards
    stop(): method for stoping the car
    _log(): method for logging data collected while driving
    get_log(): method for getting the logged data
    save_log(): method for saving the logged data
    get_status(): method for getting current speed, direction and angle
    shake_front_wheels(): method for testing the basic steering
    test_drive_1(): method for a test drive
    test_drive_2(): method for a test drive
    """

    def __init__(self, config="config.json"):
        """Constructor for the BaseCar class. It will read the config file and set the attributes.

        Args:
            config: config file for the car with the following keys: turning_offset, forward_A, forward_B. Defaults to "config.json".
        """
        with open(config, "r") as f:
            self.data = json.load(f)
            turning_offset = self.data["turning_offset"]
            forward_A = self.data["forward_A"]
            forward_B = self.data["forward_B"]

        # Components
        self.__back_wheels = BackWheels(forward_A=forward_A, forward_B=forward_B)
        self.__front_wheels = FrontWheels(turning_offset=turning_offset)

        # interne Parameter
        self.is_driving = False
        
        # Fahrt-Einstellungen
        self.speed = 0
        self.direction = 1
        self.steering_angle = 90

        # Log-Variablen und andere
        self.reset_log_dict()

    @property
    def speed(self):
        """Property for speed.
        Returns:
            int: speed of the car
        """
        return self.__speed

    @speed.setter
    def speed(self, value):
        """Setter for speed.
        Raises:
            ValueError: if value is not an integer
        Args:
            value (int): new speed
        """
        try:
            value = min(100,value)
            value = max(0,value)
            self.__speed = int(value)
            if self.__speed == 0:
                #self.__direction = 1
                self.is_driving = False
            else:
                self.is_driving = True
            self.__back_wheels.speed = int(value)
        except ValueError:
            print("Speed muss eine Zahl sein!")

    # Should be removed, useless       
    @property
    def direction(self):
        """Property for direction.
        Returns:
            int: direction of the car
        """
        return self.__direction

    @direction.setter
    def direction(self, value):
        """Setter for direction.
        Args:
            value (int): new direction
        Raises:
            ValueError: if value is not an integer
        """
        try:
            if int(value) not in [-1, 1]:
                raise ValueError("Direction muss -1, 0 oder 1 sein!")
            #if value == 0:
            #    self.__speed = 0
            #    self.__back_wheels.stop()
            #    self.is_driving = False
            if value == -1:
                self.__back_wheels.backward()
            elif value == 1:
                self.__back_wheels.forward()
            self.__direction = int(value)      
        except ValueError:
            print("Direction muss eine Zahl sein!")

    @property
    def steering_angle(self):
        """Property for steering_angle.

        Returns:
            int: steering angle of the car
        """
        return self.__steering_angle

    @steering_angle.setter
    def steering_angle(self, angle):
        """Setter for steering_angle. Front_Wheels.turn() does not allow too large steering angles and uses maximum angles in this case. Therefore the set angle is queried again in the else statement.
        Args:
            angle: new steering angle
            alpha: constant for the steering angle. Defaults to 0.0.
        Raises:
            ValueError: if angle is not an integer
        """
        try:
            self.__steering_angle = float(angle)
            if angle == None:
                self.__front_wheels.turn(self.__steering_angle)
            else:
                self.__steering_angle = self.__front_wheels.turn(angle) 
                # .turn checks for angles in the wrong interval and return the angle used!
        except ValueError:
            print("Steering Angle muss eine Zahl sein!")

    def drive(self, speed: int, direction: int = 1):
        """Method for start driving
        Args:
            speed (int): speed at which to drive
            direction (int, optional): Driving direction. 1 for forwards, -1 for backwards. Defaults to 1.
        """
        self.speed = speed
        self.direction = direction
        
    
    def drive2(self, speed: int): # Experimental
        """Others Method for driving
        Args:
            speed (int): speed at which to drive, negative value indicate backward movement
        """
        self.speed = abs(speed)
        if speed >=0:
            self.direction = 1
        else:
            self.direction = -1

    def stop(self):
        """Method for stopping the car. 
        """
        self.speed = 0
        
       
    def set_status(self,steering_angle=90,speed=0,direction=1): # Experimental 
        self.steering_angle = steering_angle
        self.speed = 0
    
    def get_status(self):
        """Method which returns a dict of current speed, direction and angle.
        Returns:
            dict: Dictionary with current speed, direction and angle
        """
        return {
            'speed': self.__speed,
            'direction': self.__direction,
            'angle': self.__steering_angle,
        }
        
    def reset_log_dict(self):
        """Resets the log dictionary so a new log can be saved
        """
        self.log_dict = {"ts": [], "speed": [], "direction": [], "angle": []}
        
    def write_to_log(self, additional_dict: dict = None, **kwargs):
        """Method for logging of data collected while driving. By default
        time, speed, direction and angle are being logged. You either can pass 
        a dict for further values or keyword arguments

        Args:
            additional_dict (dict, optional): Dict with further values for logging. Defaults to None.
        """

        self.log_dict["ts"].append(datetime.datetime.now())
        self.log_dict["speed"].append(self.speed)
        self.log_dict["direction"].append(self.direction)
        self.log_dict["angle"].append(self.steering_angle)

        if isinstance(additional_dict, dict):
            for key, value in additional_dict.items():
                if key in self.log_dict:
                    self.log_dict[key].append(value)
                else:
                    self.log_dict[key] = [value]

        for key, value in kwargs.items():
            if key in self.log_dict:
                self.log_dict[key].append(value)
            else:
                self.log_dict[key] = [value]

    def get_log(self):
        """Returns the logged data as a pandas dataframe

        Returns:
            pandas dataframe: dataframe of logged data collected while driving
        """
        df = pd.DataFrame.from_dict(self.log_dict, orient='index').T
        return df

    def _save_log(self, drive_name: str = ""):
        """Method for saving the logged data as .csv file
        """
        run_id = str(uuid.uuid4())[:8]
        self.get_log().to_csv(f"log_of_trip_{drive_name}_{run_id}.csv")
        self.reset_log_dict()
        print(
            f"log_of_trip_{drive_name}_{run_id}.csv wurde erfolgreich gespeichert!")

    def test_drive_1(self, forward_secs: int = 3, sleep_secs: int = 1, backward_secs: int = 3, speed: int = 40):
        """Method for testdrive 1: driving forwards, stopping and driving backwards again.

        Args:
            forward_secs (int, optional): Time in seconds for driving forwards. Defaults to 3.
            sleep_secs (int, optional): Time in seconds for stopping and waiting. Defaults to 1.
            backward_secs (int, optional): Time in seconds for driving backwards. Defaults to 3.
            speed (int, optional): Speed at which to drive. Defaults to 40.
        """
        print('Start')
        self.steering_angle = 90
        self.drive(speed=speed, direction=1)
        time.sleep(forward_secs)
        self.stop()
        time.sleep(sleep_secs)
        self.drive(speed=speed, direction=-1)
        time.sleep(backward_secs)
        self.stop()
        print('Ende')

    def test_drive_2(self, forward_secs: int = 1, circle_secs: int = 8,
                     sleep_secs: int = 1, angles: list = [45, 135], speed: int = 40):
        """Method for testdrive 2: driving forwards, stopping, setting steering angle 
        and driving in a circle. Driving backwards and forwards again

        Args:
            forward_secs (int, optional): Time in seconds for driving forwards. Defaults to 1.
            circle_secs (int, optional): Time in seconds for driving in a circle. Defaults to 8.
            sleep_secs (int, optional): Time in seconds for driving waiting. Defaults to 1.
            angles (list, optional): Angles for which the testdrive should be done. Defaults to [45, 135].
            speed (int, optional): Speed at which to drive. Defaults to 40.
        """
        print('Start')
        for a in angles:
            self.steering_angle = 90
            self.drive(speed=speed)
            time.sleep(forward_secs)
            self.steering_angle = a
            time.sleep(circle_secs)
            self.stop()
            time.sleep(sleep_secs)
            self.drive(speed=speed, direction=-1)
            time.sleep(circle_secs)
            self.steering_angle = 90
            time.sleep(forward_secs)
            self.stop()
        print('Ende')

    # Weitere Methoden. Diese sind nicht Teil der Projektphase.

    def shake_front_wheels(self, tw=.2):
        """Method for testing if basic steering is working.

        Args:
            tw (float, optional): Time waiting between changes in steering angle. Defaults to .2.
        """
        self.steering_angle = 90
        time.sleep(tw)
        self.steering_angle = 45
        time.sleep(tw)
        self.steering_angle = 135
        time.sleep(tw)
        self.steering_angle = 90

if __name__ == "__main__":
    car = BaseCar()
    car.test_drive_1()
