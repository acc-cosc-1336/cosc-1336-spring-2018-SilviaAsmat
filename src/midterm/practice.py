def get_km_per_hour(miles, total_minutes):
    '''
    Write a program that asks user for miles ridden on a bike and the total time ridden. Display average
    speed per hour in kilometers
    CREATE A TEST CASE FOR THIS FUNCTION
    :param miles:  Miles ridden on a bike
    :param total_minutes: Total minutes elapsed
    :return: Average speed per hour to hundredths place
    '''

    hours = total_minutes / 60

    return round(miles / hours * 1.6, 2)



'''
Create a function get_shipping_charge with one parameter named weight 
that returns rate per pound according to this table.
CREATE A TEST CASE FOR THIS FUNCTION

Weight                      Rate per Pound
0 to 2                      1.25
Over 2 but less than 6      2.75
Over 6 but less than 10     3.75
Over 10                     4.50

'''
#review void function


def get_shipping_charge(weight):
    rate_per_pound = 0
    if 0 <= weight <= 2:
        rate_per_pound = 1.25
    elif 2 < weight <= 6:
        rate_per_pound = 2.75
    elif 6 < weight <= 10:
        rate_per_pound = 3.75
    elif weight > 10:
        rate_per_pound = 4.50
    return rate_per_pound
'''
Create a function get_total_of_numbers_squared with a parameter named num
tha returns the total sum of the numbers squared.
CREATE A TEST CASE FOR THIS FUNCTION 

Sample Data
param num value 5
0
1
4
9
16

Returns 30
'''


def get_total_of_numbers_squared(num):
    sum_num_squared = 0
    for i in range(0, num):
        num_squared = i**2
        sum_num_squared += num_squared
    return sum_num_squared



'''
Create a function get_quiz_list that returns a two dimensional list of students, 
that have more than six quiz scores.
CREATE A TEST CASE FOR THIS FUNCTION.
param: list
Sample Data:
[
['joe', 10, 15, 20, 30, 40]
['bill', 23, 16, 19, 22]
['sue', 8, 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17]
['grace', 12, 28, 21, 45, 26, 10, 11]
['john', 14, 32, 25, 16, 89]
]

Return Value

'''


def get_quiz_list(list):
    name = []
    for i in list:
        student_list = list[i]
        if len(student_list) > 7:
            name.append('student_list[0]')
    return name

#review files

