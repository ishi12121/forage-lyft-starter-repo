from engine.base import Engine, NegativeMileageException

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
       self.last_service_mileage = last_service_mileage
       self.current_mileage = current_mileage
        

    def needs_service(self):
        if self.current_mileage < self.last_service_mileage:
            raise NegativeMileageException
        return self.current_mileage >= self.last_service_mileage + 60000