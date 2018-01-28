class Text(object):

    def __init__(self, canvas, x, y, text, fill):

        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = text
        self.fill = fill

    def draw(self):
        self.canvas.create_text(self.x, self.y, text=self.text, fill=self.fill)
