#write import statement for recursive_decimal_binary

from src.assignments.assignment5 import recursive_decimal_binary
from src.assignments.assignment5 import add_one_to_bits

'''
Write a for loop from 1 to 255 and call the recursive_decimal_binary function with loop index/target variable
as an argument and print the decimal and binary value next to each other as follows:
1 00000001
2 00000010
3 00000011
4 00000100
5 00000101
6 00000110
7 00000111
etc
'''
def main():

    for i in range(1,256):
        final_string = recursive_decimal_binary(i, '00000000')
        print(i,' ',final_string)


main()