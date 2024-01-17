from fahrparkur import Fahrparkur
from base_car import BaseCar

def run():
    car = BaseCar()   
     
    fp = Fahrparkur(car)
    fp.fahrparkur_2()
    
if __name__ == "__main__":
    run()