from battery.base import Battery

class NubbinBattery(Battery):
  def __init__(self, last_service_date, current_date):
    self.next_service_date = last_service_date.replace(year=last_service_date.year + 4)
    self.current_date = current_date

  def needs_service(self):
    return self.current_date >= self.next_service_date