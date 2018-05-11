from src.final_exam.q_employee.hourly_employee import HourlyEmployee
from src.final_exam.q_employee.salaried_employee import SalariedEmployee

employees = {1: HourlyEmployee(10,80, 'joe', 1), 2: SalariedEmployee(80000, 2, 'Mike')}

for i in employees.values():
    print(round(i.calculate(), 2))
