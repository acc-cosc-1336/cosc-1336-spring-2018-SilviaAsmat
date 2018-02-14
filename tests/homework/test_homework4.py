import unittest

#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average
from src.homework.homework4 import sample_function

class TestHomework2(unittest.TestCase):

    def test_example(self):
        '''
        This is just an example.
        DON'T CHANGE THIS FUNCTION
        '''
        #assert that 1 equals the return value of the sample_function(1) with argument 1
        self.assertEqual(1, sample_function(1));

    #WRITE 5 TESTS FOR get_credit_points with the letter A, B, C, D, and F as arguments

    #WRITE 5 TESTS FOR get_credit_points with the letter a, b, c, d, and f as arguments

    #WRITE A TEST FOR valid_letter_grade with letter B as argument

    #WRITE A TEST FOR valid_letter_grade with letter Z as argument

    #WRITE A TEST FOR get_grade_points with arguments 3 and 4

    #WRITE A TEST FOR get_grade_point_average with arguments 9.0 and 36.0
