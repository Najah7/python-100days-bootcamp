from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 150
CAR_START_POS = 0

class Car(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.init_car()
        
    def init_car(self):
        self.shape('square')
        random_color = random.choice(COLORS)
        self.color(random_color)
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.setheading(90)
        

class CarManager:
    
    def __init__(self) -> None:
        self.num_cars = NUM_CARS
        self.cars = [Car() for _ in range(self.num_cars)]
        self.go_to_start()
    
    def go_to_start(self):
        for car in self.cars:
            # HACK:3000の定数化。（いい感じの名前ひらめかず） 
            # NOTE:3000は車がどのくらい通り続けるか（ゲームの長さ）を決める数字。
            # 　※　大きくする車が通り続ける時間は伸びるが、車の配置の密度は減る。（車の数とバランスをとって決める必要あり。）
            start_x = random.randint(CAR_START_POS, 3000)
            start_y = random.randint(-250, 250)
            car.goto(start_x, start_y)
    
    def go_left(self):
        for car in self.cars:
            new_x = car.xcor() - MOVE_INCREMENT
            car.goto(new_x, car.ycor())
    