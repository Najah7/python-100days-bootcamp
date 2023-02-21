from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.init_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def init_ball(self):
        self.shape('circle')
        self.color('white')
        self.penup()
    
    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        # self.bounce_on_x()
    
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def bounce_on_y(self):
        self.y_move *= -1
    
    def bounce_on_x(self):
        self.x_move *= -1
        self.speed_up()
    
    def speed_up(self):
        self.move_speed *= 0.9
        
    def is_on_y(self):
        return self.ycor() > 280 or self.ycor() < -280
    
    def is_on_x(self):
        return self.xcor() > 380 or self.xcor() < -380


            
        