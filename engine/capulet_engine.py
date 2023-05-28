from engine.base import Engine

class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.next_service_mileage = last_service_mileage + 30000
        self.current_mileage = current_mileage
    

    def needs_service(self):
        return self.current_mileage >= self.next_service_mileage
