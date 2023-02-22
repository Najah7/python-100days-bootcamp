from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self,) -> None:
        super().__init__()
        self.score = 0
        self.inti_score_board()
        self.update_score_board()
        
    def inti_score_board(self):
        self.color('black')
        self.penup()
        self.hideturtle()
        
    def update_score_board(self):
        self.clear()
        self.goto(0, 200)
        score_text = f"Score: {self.score}"
        self.write(score_text, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
    
    def print(self, message):
        self.clear()
        self.write(f'{message}', align='center', font=FONT)
        
    def print_game_over(self):
        self.goto(0, 0)
        self.print('GAME OVER')