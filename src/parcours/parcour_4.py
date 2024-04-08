from datetime import datetime
from car_sensor import SensorCar

class ParcourFour():
    
    def __init__(self, car = SensorCar):
        self._car = car
                
    def run(self, 
                             init_speed: int=30, 
                             min_distance: int=30, 
                             max_distance: int=100,
                             loops: int=50, 
                             random_direction: bool=True,
                             high_speed: bool=True,
                             ):
        c = self._car
        c.emergency_stop = False
        c.steering_angle = 90
        c.set_speed(init_speed)
        c.drive_forward(c.get_speed())        
        ds = c._data_service
        ds.clear_data()
        
        try:
            for i in range(loops):
                if c.emergency_stop == True:
                    raise Exception('Emergency Stop activated!')  
                c._distance = c.distance()
                ds.write_data(self.create_data(self._car))   
                print(f"Obsticle detected at {c._distance:.2f}")               
                c._check_low_distance(init_speed, min_distance, c._distance)                            
                
                c._check_normal_distance(init_speed, min_distance, max_distance, random_direction, c._distance)
                
                c._check_far_distance(high_speed, max_distance, c._distance) 
                
            print(i, 'Loops beendet.')                                 
        except Exception as e:
            print(e) 
        ds.write_data(self.create_data(self._car))      
        ds.save_to_file()
        c.drive_stop()
        print('Parcour execution ended')
        

    def create_data(self, car = SensorCar) -> dict:
            """
            Create a data object containing information about the car's state.

            Parameters:
            - car (SonicCar, optional): An instance of the SonicCar class. Defaults to a new instance if not provided.

            Returns:
            object: A dictionary containing the following car-related information:
                - "speed": Current speed of the car.
                - "obstacle_dist": Distance to the obstacle as measured by the car.
                - "wheels_angle": Current steering angle of the car's wheels.
                - "direction": Current direction of the car.
                - "time": Formatted timestamp indicating when the data was created.

            Example:
            >>> sonic_car = SonicCar()
            >>> data = DataService.create_data(sonic_car)
            >>> print(data)
            {'speed': 20, 'obstacle_dist': 35.333, 'wheels_angle': 95, 'direction': 'D', 'time': '12:34:56.789'}

            Note:
            - The 'time' value is formatted as HH:MM:SS.sss, representing hours, minutes, seconds, and milliseconds.
            """        
            current_time = datetime.now()
            formatted_time = current_time.strftime("%H:%M:%S.%f")[:-3]
            data_obj = {
                "speed": car.get_speed(),
                "obsticle_dist": car._distance,
                "wheels_angle": car.steering_angle,
                "direction": car.get_direction(),
                "time": formatted_time,
                    "sensor_values": {
                    "sensor1": 0,
                    "sensor2": 0,
                    "sensor3": 0,
                    "sensor4": 0,
                    "sensor5": 0,
                }
            }
            return data_obj