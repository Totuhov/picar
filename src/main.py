from sonic_car import SonicCar

def run():
    car = SonicCar()
    try:
        car.run_exploration_tour()
    except Exception as ex:
        print(f"Something's wrong! {ex}")
        car.drive_stop()
    
if __name__ == "__main__":
    run()