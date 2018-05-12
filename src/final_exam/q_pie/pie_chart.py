class PieChart:
    def __init__(self, list1):

        self.list = list1

    def draw(self):

        for arc in self.list:
            arc.draw()
