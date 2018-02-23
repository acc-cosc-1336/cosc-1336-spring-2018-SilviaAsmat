import unittest
from src.assignments.assignment6 import get_count_A_C_G_and_T_in_string
#write the import for function get_count_A_C_G_and_T_in_string


class Test_Assign6(unittest.TestCase):

    def test_countACGT_w_string_ATGCTTCAGAAAGGTCTTACG(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string ATGCTTCAGAAAGGTCTTACG
        '''
        expected = 6, 4, 5, 6
        actual = get_count_A_C_G_and_T_in_string('ATGCTTCAGAAAGGTCTTACG')
        self.assertTupleEqual(expected, actual)


    def test_count_ACGT_w_stringAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC(self):
        '''
        Create a test case to test the count of As, Cs, Gs, and Ts in string
        AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
        '''
        expected = 20, 12, 17, 21
        actual = get_count_A_C_G_and_T_in_string('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
        self.assertEqual(expected, actual)
