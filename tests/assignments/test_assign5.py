from src.assignments.assignment5 import recursive_decimal_binary

import unittest


#write import for decimal to binary function


class Test_Assign4(unittest.TestCase):

    def test_sample_one(self):
        self.assertEqual(1,1)

    #write test cases with arguments 85 and 63 for recursive_decimal_binary function
    def test_85(self):
        self.assertEqual('01010101',recursive_decimal_binary(85))

    def test_63(self):
        self.assertEqual('00111111',recursive_decimal_binary(63))


