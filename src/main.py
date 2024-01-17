from fahrparcour import Fahrparkur
from base_car import BaseCar
from sonic_car import SonicCar

def run():
    car = SonicCar()       
    fp = Fahrparkur(car)
    # fp.fahrparkur_1()
    car.run_until_obstacle_detected()
    
if __name__ == "__main__":
    run()