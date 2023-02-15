# Project 
import random
from turtle import Turtle, Screen


colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def main():
    
    # prepare a screen
    screen = init_screen()
    
    # pop up textinput
    user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter a color: ")
    
    turtles = line_up_turtles()
    
    winning_color = race(turtles)
    
    print_result(winning_color, user_bet)
    
    
    screen.exitonclick()
    
    
def init_screen():
    # initialize screen for this project
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.colormode(255)
    
    return screen
    
def line_up_turtles():
    # prepare to memorize turtles
    all_turtles = list()
    
    # use it to line up turtle on start position
    start_position_y = -70
    
    # lining up turtles
    for color in colors:
        # initialize turtle
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=start_position_y)
        
        # change y position to line up turtles.
        start_position_y += 30
        
        # append a turtle to list
        all_turtles.append(new_turtle)
    
    return all_turtles
   
    
def at_goal(turtle):
    return turtle.xcor() > 220


def race(turtles):
    while True:
        for turtle in turtles:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
            if at_goal(turtle): 
                winning_color = turtle.pencolor()
                return winning_color


def print_result(result_color, user_bet):
    if result_color == user_bet:
        print(f"You've won! The {result_color} turtle is the winner!")
    else:
        print(f"You've lost! The {result_color} turtle is the winner!")        

if __name__== '__main__':
    main()