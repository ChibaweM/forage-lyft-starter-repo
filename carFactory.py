from battery.model.nubbin import Nubbin
from battery.model.spindler import Splindler
from car import Car
from engine.model.capulet_engine import CapuletEngine
from engine.model.sternman_engine import SternmanEngine
from engine.model.willoughby_engine import WilloughbyEngine

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Splindler(current_date,last_service_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Splindler(current_date,last_service_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = SternmanEngine(current_mileage, last_service_mileage)
        battery = Splindler(current_date,last_service_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date,last_service_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(current_date,last_service_date)
        car = Car(engine,battery)
        return car