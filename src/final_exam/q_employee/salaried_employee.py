from src.final_exam.q_employee.employee import Employee

class SalariedEmployee(Employee):

    def __init__(self, yearly_rate, employee_id, name):
        Employee.__init__(self, employee_id, name)
        self.yearly_rate = yearly_rate
        
    def calculate(self):
        return self.yearly_rate/26
