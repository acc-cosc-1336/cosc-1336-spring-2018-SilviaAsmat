from src.final_exam.q_employee.employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, hourly_rate, worked_hours, employee_id, name):
        Employee.__init__(self, employee_id, name)
        self.hourly_rate = hourly_rate
        self.worked_hours = worked_hours
        
    def calculate(self):
        return self.hourly_rate*self.worked_hours
