from datetime import datetime
from car_sensor import SensorCar
from utilities.timer import Timer

class ParcourFive():
    
    def __init__(self, car = SensorCar, speed: int = 20):
        self._car = car
        self._speed = speed
        
    def run(self):
        c = self._car
        c.emergency_stop = False     
        ds = c._data_service
        
        self._timer = Timer(c)
        self._time_sleep_forward = c.forward_sleep_index / self._speed
        self._time_sleep_backward = c.backward_sleep_index / self._speed
        
        try:
            for i in range(50):
                if c.emergency_stop == True:
                    raise Exception('Emergency Stop activated!')
                c.drive_forward(self._speed)
                c.sensor_values = c.sensor.read_analog()
                
                min_value = min(c.sensor_values)
                max_value = max(c.sensor_values)
                
                ds.write_data(self.create_data(c))
                
                if max_value - min_value < 5 or min_value > 15:
                    c.drive_stop()
                    if c.steering_angle >= 90:
                        c.steering_angle = 45
                    else:
                        c.steering_angle = 135
                        
                    ds.write_data(self.create_data(c))
                    c.drive_backward(self._speed)
                    self._timer.timer(self._time_sleep_backward)
                    c.steering_angle = 90
                    continue
                    
                index = c.sensor_values.index(min_value)  
                c.turn(index)               
                self._timer.timer(self._time_sleep_forward) 
        except Exception as e:
            print(e)
        ds.write_data(self.create_data(c)) 
        ds.save_to_file()
        c.drive_stop()
        print('Parcour execution ended')
        
    def create_data(self, car = SensorCar) -> dict:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H:%M:%S.%f")[:-3]
        data_obj = {
            "speed": car.get_speed(),
            "obsticle_dist": car._distance,
            "wheels_angle": car.steering_angle,
            "direction": car.get_direction(),
            "time": formatted_time,
            "sensor_values": {
                "sensor1": car._sensor_values[0],
                "sensor2": car._sensor_values[1],
                "sensor3": car._sensor_values[2],
                "sensor4": car._sensor_values[3],
                "sensor5": car._sensor_values[4]
            }
        }
        return data_obj