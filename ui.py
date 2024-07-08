from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, data: QuizBrain):
        self.result = ""
        self.quiz = data
        self.window = Tk()
        self.window.title("Quiz.exe")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.qn_text = self.canvas.create_text((150, 125), text="", font=("Arial", 20, "italic"), fill="black",
                                               width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=40)

        self.score_label = self.score = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        check_img = PhotoImage(file="images/true.png")
        cross_img = PhotoImage(file="images/false.png")

        self.check = Button(image=check_img, highlightthickness=0, command=self.click_true)
        self.check.grid(row=2, column=0)

        self.cross = Button(image=cross_img, highlightthickness=0, command=self.click_false)
        self.cross.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.qn_text, text=q_text)
        else:
            self.canvas.itemconfig(self.qn_text, text="you've reached the end of the quiz")
            self.check.config(state="disabled")
            self.cross.config(state="disabled")
    def click_true(self):
        self.result = "true"
        is_right = self.quiz.check_answer(self.result)
        self.give_feedback(is_right)

    def click_false(self):
        self.result = "false"
        is_right = self.quiz.check_answer(self.result)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.update_idletasks()
        self.window.after(1000, self.get_next_question())




