from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.init_player()

    def init_player(self):
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.penup()
        self.go_to_start()
    
    def go_up(self):
        nex_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, nex_y)
        
    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(0, new_y)
        
    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)