# Project Pong which is the famouse arcade game

# Steps to build this game
# 1.Create the Screen
# 2.Create and move a paddle
# 3.Create another
# 4.Create the ball and make it move
# 5.Detect collision with wall and bounce
# 6.Detect when paddle misses
# 7.Keep score

from turtle import Turtle, Screen
import time

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard


SCREEN_WIDTH=800
SCREEN_HEIGHT=600

def main():
    screen = init_screen()
    screen.tracer(0)
    
    # NOTE:一時的な処置。paddleを動かす関数内で使いたかったのglobalに（イベントハンドラで引数を指定できそうにないから）
    r_paddle = Paddle((350, 0))   
    l_paddle =Paddle((-350, 0))
    ball = Ball()
    score_board = ScoreBoard()
    screen.update()
    
    
    
    while True:
        

        time.sleep(ball.move_speed)
        screen.update()
        screen.listen()
        
        # oprating of right paddle
        screen.onkey(r_paddle.go_up, 'Up')
        screen.onkey(r_paddle.go_down, 'Down')
        # oprating of left paddle
        screen.onkey(l_paddle.go_up, 'w')
        screen.onkey(l_paddle.go_down, 's')
        
        ball.move()
        
        # Detect collision with wall
        if ball.is_on_y(): ball.bounce_on_y()
        if ball.is_on_x(): ball.bounce_on_x()
        
        # Detect collision with paddle
        if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or \
            ball.distance(l_paddle) < 50 and ball.xcor() < -320:
            ball.bounce_on_x()

        
        # Detect R paddle misses
        if ball.xcor() > 380:
            score_board.increase_l_score()
            score_board.update_score_board()
            ball.reset_position()
            
        # Detect L paddle misses
        if ball.xcor() < -380:
            score_board.increase_r_score()
            score_board.update_score_board()
            ball.reset_position()    
    
    
    screen.exitonclick()

def init_screen():
    screen = Screen()
    screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
    screen.bgcolor('black')
    screen.title('Pong')
    
    return screen


    



    
    

if __name__ == '__main__':
    main()