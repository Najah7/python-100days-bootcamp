import random

from data import QUESTION_DATA

class Quiz:
    
    def __init__(self) -> None:
        # NOTE:QUESTION_DATAはtextとanswerの2つのキーを持つ辞書
        self.questions = QUESTION_DATA
        self.num_questions = 0
        self.score = 0

    # HACK:メソッドの並び順はどうするべき？
    
    def ask_question(self):
        
        question = self.questions[self.num_questions]
        
        # NOTE:この位置で大丈夫そ？（choiceを聞くときに問題数を使いたいのでこの位置にした）
        self.increase_num_questions()
        
        choice = input(f"Q.{self.num_questions}: {question['text']}. (True/False):")
        
        if self.is_corrct_answer(question, choice):
            print("You got it right ")
            self.increase_score()
        else:
            print("That's wrong")
            
        print(f"The corrent answer was {question['answer']}")
        self.print_current_score()
    
    def still_has_question(self):
        return self.num_questions < len(self.ask_question)
        
    
    def is_corrct_answer(self, question, choice):
        return choice == question['answer'].lower()
    
    def print_current_score(self):
        print(f"Your current score is: {self.score}/{self.num_questions}")
        
        
    def increase_num_questions(self):
        self.num_questions += 1
    
    def increase_score(self):
        self.score += 1