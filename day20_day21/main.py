# Project Snake Game (first half)

# NOTE:[::-1]でスライスを用いて、リストを逆順にできる。

from turtle import Screen, Turtle
import time

from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

def main():
    screen = init_screen()
    
    food = Food()
    snake = Snake()
    score = 0
    score_board = ScoreBoard(score)
    
    snake.setup_snake()
    
    screen.update()
    
    screen.listen()
    
    screen.onkey(snake.up,'Up')
    screen.onkey(snake.dwon,'Down')
    screen.onkey(snake.right, 'Right')
    screen.onkey(snake.left, key='Left')
    
    
    
    # 無限ループしない用のカウンタ
    counter_for_dev = 0
    
    while True:
        
        
        
        # 再レンダリングと少し動きに間を
        # NOTE:0.2秒に特に意味はない、見た感じの直感で
        screen.update()
        time.sleep(0.1)
        
        snake.move()
        
        # Detect collision with food
        if did_snake_get(food, snake):
            food.refresh()
            snake.extend()
            score_board.increase_score()
            score_board.print_score()
        
        # Detect collision with wall
        if is_on_wall(snake):
            score_board.print_game_over()
            break

        
        # Detect collision with tail.
        for snake_body in snake.snake[1:]:
            if not is_any_space(snake.head, snake_body):
                score_board.print_game_over()
                break
        
        # NOTE:無限ループしないために
        # counter_for_dev += 1
        # if counter_for_dev == 10: break
            
        
    # for dev
    screen.exitonclick()
    
    

def init_screen():
    # initialize a screen
    screen = Screen()
    # set size of the screen
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    # set color of the screen
    screen.bgcolor("black")
    # set title of the game
    screen.title('Snake Game🐍')
    # updateのタイミングで画面を描写するための設定
    # NOTE:説明ではブラウン管モニターやGIFアニメーション（パラパラ漫画的な、静止画を素早く切り替えて動画に）などを例に説明していた
    screen.tracer(0)
    
    return screen

# HACK：インタフェース。それに伴って名前も
def did_snake_get(food, snake):
    return snake.head.distance(food) < 15
    
def is_on_wall(snake):
    if not -SCREEN_WIDTH/2 < snake.head.xcor() < SCREEN_WIDTH/2 or \
            not -SCREEN_HEIGHT/2 < snake.head.ycor() < SCREEN_HEIGHT/2:
                return True
    return False

def is_any_space(head, snake_body):
    return not head.distance(snake_body) < 10
    
    
            

if __name__ == '__main__':
    main()