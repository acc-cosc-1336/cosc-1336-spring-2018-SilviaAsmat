from src.final_exam.employee import Employee


class SalariedEmployee(Employee):

    def __init__(self, yearly_rate, employee_id, name):
        Employee.__init__(self, employee_id, name)
        self.yearly_rate = yearly_rate
        self.employee_id = employee_id
        self.name = name

    def calculate_biweekly_pay(self, yearly_rate):
        return yearly_rate/26
