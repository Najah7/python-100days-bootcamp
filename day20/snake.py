from turtle import Turtle

# NOTE:クラスの外でOK？
SIZE_OF_SQUARE = 20
MOVE_DISTANCE = 20

# use these for set a direction
UP = 90
DWON = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self, snake_head_position=[0, 0], size_of_snake=3) -> None:
        self.snake = [Turtle('square') for _ in range(size_of_snake)]
        self.head = self.snake[0]
        

    def setup_snake(self, color='white'):
        
        position_x = self.head.xcor()
        for snake_body in self.snake:
            snake_body.color(color)
            snake_body.penup()
            snake_body.goto(x=position_x, y=self.head.ycor())
            position_x -= SIZE_OF_SQUARE
    
    def move(self):
        # スネークの体の一部（タートル）のしっぽ側を一つ頭側に動かす処理
        # NOTE:スネークの配列は「頭→しっぽ」という風に並んだ配列
        for snake_body_num in range(len(self.snake) - 1, 0, -1):
            nex_x = self.snake[snake_body_num - 1].xcor()
            nex_y = self.snake[snake_body_num - 1].ycor()
            self.snake[snake_body_num].goto(x=nex_x, y=nex_y)
        self.head.forward(MOVE_DISTANCE) 
    
    def up(self):
        self.head.setheading(UP)
    
    def dwon(self):
        self.head.setheading(DWON)
        
    def left(self):
        self.head.setheading(LEFT)
    
    def right(self):
        self.head.setheading(RIGHT)
    
    