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
            # NOTE:この処理により、画面の並び(しっぽ→頭)とsankeクラスのリスト（頭→しっぽ）の並びが逆になるので、以後注意
            position_x -= SIZE_OF_SQUARE
    
    def get_new_tail(self):
        # get tail
        old_tail = self.snake[-1]
        # make new tail
        new_tail = Turtle('square')
        new_tail.color('white')
        new_tail.penup()
        # move to tail of the snake
        new_tail.goto(old_tail.position())
        
        return new_tail
        
    
    def extend(self):
        new_tail = self.get_new_tail()
        self.snake.append(new_tail)
    
    def move(self):
        # スネークの体の一部（タートル）のしっぽ側を一つ頭側に動かす処理
        # NOTE:ここで最後から一つずつ前に動かすことのよって、しっぽが伸びていくようになる。（追加した時はしっぽとしっぽの前の要素が同じ位置（同じx座標）なので、しっぽの位置は変化しない。）
        for snake_body_num in range(len(self.snake) - 1, 0, -1):
            nex_x = self.snake[snake_body_num - 1].xcor()
            nex_y = self.snake[snake_body_num - 1].ycor()
            self.snake[snake_body_num].goto(x=nex_x, y=nex_y)
        self.head.forward(MOVE_DISTANCE) 
    
    def up(self):
        # 来た方向に戻れないように
        if self.head.heading() != DWON:
            self.head.setheading(UP)
    
    def dwon(self):
        # 来た方向に戻れないように
        if self.head.heading() != UP:
            self.head.setheading(DWON)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    