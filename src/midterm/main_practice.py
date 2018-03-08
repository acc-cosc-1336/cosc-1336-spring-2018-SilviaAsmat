from src.midterm.practice import get_total_of_numbers_squared

#write import statement for get_total_of_numbers_squared

'''
Write a main function to ...
Loop until user opts not to.
Prompt user for a number.
Call the get_total_of_numbers_squared function with prompted number as argument.
Display the return value of get_total_of_numbers_squared function.
'''

#Call the main function


def main():
    keep_going = 'Y'
    while keep_going == 'Y':
        number = int(input("Enter number: "))
        sum_number_squared = get_total_of_numbers_squared(number)
        print(sum_number_squared)
        keep_going = input("Enter Y to continue: ")


main()
