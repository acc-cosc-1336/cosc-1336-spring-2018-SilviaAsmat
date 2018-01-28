from assignment2 import faculty_evaluation_result

from tkinter import Tk
from tkinter import Canvas
from rectangle import Rectangle
from text import Text
from assignment2 import get_ratings

class GraphApp(Tk):

    def __init__(self, headings, values, eval_result, *args, **kargs):
        Tk.__init__(self, *args, **kargs)

        canvas = Canvas(self, width=400, height=400)
        canvas.pack()
        
        cnt = 0
        for i in range(308, 0, -28):
            Text(canvas, 10, i, cnt, "black").draw()
            cnt += 10

        text_x = 35
        rec_x = 20
        rec_x1 = 50
        max_x = 300
        
        for i in range (0, 6):
            Text(canvas, text_x, 18, values[i], "black").draw()
            Rectangle(canvas, (rec_x,300,rec_x1,275*(1-values[i])+25), "red").draw()
            Text(canvas, text_x, 310, headings[i], "black").draw()
            text_x += 50
            rec_x += 50
            rec_x1 += 50

        Text(canvas, 50, 360, "Result=" + eval_result, "black").draw()


#create a new variable named ratings here and assign it the return value of
#an evaluation with the following numbers 10,5,30,25,100,400
#I've done this step for you
ratings = get_ratings(10,5,30,25,100,400)

#create a new variable named result and assign it 
result = faculty_evaluation_result (10, 5, 30, 25, 100, 400)# #here replace the Excellent string with
#the return value of the
#faculty_evalution_reslult function with this numbers  10,5,30,25,100,400

#run the program from menu Run->Run Module            

app = GraphApp(("ALW", "VOF", "OFT", "SOM", "RAR", "NEV"),
                ratings, result)
app.mainloop()
