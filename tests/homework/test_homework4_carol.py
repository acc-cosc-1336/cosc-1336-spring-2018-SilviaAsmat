import unittest

#write the import statements to bring in homework 4 functions
#valid_letter_grade, get_credit_points, get_grade_points, and get_grade_point_average

#from src.homework.homework4 import sample_function
#from src.homework.homework4 import get_credit_points
#from src.homework.homework4 import valid_letter_grade

from homework4 import sample_function
from homework4 import get_credit_points
from homework4 import valid_letter_grade

class TestHomework4(unittest.TestCase):

    def test_example(self):
        '''
        This is just an example.
        DON'T CHANGE THIS FUNCTION
        '''
        #assert that 1 equals the return value of the sample_function(1) with argument 1
        self.assertEqual(1, sample_function(1));

    #WRITE 5 TESTS FOR get_credit_points with the letter A, B, C, D, and F as arguments
    def test_get_credit_points(letter_grade):
        #assert that A,B,C,D, and F will return credit points according to table.
        self.assertCreditPoints_4(4, get_credit_points(A))
        self.assertCreditPoints_3(4, get_credit_points(B))
        self.assertCreditPoints_2(4, get_credit_points(C))
        self.assertCreditPoints_1(4, get_credit_points(D))
        self.assertCreditPoints_0(4, get_credit_points(F))
        
    #WRITE 5 TESTS FOR get_credit_points with the letter a, b, c, d, and f as arguments

    #WRITE A TEST FOR valid_letter_grade with letter B as argument
    def test_valid_letter_grade(letter_grade):
        #assert that 'B' is a valid letter_grade
        self.assertValidInput(True, valid_letter_grade(B))  

    #WRITE A TEST FOR valid_letter_grade with letter Z as argument
    def test_NOT_valid_letter_grade(letter_grade):
        #assert that 'Z' is not a valid letter_grade
        self.assertNOTValidInput(False, valid_letter_grade(Z))


    #WRITE A TEST FOR get_grade_points with arguments 3 and 4

    #WRITE A TEST FOR get_grade_point_average with arguments 9.0 and 36.0


    #unittest.Main(verbosity=2)
    unittest(verbosity=2)
