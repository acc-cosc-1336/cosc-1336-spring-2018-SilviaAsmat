from src.homework.homework10.score_entry import ScoreEntry
#write import statement for ScoreEntry

#create a class named GameLog with a parameterless constructor-create an empty list of score_entries class attribute in
# constructor
#Create a class method add_score_entry with a score_entry parameter, in the method code append the score_entry parameter
#to the score_entries class attribute
#Create a display_log method with no parameters-in this method iterate through display_log and display each
#score entry to screen


class GameLog:

    def __init__(self):
        self.score_entries = []

    def add_score_entry(self, score_entry):
        self.score_entries.append(score_entry)

    def display_log(self):

        for value in self.score_entries:
            print("Entry ID:", value.score_entry_id, "Roll 1:", value.die1value,"Roll 2:", value.die2value)
