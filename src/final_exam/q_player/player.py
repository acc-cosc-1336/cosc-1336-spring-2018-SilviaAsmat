class Player:

    def check_come_out_roll(self, d1, d2,b=True):
        sum = d1+d2
        if d1 > 0 or  d1 > 6 and  d2 < 0 or d2 > 6:
            return 'Invalid range'
        elif sum == 7 or sum == 11 and b==True:
            return 'Winner'
        elif sum == 7 or sum == 11 and b==False:
            return 'Loser'
        elif sum == 2 or sum == 3 or sum == 12 and b==True:
            return 'Loser'
        elif sum == 2 or sum == 3 or sum == 12 and b==False:
            return 'Winner'
        else:
            return sum
