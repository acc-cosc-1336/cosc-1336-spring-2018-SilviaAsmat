class Rectangle(object):

    def __init__(self, canvas, coords, fill, outline=None):

        self.canvas = canvas
        self.coords = coords
        self.fill = fill

    def draw(self):
        self.canvas.create_rectangle(self.coords, fill=self.fill)
        
