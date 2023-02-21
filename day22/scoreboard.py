from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.init_score_board()
        
    
    def init_score_board(self):
        self.color('White')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score_board()
        
        
    def update_score_board(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, 'normal'))
    
    def increase_r_score(self):
        self.r_score += 1
    
    def increase_l_score(self):
        self.l_score += 1
        