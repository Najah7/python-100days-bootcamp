from turtle import Turtle

# NOTE:クラスの外でOK？
SIZE_OF_SQUARE = 20
MOVE_DISTANCE = 20


class Snake:
    
    def __init__(self, snake_head_position=[0, 0], size_of_snake=3) -> None:
        self.snake = [Turtle('square') for _ in range(size_of_snake)]
        self.head_position_x = snake_head_position[0]
        self.head_position_y = snake_head_position[1]
        

    def setup_snake(self, color='white'):
        
        position_x = self.head_position_x
        position_y = self.head_position_y
        for snake_body in self.snake:
            snake_body.color(color)
            snake_body.penup()
            snake_body.goto(x=position_x, y=position_y)
            position_x -= SIZE_OF_SQUARE
    
    def up(self):
        self.move()
        self.snake[0].forward(MOVE_DISTANCE)
    
    def dwon(self):
        self.move()
        self.snake[0].backward(MOVE_DISTANCE)
        
    def left(self):
        self.move()
        self.snake[0].left(90)
        self.snake[0].forward(MOVE_DISTANCE)
    
    def right(self):
        self.move()
        self.snake[0].right(90)
        self.snake[0].forward(MOVE_DISTANCE)
    
    # HACK:命名
    def move(self):
        # スネークの体の一部（タートル）のしっぽ側を一つ頭側に動かす処理
        # NOTE:スネークの配列は「頭→しっぽ」という風に並んだ配列
        for snake_body_num in range(len(self.snake) - 1, 0, -1):
            nex_x = self.snake[snake_body_num - 1].xcor()
            nex_y = self.snake[snake_body_num - 1].ycor()
            self.snake[snake_body_num].goto(x=nex_x, y=nex_y)    