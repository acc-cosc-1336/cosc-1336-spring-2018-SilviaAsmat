import pickle
'''
Write a main function to create an empty dictionary and
a user-controlled loop to prompt for a widget name and quantity.
Add the values to the dictionary as key(widget name) and value(quantity) pairs.

After user decides to exit write data to file .

'''


def main():
    dictionary = {}
    keep_going = 'Y'
    while keep_going == 'Y':
        widget_name = input('Enter widget name: ')
        quantity = input('Enter quantity of widget: ')
        dictionary[widget_name] = quantity
        keep_going = input('Enter Y to continue: ')
    pickle.dump(dictionary, open("save.p", "wb"))
