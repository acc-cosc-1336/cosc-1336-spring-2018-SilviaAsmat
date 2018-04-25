from src.homework.homework12.converter import Converter
from tkinter import Tk, Label, Button


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
                                     command=self.display_labels).grid(row=0)

        self.quit_button = Button(self, text='Quit', command=self.destroy).grid(row=3)

        self.mainloop()

    def display_labels(self):
        converter = Converter()
        miles = converter.get_miles_from_km(100)
        self.label1 = Label(self, text='km: 100 ').grid(row=1)
        self.label2= Label(self, text='miles: ' + miles).grid(row=2)