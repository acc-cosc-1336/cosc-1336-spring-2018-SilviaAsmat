from src.final_exam.q_employee.hourly_employee import HourlyEmployee
from src.final_exam.q_employee.salaried_employee import SalariedEmployee
from src.final_exam.q_player.player import Player
from src.final_exam.q_dna.motif import non_contiguous_motif


import unittest
#write import statements for required classes or functions

class TestFinalExam(unittest.TestCase):

    #3 points
    #Create a test case to test the non_contiguous_motif  function with values
    #['A', 'C','G','T','A','C','G','T','G','A','C','G'] that returns three values 3, 8, and 10
    def test_non_contiguous_motif(self):
        test = ['A', 'C','G','T','A','C','G','T','G','A','C','G']
        result = (3, 8, 10)
        self.assertEqual(result, non_contiguous_motif('GTA', test))
    #3 points
    #For the Player class create a test case, to test the check_come_out_roll
    #with argument values True, 8, and 9 the result should be 'Invalid range'
    def test_player_t_8_9(self):
        player = Player
        self.assertEqual('Invalid range', player.check_come_out_roll(8, 9, True))
    #3 points
    #For the Player class create a test case, to test the check_come_out_roll
    #with argument values False, 4 and 7 should return 'Loser'
    def test_player_t_6_5(self):
        player = Player
        self.assertEqual('Loser', player.check_come_out_roll(6, 5, True))
    
    #3 points
    #Add a test case for HourlyEmployee that calls the calculate method with values 10 and 80 to yield a result of 800.
    def test_Hourly_Employee(self):
        hourly_employee = HourlyEmployee('n/a', 'n/a', 'n/a', 'n/a')
        self.assertEqual(800, hourly_employee.calculate(10, 80))
    #3 points
    #Add a test case for SalariedEmployee that calls the calculate method with values 260000 to yield a result of 10000.
    def test_Salaried_Employee(self):
        salaried_employee = SalariedEmployee('n/a', 'n/a', 'n/a')
        self.assertEqual(10000,salaried_employee.calculate_biweekly_pay(260000))

    

    

unittest.main(verbosity=2)
        
