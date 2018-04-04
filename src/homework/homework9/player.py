from src.homework.homework9.die import Die
#write import statement for Die class

'''
Create a Player class.

'''


class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''
        self.die1 = Die()
        self.die2 = Die()

    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        value1 = 0
        value2 = 0

        while value1 != value2:
            value1 = self.die1.roll()
            print("This is value 1: ", value1)
            value2 = self.die2.roll()
            print("This is value 2: ", value2)
