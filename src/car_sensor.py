import datetime
import json
import threading
import time
import random

from car_sonic import SonicCar
from basisklassen import Infrared

class SensorCar(SonicCar):
    def __init__(self):
        super().__init__()
        
        with open("config.json", "r") as f:
            self.settings = json.load(f)         
              
        self.sensor = Infrared(self)
        self._sensor_values = self.sensor.read_analog()
        self._avg_ligth = float
        self.forward_sleep_index = self.settings['forward_sleep_index']
        self.backward_sleep_index = self.settings['backward_sleep_index']
        self.distance_from_start_avoid = self.settings['distanse_detection']
        
        self.start_event = threading.Event()
        self.stop_event = threading.Event()
        
    @property 
    def sensor_values(self) -> list:
        return self._sensor_values
    
    @sensor_values.setter
    def sensor_values(self, value) -> None:
        self._sensor_values = value
        
    @property 
    def avg_ligth(self) -> float:
        return self._avg_ligth
    
    @sensor_values.setter
    def avg_ligth(self, value) -> None:
        self._avg_ligth = value    
        
        
    def test_run(self):
        self.emergency_stop = False        
        self.speed = 20
        self._time_sleep_forward = self.forward_sleep_index / self.speed
        self._time_sleep_backward = self.backward_sleep_index / self.speed
        
        for i in range(50):
            if self.emergency_stop == True: 
                break
            self.drive_forward(self.speed)
            self.sensor_values = self.sensor.read_analog()
            
            min_value = min(self.sensor_values)
            max_value = max(self.sensor_values)
            
            if max_value - min_value < 5 or min_value > 15:
                self.drive_stop()
                if self.steering_angle >= 90:
                    self.steering_angle = 45
                else:
                    self.steering_angle = 135
                    
                self.drive_backward(self.speed)
                time.sleep(self._time_sleep_backward)
                self.steering_angle = 90
                continue
                
            index = self.sensor_values.index(min_value)  
            self.turn(index)             
                
            time.sleep(self._time_sleep_forward)        
        self.drive_stop()           
        
    def final_run(self):
        self.emergency_stop = False        
        self.speed = 20
        self._time_sleep_forward = self.forward_sleep_index / self.speed
        self._time_sleep_backward = self.backward_sleep_index / self.speed
        
        for _ in range(50):
            if self.emergency_stop == True: 
                break
            self._distance = self.distance() 
            
            if self._distance < self.distance_from_start_avoid:
                self.obsticle_detected_mode()
            
            self.drive_forward(self.speed)
            self.sensor_values = self.sensor.read_analog()
            
            min_value = min(self.sensor_values)
            max_value = max(self.sensor_values)
            
            if max_value - min_value < 10 or min_value > 25:
                self.drive_stop()
                if self.steering_angle >= 90:
                    self.steering_angle = 45
                else:
                    self.steering_angle = 135
                    
                self.drive_backward(self.speed)
                time.sleep(self._time_sleep_backward)
                self.steering_angle = 90
                continue
                
            index = self.sensor_values.index(min_value)  
            self.turn(index)             
                
            time.sleep(self._time_sleep_forward) 
                   
        self.drive_stop()  
        
    def obsticle_detected_mode(self):
        
        self._distance = self.distance()   
        self.drive_forward(20)    
        
        while self._distance < self.distance_from_start_avoid:
            if self.emergency_stop == True: 
                return
            
            while self.steering_angle < 135:
                self.steering_angle += 5
                time.sleep(0.1)
                    
            self._distance = self.distance()
                
        while self.steering_angle > 45:
            if self.emergency_stop == True: 
                return
            self.steering_angle -= 5
            time.sleep(0.1)                         
            
        self.sensor_values = self.sensor.read_analog() 
        
        while min(self.sensor_values) > 5: 
            if self.emergency_stop == True: 
                return  
            time.sleep(0.2)
            random_steering = random.choice([True, False])
            if random_steering:
                 self.steering_angle += 1
            else:   
                self.steering_angle -= 1                             
            self.sensor_values = self.sensor.read_analog()
         
        print(f'Min. sensor value: {min(self.sensor_values)} ---- time: {datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]}')
        return   
            
    def turn(self, argument):
        if argument == 0:
            self.steering_angle -= 30
        elif argument == 1:
            self.steering_angle -= 20
        elif argument == 2:
            self.steering_angle = 90
        elif argument == 3:
            self.steering_angle += 20
        elif argument == 4:
            self.steering_angle += 30            
    
    def measure_data(self, stop_event):
        print("measure data - Start")
        self.data_service.write_data(self.create_data())
        while not stop_event.is_set():
            time.sleep(0.2)
            self.data_service.write_data(self.create_data())

        self.data_service._save_to_file()
        print("measure data - Stop")

    def run_fahrparcour_5(self):
        thread1 = threading.Thread(target=self.test_run)
        thread2 = threading.Thread(target=self.measure_data, args=(self.stop_event,))
        
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
        
    def run_fahrparcour_6(self):
        thread1 = threading.Thread(target=self.final_run)
        thread2 = threading.Thread(target=self.measure_data, args=(self.stop_event,))
        
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
        
    def create_data(self):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S.%f")[:-3]
        data_obj = {
            "speed": self.get_speed(),
            "obsticle_dist": self._distance,
            "wheels_angle": self.steering_angle,
            "direction": self.get_direction(),
            "time": formatted_time,
            "sensor_values": {
                "sensor1": self._sensor_values[0],
                "sensor2": self._sensor_values[1],
                "sensor3": self._sensor_values[2],
                "sensor4": self._sensor_values[3],
                "sensor5": self._sensor_values[4]
            }
        }
        return data_obj
        