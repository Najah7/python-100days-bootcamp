# This lecture is for Turtle Graphics, Tuples and Importing Moudules

# NOTE:Turtle Graphicsのドキュメント：https://docs.python.org/3/library/turtle.html

# NOTE:使う前に「sudo apt-get install python3-tk」でpythonのtk(tool kit)をダウンロードする

# NOTE:About Importing
# 1.Basic Import: import モジュール名
# 2.from Import: form　モジュール名 import　クラス, 関数 or 変数
# 3.ワイルドカードimport: 「from モジュール名 import *」（可読性が下がるので、ワイルドカードは基本使うべきではない）
# 4.as句：import モジュール名 as 別名(基本的にオリジナルで使用しない、慣習などがある場合に使う。)

# NOTE:Installing module：pip install モジュール名（詳しくはpipyを参照）

# tkinter（TK interface）（Graphical User Interfaceを提供）

from turtle import Turtle, Screen

# make an instance
# NOTE:名前はテキトウ
timmy = Turtle()

screen = Screen()
screen.colormode(255)

# Change shape of the turtle
timmy.shape('turtle')

# change color of the turtle
# NOTE:指定できる色(文字列)：TK color specification stirng(https://www.tcl.tk/man/tcl8.4/TkCmd/colors.html)
# NOTE:pencolor((r, g, b))で指定も可能(rgbのタプル)
timmy.color('red')

# change size of the pen
timmy.pensize(10)

# chage speed of the turtle animation
timmy.speed('fastest')

# move the turtle
# timmy.forward(100)
# timmy.right(90)

# drawing a Square
# NOTE:ループ内で変数を使わない場合は「_（アンダースコア）」を使う。
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)
    
# drawing a Dashed Line
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
    
# Drawing a Different Shape

import random

COLORS = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# MAX_SIDES = 15

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     timmy.color(random.choice(COLORS))
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
        

# for i in range(3, MAX_SIDES):
#     draw_shape(i)
    
# Drawing a Random Walk

directions = [0, 90, 180, 270]



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return (r, g, b)

def one_step():
    # change color
    timmy.pencolor(random_color())
    # take a step
    timmy.right(random.choice(directions))
    timmy.forward(30)
    
for _ in range(1000):
    one_step()



screen.exitonclick()
