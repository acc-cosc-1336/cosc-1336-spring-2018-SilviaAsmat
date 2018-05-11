from src.final_exam.hourly_employee import HourlyEmployee
from src.final_exam.salaried_employee import SalariedEmployee


employees = {1: HourlyEmployee(1, 'joe', 10, 80), 2: SalariedEmployee(2, 'Mike', 80000)}


for i in employees:
    print(round(i.calculate(), 2))
