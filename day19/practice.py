# This Lecture is for Instances, State and Higher Order Function

# NOTE:State：機器やソフトウェア、システム、あるいはそれらの取り扱う対象などについて、ある具体的な状況や状態、設定などを値やデータなどで表したものをステートという
# NOTE:State≒value of attribute

from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()

# イベントのlistenを開始する
screen.listen()

def move_forward():
    timmy.forward(10)
    

# キーボードの入力にハンドラを紐つける。（func：関数、key：キーボードの値）
# NOTE:Higher Order Function（高階関数）。言語には使えない言語もある
screen.onkey(key='space', fun=move_forward)


# Making an Etch-A-Sketch App

# NOTE:Rules
# f:Forwards
# b:Backwards
# l:counter-clockwise
# r:clockwise
# c:clear drawing

def move_forward():
    timmy.forward(10)
    
def move_backforward():
    timmy.backward(10)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)
    
def clear_drawing():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    
# add Event Listeners to keyboard input
screen.onkey(key='f', fun=move_forward)
screen.onkey(key='b', fun=move_backforward)
screen.onkey(key='l', fun=turn_left)
screen.onkey(key='r', fun=turn_right)
screen.onkey(key='c', fun=clear_drawing)

screen.exitonclick()