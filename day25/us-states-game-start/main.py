"""Project U.S. States Game"""

# importations
import pandas
from turtle import (
    Turtle,
    Screen,
    shape,
    )

# Constants
STATES_DF = pandas.read_csv('50_states.csv')
FONT = ("Arial", 10, 'normal')
NUM_STATE = len(STATES_DF['state'].to_list())

def main():
    """Main logic of U.S. States Game"""
    # initialize screen
    screen = init_screen()
    
    # add image on screen
    img = 'blank_states_img.gif'
    screen = add_img_on_screen(screen, img)
    
    # use it to check if game over
    guessed_states = []
    
    while len(guessed_states) < NUM_STATE:
        
        # get user's guess
        answer_state = screen.textinput(title=f'{len(guessed_states)}/50 State Correct', prompt="What's another state's name?")
        answer_state = answer_state.title()
        
        """
        NOTE: for dev. 
        you can use the code below to check names of states in console
        """
        print(STATES_DF['state'].to_list())
        
        if answer_state == 'Exit': break
        
        # name list of states in the 50_state.csv
        all_states = STATES_DF['state'].to_list()
        
        # If answer_state is one of the states in all the states of the 50_state.csv
        if answer_state in all_states:
            text = make_text()
            state_series = STATES_DF[STATES_DF['state'] == answer_state]
            position = get_position_from(state_series)
            text.goto(position)
            text.write(answer_state, align='center', font=FONT)
            guessed_states.append(answer_state)
    
    # states to learn.csv
    missing_states = []
    with open('learned.csv', 'w', newline='') as csv_file:
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        
        
    
def init_screen():
    """initialize screen for this project"""
    screen = Screen()
    screen.title('U.S. States Game')
    
    return screen

def add_img_on_screen(screen, img):
    """show up image on screen"""
    screen.addshape(img)
    shape(img)
    return screen

def make_text():
    """make text object from base on Turtle"""
    # make text from Tutle
    text = Turtle()
    text.color('Black')
    text.penup()
    text.hideturtle()
    
    return text

def get_position_from(state_series):
    """return (x, y) position tuple from state_series"""
    x = int(state_series.x)
    y = int(state_series.y)
    
    # just named the tuple
    state_position = (x, y)
    
    return state_position
    
if __name__ == '__main__':
    main()