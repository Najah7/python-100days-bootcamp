from turtle import Turtle

class Paddle(Turtle):
    """Paddleクラス"""
    
    def __init__(self, position) -> None:
        super().__init__()
        self.turn_into_paddle()
        self.goto(position)
        
        
    def turn_into_paddle(self):
        self.shape("square")
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
            
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        