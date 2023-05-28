from abc import ABC, abstractmethod
 
NegativeMileageException = Exception("The current mileage cannot be less than the last service mileage.")

class Engine(ABC):
  @abstractmethod
  def needs_service():
    pass