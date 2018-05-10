import unittest
#write import statements for required classes or functions
from src.final_review.payroll import Payroll
from src.final_review.question5 import sum_values
from src.final_review.question6 import count_odd_even

class TestFinalExamReview(unittest.TestCase):

    #For Question 1, payroll class, Create test case to test the payroll class with values hours:
    #80 and rate: 10 the result should be 400.
    def test_payroll_w_80_and_10(self):
        payroll = Payroll(80, 10)
        self.assertEqual(800, payroll.calculate())

    #for Question 4  get_average function, create a test case case to test the average for a list of
    #numbers 10 15 20 30 40 result should be 23.

    #for Question 5 sum_values function, Create a test case that test sum_values with value 10 and ‘90’
    #the result should be 100.
    def test_sum_values(self):

        self.assertEqual(100, sum_values(10, '90'))

    #For Question 6 count_odd_even function, Create a test case to test the list [1,2,3,10,13, 15,17,20, 21,22]
    #the result should be 6 and 4.
    def test_count_even_odd(self):

        self.assertEqual((4,6), count_odd_even([1,2,3,10,13, 15,17,20, 21,22]))
        

    

    

unittest.main(verbosity=2)
        
