from sandbox.basecar_set import *
import random

class SonicCar(BaseCar):
    """A class for a car with an Ultra-Sonic Sensor

    Args:
    config: config file for the car

    Attributes:
    --------
    _ultrasonic: the Ultra-Sonic Sensor
    
    Methods
    --------
    distance(): returns the current distance to an obstacle in front of the car
    run_until_obstacle_detected(): car drives forward until an obstacle gets to close
    run_exploration_tour(): car drives randomly and navigates if an obstacle is in front
    __check_low_distance(): checks if an obstacle is to close
    __check_normal_distance(): checks if no obstacle is to close but not far enough to accelerate
    __check_high_distance(): checks if nothing is in the way and accelerates
    """
    def __init__(self, config="config.json", **kwargs):

        super().__init__(config, **kwargs)

        self._ultrasonic = Ultrasonic()

    def distance(self, n: int=3, skip_errors: bool=False):
        """ Calculates the distance to an obstacle in front of the car. If n>1 it 
        takes the mean distance of n measurements.

        Args:
            n (int, optional): Number of measurements. Defaults to 3.
            skip_errors (bool, optional): Boolen if false measurements should be skipped. Defaults to False.

        Returns:
            int: distance to an obstalce
        """
        result = 0
        number_valid_measurements = 0
        for _ in range(n):
            d = self._ultrasonic.distance()
            if d < 0:
                if skip_errors:
                    continue
            else:
                result += d 
                number_valid_measurements += 1
        if number_valid_measurements > 0:
            return result / number_valid_measurements
        else:
            return -1

    def run_until_obstacle_detected(self, speed: int=40, min_distance: int=40, print_distance: bool=False):
        """Lets the car drive as long as no obstacle is closer than min_distance

        Args:
            speed (int, optional): Speed at which to drive. Defaults to 40.
            min_distance (int, optional): Distance which is considered as to close for an obstacle. Defaults to 40.
            print_distance (bool, optional): Boolean if the distance should be printed in the console while driving. Defaults to False.
        """
        self.steering_angle = 90
        self.drive(speed)
        distance = self.distance()
        while distance >= min_distance or distance == -1:
            if print_distance:
                print(distance)
            self.write_to_log(distance=distance)
            distance = self.distance()
        self.stop()
        self._save_log(drive_name="run_until_obstacle_detected")

    def run_exploration_tour(self, 
                             init_speed: int=30, 
                             min_distance: int=30, 
                             max_distance: int=80,
                             loops: int=100, 
                             random_direction: bool=True,
                             high_speed: bool=True
                             ):
        """ Lets the car drive randomly in space. 

        Args:
            init_speed (int, optional): Initial speed. Defaults to 30.
            min_distance (int, optional): Distance which is considered to close for obstacles. Defaults to 30.
            max_distance (int, optional): Distance which is considered as enough free space to accelerate. Defaults to 80.
            loops (int, optional): Number of loops corresponds to the duration of the trip. Defaults to 100.
            random_direction (bool, optional): If True the car drives at random directions. Defaults to True.
            high_speed (bool, optional): If True the car accelerates if there is enough space. Defaults to True.
        """
        self.steering_angle = 90
        self.speed = init_speed
        self.drive(self.speed)
        for i in range(loops):
            distance = self.distance()                  
            self.__check_low_distance(init_speed, min_distance, distance)
            self.__check_normal_distance(init_speed, min_distance, max_distance, random_direction, distance)
            self.__check_far_distance(high_speed, max_distance, distance)

        print(i, 'Loops beendet.')
        self.stop()
        self._save_log(drive_name="run_exploration_tour")

    def __check_low_distance(self, init_speed: int, min_distance: int, distance: float):
        """Checks if an obstacle is to close

        Args:
            init_speed (int): Speed at which to drive backwards to avoid the obstacle.
            min_distance (int): Distance which is considered as to close for an obstacle.
            distance (float): Current distance to obstacles in front of the car.
        """
        if 0 < distance < min_distance:
            self.stop()                            
            self.steering_angle = 45                
            self.drive(speed=init_speed, direction=-1)                     
            time.sleep(random.random() + 1)              
            self.steering_angle = 90                 
            self.drive(self.speed)               
            self.write_to_log(distance=distance, used_mode = "change direction")  

    def __check_normal_distance(self, init_speed: int, min_distance: int, max_distance: int, random_direction: bool, distance: float):
        """Checks if nothing is to close to the car but not enough space to accelerate.

        Args:
            init_speed (int): Normal driving speed for the exploration tour
            min_distance (int): Distance which is considered as to close for an obstacle.
            max_distance (int): Distance which is considered as enough space in front of the car to accelerate.
            random_direction (bool): If Ture the car drives in random directions.
            distance (float): Current distance to an obstacle in front of the car.
        """
        if (min_distance < distance <= max_distance) and random_direction:  
            self.speed = init_speed
            self.steering_angle = self.steering_angle + random.randint(-10, 10)
            self.write_to_log(distance=distance, used_mode = "random direction")

    def __check_far_distance(self, high_speed: bool, max_distance: int, distance: float):
        """Checks if there is enough space to accelerate.

        Args:
            high_speed (bool): If True the car accelerates while driving and if there is enough space
            max_distance (int): Distance which is considered as enough space in front of the car to accelerate.
            distance (float): Current distance to an obstacle in front of the car.
        """
        if (distance > max_distance or distance == -1) and high_speed:  
            self.steering_angle = 90  
            self.speed = min(self.speed + 5, 50)
            self.write_to_log(distance=distance, used_mode = "high speed")

if __name__ == "__main__":
    car = SonicCar()
    car.run_until_obstacle_detected()