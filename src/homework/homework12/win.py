from src.homework.homework12.converter import Converter
from tkinter import Tk, Label, Button, Frame


# In  file win.py create a class named Win that displays the main window
# and two labels, see attached window.png file for layout.
# In the Win class create an instance of converter class and
# call the get_miles_from_km with a value of 100 the miles result should be 62.14.

# HW 12:In the Win class add two buttons, one with text 'Display Conversion' and the other one with text 'Quit.
# The display button will display the same labels from assignment 12, but this time it will only display after button clicked.
# Create a display_labels class method and make it the callback for the display button.
# The quit button will exit the Window
class Win(Tk):

    def __init__(self):
        Tk.__init__(self, None, None)

        self.display_labels = Button(self, text='Display Conversion',
                                     command=self.display_labels).grid(row=3, column=0)

        self.quit_button = Button(self, text='Quit', command=self.destroy).grid(row=3, column=1)

        self.mainloop()

    def display_labels(self):
        self.converter = Converter()
        km = 100
        miles = self.converter.get_miles_from_km(km)
        self.label = Label(self, text='km:' + ' ' + str(km)).grid(row=1)
        self.label = Label(self, text='miles:' + ' ' + format(miles, '.2f')).grid(row=2)