import unittest
from src.midterm.practice import get_km_per_hour
from src.midterm.practice import get_shipping_charge
from src.midterm.practice import get_total_of_numbers_squared
from src.midterm.practice import get_quiz_list




class Test_Practice(unittest.TestCase):

    def test_sample(self):
        self.assertEqual(1,1)

    def test_get_km_per_hour(self):
        self.assertEqual(32, get_km_per_hour(20, 60))

    #Write a test case for function get_shipping_charge with argument 2
    #return value should be 2.5

    def test_get_shipping_charge(self):
        self.assertEqual(1.25, get_shipping_charge(2))

    #Write a test case for function get_total_of_numbers_squared with argument 5
    #return value should be 30

    def test_get_total_of_numbers_squared(self):
        self.assertEqual(30, get_total_of_numbers_squared(5))

    #Write a test case for function get_quiz_list with argument
    '''
    [
    ['joe', 10, 15, 20, 30, 40]
    ['bill', 23, 16, 19, 22]
    ['sue', 8 22, 17, 14, 32, 17, 24, 21, 2, 9, 11, 17]
    ['grace', 12, 28, 21, 45, 26, 10, 11]
    ['john', 14, 32, 25, 16, 89]
    ]
    '''
    #return value should be
    '''
    ['sue', 'grace']
    '''


unittest.main(verbosity=2)
