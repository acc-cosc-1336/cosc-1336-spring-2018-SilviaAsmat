import random
#Write an import statement for the Python random module

'''
Create a Die class to model a game die with 6 sides and values 1,2,3,4,5, and 6.

'''

class Die:

    def __init__(self):
        '''
        Define a constructor method with one attribute sides with a values of 6.
        '''
        self.sides = 6

    def roll(self):
        '''
        Defina a roll method that virtually rolls a die and returns the value.
        Use the Python random object to generate a random value from 1 to 6
        '''

        random_value = random.randint(0, self.sides)
        return random_value


