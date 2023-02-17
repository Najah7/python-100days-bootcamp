# Project Snake Game (first half)

from turtle import Screen, Turtle
import time

from snake import Snake


def main():
    screen = init_screen()
    
    snake = Snake()
    
    snake.setup_snake()
    
    screen.update()
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
        time.sleep(0.2)
        
        # とりあえず全身させている。
        snake.forward()
        
        
        # NOTE:無限ループしないために
        counter_for_dev += 1
        if counter_for_dev == 10: break
            
        

    
    screen.exitonclick()
    
    

def init_screen():
    # initialize a screen
    screen = Screen()
    # set size of the screen
    screen.setup(width=600, height=600)
    # set color of the screen
    screen.bgcolor("black")
    # set title of the game
    screen.title('Snake Game🐍')
    # updateのタイミングで画面を描写するための設定
    # NOTE:説明ではブラウン管モニターやGIFアニメーション（パラパラ漫画的な、静止画を素早く切り替えて動画に）などを例に説明していた
    screen.tracer(0)
    
    return screen
        

if __name__ == '__main__':
    main()