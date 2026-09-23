from app.color import Color
from blessed import Terminal

class Pixel():
    def __init__(self, x, y, color : Color, term : Terminal):
        self.x = x; self.y = y
        self.color = color
        self.term = term


    def draw_characters(self):
        return f"{self.term.move_xy(2*self.x, self.y)}{self.term.color_rgb(self.color.red, self.color.green, self.color.blue)}██"
            

        