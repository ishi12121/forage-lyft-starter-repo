from engine.base import Engine

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.next_service_mileage = last_service_mileage + 60000
        self.current_mileage = current_mileage
        

    def needs_service(self):
        return self.current_mileage >= self.next_service_mileage