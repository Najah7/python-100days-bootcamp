# Project Making a Spirograph

from turtle import Turtle, Screen
import random

timmy = Turtle()

def main():
    
    timmy.speed('fastest')

    screen = Screen()
    screen.colormode(255)

    draw_spirograph(5)
        
    screen.exitonclick()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)
    
        
if __name__ == '__main__':
    main()