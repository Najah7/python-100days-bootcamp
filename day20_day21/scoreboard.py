from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 24, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self, score):
        super().__init__()
        self.score = 0
        self.setup()
        self.move_to_upper_center()
        self.print_score()
        
        
        self.print_score()
    
    def setup(self):
        self.color('white')
        self.hideturtle()
    
    def move_to_upper_center(self):
        self.penup()
        self.goto(0, 250)
      
    def print(self, message):
        self.clear()
        self.write(f'{message}', align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
    
    def print_score(self):
        self.print(f'Score: {self.score}')
    
    def print_game_over(self):
        self.goto(0, 0)
        self.print('GAME OVER')