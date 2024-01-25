import random
from car_base import BaseCar
from data_service import DataService
from basisklassen import *
import time
from datetime import datetime
import threading

class SonicCar(BaseCar):
    def __init__(self):
        super().__init__()
                
        self._ultrasonic = Ultrasonic()  
        self.data_service = DataService("drive_data.json")
        
        self.start_event = threading.Event()
        self.stop_event = threading.Event()
        
        self._distance = self.distance()
    
    def distance(self, n: int=3, skip_errors: bool=False): 
               
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
        
    def run_exploration_tour(self, 
                             init_speed: int=30, 
                             min_distance: int=30, 
                             max_distance: int=100,
                             loops: int=100, 
                             random_direction: bool=True,
                             high_speed: bool=True,
                             ):
        self.emergency_stop = False 
        self.start_event.wait()  
        self.steering_angle = 90
        self.set_speed(init_speed)
        self.drive_forward(self.get_speed())      
        
        for i in range(loops):  
            if self.emergency_stop == True: 
                break 
            self._distance = self.distance()
               
            print(f"Obsticle detected at {self._distance} cm.")               
            self.__check_low_distance(init_speed, min_distance, self._distance)                            
            
            self.__check_normal_distance(init_speed, min_distance, max_distance, random_direction, self._distance)
            
            self.__check_far_distance(high_speed, max_distance, self._distance)                                
        
        print(i, 'Loops beendet.')        
        # self.data_service._save_to_file()
        self.drive_stop()
        self.stop_event.set()
            
    def run_until_obstacle_detected(self, speed: int=40, min_distance: int=20, print_distance: bool=True):
        
        self.steering_angle = 90
        self.drive_forward(speed)
        self._distance = self.distance()
        
        while self._distance >= min_distance or self._distance == -1:
            if print_distance:
                print(self._distance)
            self._distance = self.distance()            
            
        self.drive_stop()

    def __check_low_distance(self, init_speed: int, min_distance: int, distance: float):
    
        if 0 < self._distance < min_distance:
            self.drive_stop()                            
            self.steering_angle = 45  
            self.data_service.write_data(self.create_data())              
            self.drive_backward(init_speed)                     
            time.sleep(random.uniform(0.5, 2))              
            self.steering_angle = 135
            self.data_service.write_data(self.create_data())
            

    def __check_normal_distance(self, init_speed: int, min_distance: int, max_distance: int, random_direction: bool, distance: float):
        
        if (min_distance < distance <= max_distance) and random_direction:  
            self.set_speed(init_speed)
            self.drive_forward(self.get_speed())
            self.steering_angle = self.steering_angle + random.randint(-10, 10)
            
            self.data_service.write_data(self.create_data())

    def __check_far_distance(self, high_speed: bool, max_distance: int, distance: float):
        
        if (distance > max_distance or distance == -1) and high_speed:  
            self.steering_angle = 90  
            self.set_speed(min(self.get_speed() + 5, 50))
            self.drive_forward(self.get_speed())
            self.data_service.write_data(self.create_data())
    
    def measure_data(self, stop_event):
        print("measure data - Start")
        self.data_service.write_data(self.create_data())
        while not stop_event.is_set():
            time.sleep(0.2)
            self.data_service.write_data(self.create_data())

        self.data_service._save_to_file()
        print("measure data - Stop")
    
    def run_fahrparcour_4(self):
        
        thread1 = threading.Thread(target=self.run_exploration_tour)
        thread2 = threading.Thread(target=self.measure_data, args=(self.stop_event,))  # Pass stop_event to measure_data

        thread1.start()
        thread2.start()

        # Signal the first thread to start
        self.start_event.set()

        # Wait for the first thread to finish
        thread1.join()

        # Set the stop_event to signal the second thread to stop
        self.stop_event.set()

        # Wait for the second thread to finish
        thread2.join()

        print("Both threads have finished.")    
              
    def create_data(self):
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S.%f")[:-3]
        data_obj = {
            "speed": self.get_speed(),
            "obsticle_dist": self._distance,
            "wheels_angle": self.steering_angle,
            "direction": self.get_direction(),
            "time": formatted_time
            }
        return data_obj