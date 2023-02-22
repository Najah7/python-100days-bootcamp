import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_SPEED = 0.1
COLLISION_DISTANCE = 22


def main():
    # Screen setup
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # initialize compoments used in this game
    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()
    
    game_is_on = True
    while game_is_on:
        
        # rendering setup
        time.sleep(CAR_SPEED)
        screen.update()
        
        # move car from right to left
        car_manager.go_left()
        
        # handle user input
        screen.listen()
        screen.onkey(player.go_up, 'Up')
        screen.onkey(player.go_down, 'Down')
        
        # increase Score and get player back to start position  when player get to the goal
        if player.is_at_finish_line():
            scoreboard.increase_score()
            scoreboard.update_score_board()
            car_manager.go_to_start()
            player.go_to_start()
        
        # Detect collsion with cars
        for car in car_manager.cars:
            # HACK:車にあたった時の検知する距離感。（横が長くて、縦が短いので、値を大きくすると横を通りすぎただけで衝突した検知してしまう。）
            if player.distance(car) < COLLISION_DISTANCE:
                
                # NOTE：衝突検知の距離感を調整する際に使うと便利なprint （微調整用に残している）
                # print(player.distance(car))
                
                # print game over  
                scoreboard.print_game_over()
                game_is_on = False
            

    screen.exitonclick()

if __name__ == '__main__':
    main()


