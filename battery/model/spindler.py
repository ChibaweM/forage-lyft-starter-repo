from battery.battery import Battery
from utils import add_years_to_date

class Splindler(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_serfice(self):
        date_of_service = add_years_to_date(self.last_service_date , 2)
        if date_of_service < self.current_date:
            return True
        else:
            return False