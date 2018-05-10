class Payroll:

    def __init__(self, hours_worked, hourly_rate):

        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate(self):

        return self.hours_worked * self.hourly_rate
