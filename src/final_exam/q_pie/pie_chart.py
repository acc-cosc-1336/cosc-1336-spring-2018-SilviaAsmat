from src.final_exam.Pie_Arc import Pie_Arc

class PieChart(Pie_Arc):
    def __init__(self, list):
        Pie_Arc.__init__(self,"")
        self.list = list

    def draw(self):
        pie_arc = Pie_Arc('')
        for i in self.list:
            pie_arc.draw()
