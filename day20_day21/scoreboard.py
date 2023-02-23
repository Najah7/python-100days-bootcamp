from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 24, 'normal')

class ScoreBoard(Turtle):
    
    def __init__(self, score):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as data_file:
            self.high_score = int(data_file.read())
        self.setup()
        self.move_to_upper_center()
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
        self.print(f'Score: {self.score} High Score: {self.high_score}')
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.print_score()