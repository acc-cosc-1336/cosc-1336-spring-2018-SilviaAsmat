'''
5 points
Create a function named get_miles_per_hour with parameters kilometers and minutes that returns
the miles per hour.
Use .621371 as conversion ratio.
Return the string error 'Invalid arguments' if negative kilometers or minutes are given.
RUN THE PROVIDED TEST CASES TO VALIDATE YOUR CODE
'''


def get_miles_per_hour(kilometers, minutes):
    if kilometers < 0 or minutes < 0:
        return "Invalid Arguments"
    hours = minutes/60
    return kilometers/hours * .621371


'''
10 points
Create a function named get_bonus_pay_amount with parameter sales that returns the bonus pay amount.

Sales Range          Percentage
0    to  499             5%
500  to  999             6%
1000 to 1499             7%
1500 to 1999             8%

Return the string error 'Invalid arguments' if sales amount less than 0 or greater than 1999

Sample Data sales amount:
1000

Return Value:
70

'''


def get_bonus_pay(sales):
    if 0 <= sales <= 499:
        return sales*.05
    if 500 <= sales <= 999:
        return sales*.06
    if 1000 <= sales <= 1499:
        return sales*.07
    if 1500 <= sales <= 1999:
        return sales*.08
    else:
        return "Invalid arguments"


'''
10 points
Create a function named reverse_string that has one parameter named string1 that returns the
reverse of the string.

MUST USE A WHILE LOOP
DO NOT USE STRING SLICING!!!

Sample Data string1 argument:
My String Data

Returns:
ataD gnirtS yM

CREATE A TEST CASE IN THE exam_test.py file.
'''


def reverse_string(string1):
    string1_reverse = ''
    i = 0
    while i < len(string1):
        string1_reverse = string1[i] + string1_reverse
        i += 1
    return string1_reverse


'''
10 points
Create a function named get_list_min_max with a list1 parameter that returns the min and max values
in a list.

Sample Data list1 value:
['joe', 10, 15, 20, 30, 40]

Returns:
[10, 40]

CREATE A TEST CASE IN THE exam_test.py file.
'''


def get_list_min_max(list1):
    min_max = [min(list1[1:]), max(list1[1:])]
    return min_max




'''
25 points
Create a function named get_list_min_max_file with no parameters that reads the attached quiz.dat file
that returns all the min and max values from multiple lists.

You can use the get_list_min_max to get the min max for each list.

Sample quiz.dat file data:

joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10 11
john 14 32 25 16 89

Return Value:
[2,89]

'''


def get_list_min_max_file():
    quiz_file = open('quiz.dat', 'r')
    max_list_1 = []
    min_list_1 = []

    for line in quiz_file:
        line_int = []
        line1 = line.split()

        for i in line1[1:]:
            line_int.append(int(i))
            
        max_list_1.append(max(line_int))
        min_list_1.append(min(line_int))
    return_list = [min(min_list_1), max(max_list_1)]
    quiz_file.close()
    return return_list

"""def get_quiz_list_file():
    file = open('quiz.dat', 'r')
    return_list = []

    for line in file:
        list1 = line.split()
        if len(list1) > 7:
            return_list.append(list1[0])

    file.close()

    return  return_list"""


