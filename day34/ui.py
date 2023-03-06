from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        # initialize ui commponets
        self._init_windows()
        self._init_score()
        self._init_canvas()
        true_img = PhotoImage(file='images/true.png')
        false_img = PhotoImage(file='images/false.png')
        self._init_btn(true_img, false_img)
        
        self.get_next_question()
                
        self.window.mainloop()
    
    def _init_windows(self):
        self.window = Tk()
        self.window.title('Quizzer')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
    
    def _init_score(self):
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
    def _init_canvas(self):
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text='Some Qestion Text',
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic')
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
    
    def _init_btn(self, true_img, false_img):
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.click_true)
        self.true_btn.grid(row=2, column=0)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.click_false)
        self.false_btn.grid(row=2, column=1)
        
        
    
    def get_next_question(self):
        self.canvas.config(bg='white')
        
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disable')
            
    def click_true(self):
        self.give_feedback(self.quiz.is_correct("True"))
        
    
    def click_false(self):
        self.give_feedback(self.quiz.is_correct("False"))
        
    
    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, self.get_next_question)