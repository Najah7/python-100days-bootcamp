import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_SPEED = 0.1
COLLISION_DISTANCE = 22

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initialize compoments used in this game
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


game_is_on = True
while game_is_on:
    
    time.sleep(CAR_SPEED)
    screen.update()
    car_manager.go_left()
    
    screen.listen()
    
    screen.onkey(player.go_up, 'Up')
    screen.onkey(player.go_down, 'Down')
    
    if player.is_at_goal():
        scoreboard.increase_score()
        scoreboard.update_score_board()
        player.back_to_start()
        
    for car in car_manager.cars:
        # HACK:車にあたった時の検知する距離感。（横が長くて、縦が短いので、値を大きくすると横を通りすぎただけで衝突した検知してしまう。）
        if player.distance(car) < COLLISION_DISTANCE:
            # NOTE：衝突検知の距離感を調整する際に使うと便利なprint
            # print(player.distance(car))
            
            # print game over  
            scoreboard.print_game_over()
            game_is_on = False
        

screen.exitonclick()


