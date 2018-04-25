from src.assignments.assignment12.converter import Converter
import tkinter


# In  file win.py create a class named Win that displays the main window
# and two labels, see attached window.png file for layout.
# In the Win class create an instance of converter class and
# call the get_miles_from_km with a value of 100 the miles result should be 62.14.


"""class Win:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.label1 = tkinter.Label(self.main_window, text='Km: 100 ')
        converter = Converter()
        miles = str(converter.get_miles_from_km(100))
        self.label2 = tkinter.Label(self.main_window, text='Miles: ' + miles)
        self.label1.pack()
        self.label2.pack()

        tkinter.mainloop()


# HW 12:In the Win class add two buttons, one with text 'Display Conversion' and the other one with text 'Quit.
# The display button will display the same labels from assignment 12, but this time it will only display after button clicked.
# Create a display_labels class method and make it the callback for the display button.
# The quit button will exit the Window"""
