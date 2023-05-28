from abc import ABC, abstractmethod

ArrayLengthException = Exception("Sensor data must be an array of exactly four numbers")
InvalidDataPointException = Exception("Sensor data points must be between 0 and 1 inclusive")

class Tires(ABC):
  @abstractmethod
  def needs_service():
    pass