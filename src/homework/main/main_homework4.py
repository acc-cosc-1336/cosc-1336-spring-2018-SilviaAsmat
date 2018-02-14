import unittest
from src.homework.homework4 import valid_letter_grade
from src.homework.homework4 import get_grade_point_average
from src.homework.homework4 import get_grade_points
from src.homework.homework4 import get_credit_points

#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average

'''
Use the functions from homework4 to...
Write code to prompt the user for number of students and grades.
Create a nested loop to collect letter grades and credit hours for each student.
Validate the letter grade is in accepted range if not prompt user for letter again.
From the letter grade, get the credit points for that class.
Calculate grade points (How? Research GPA calculation).
Sum grade points and credit hours for each student.
Calculate GPA for each student.
Display Student 1(etc) GPA is 3.77. Format the GPA to two values.
'''

#WRITE YOUR CODE IN THE MAIN FUNCTION BELOW
def main():

    number_of_students = int(input('Enter amount of students:'))
    number_of_grades = int(input('Enter number of grades:'))
    print("")
    i = 1
    gpas = []
    while i < number_of_students+1:
        grade_points_total = 0
        credit_hours_total = 0
        for j in range(1,number_of_students+1):
            letter_grade = str(input('Enter a grade:'))
            is_valid = valid_letter_grade(letter_grade)
            if is_valid == False:
                letter_grade = str(input('Enter a grade:'))

            credit_points = get_credit_points(letter_grade)
            credit_hours = int(input('Enter credit hours:'))
            credit_hours_total += credit_hours
            print("")

            grade_points = get_grade_points(credit_hours, credit_points)
            grade_points_total += grade_points
        gpa = get_grade_point_average(credit_hours_total, grade_points_total)
        gpas.append(gpa)
        i += 1
    print("")

    for k in range (0,number_of_students):
        gpa = gpas[k]
        gpa_formatted = '{0:.2f}'.format(gpa)
        print('Student ', str(k+1),' GPA is: ',gpa_formatted)


#CALL THE MAIN FUNCTION
main()