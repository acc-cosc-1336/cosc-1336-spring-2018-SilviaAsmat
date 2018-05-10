from payroll import Payroll

payroll_log = {1: Payroll(40, 10), 2:Payroll(30, 10), \
               3: Payroll(20, 10)}

print('Hours', 'Rate', 'Pay\n')
for p in payroll_log.values():
    print(p.hours_worked, p.hourly_rate,  p.calculate())
