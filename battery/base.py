from abc import ABC, abstractmethod
NegativeTimeException = Exception("The current date cannot be before the last service date.")

class Battery(ABC):
  @abstractmethod
  def needs_service():
    pass