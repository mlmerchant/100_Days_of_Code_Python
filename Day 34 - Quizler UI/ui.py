from tkinter import *
from quiz_brain import QuizBrain
from functools import partial

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        starter_text = "Amazon acquired Twitch in August 2014 for $940 million dollars."

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        # Score Label
        self.score_label = Label(
            fg="white",
            text="Score: 0",
            font=("aerial", 15),
            bg=THEME_COLOR,
        )
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            text=starter_text,
            fill="black",
            font=("Arial", 20, "italic"),
            width=300
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        # TrueButton
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=partial(
            self.check_answer,
            "True"
        ))
        self.true_button.grid(row=2, column=0)

        # FalseButton
        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=partial(
            self.check_answer,
            "False"
        ))
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        self.canvas.config(bg="white")

    def check_answer(self, answer):
        is_correct = self.quiz.check_answer(answer)
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
