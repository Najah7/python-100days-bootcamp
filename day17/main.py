# Project Quiz App

# Open Trivia Database:https://opentdb.com/

import sys

sys.path.append('../utils')
from output_helper import welcome

from data import QUESTION_DATA
from quiz_brain import Quiz

def main():
    welcome('Quiz App')
    
    quiz = Quiz()
    
    while quiz.still_has_question():
        # Ask a question
        quiz.ask_question()
        print('\n')
    
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.num_questions}")



            

if __name__ == '__main__':
    main()