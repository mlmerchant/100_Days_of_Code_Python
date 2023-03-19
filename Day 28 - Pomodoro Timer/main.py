from tkinter import *

# ---------------------------- References ------------------------------- #
# https://colorhunt.co/

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"

# -------------------------- GLOBAL VARIABLES ------------------------------#
reps = 0
running = False
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_function():
    global running
    global reps
    running = False
    reps = 0
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN)
    session_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global running

    reps += 1

    # Keep 2 instances of clock from running at once
    if running:
        return
    else:
        running = True

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps in (1, 3, 5, 7):
        counter = work_sec
        current_period_text = "Work"
        current_period_color = GREEN
    elif reps in (2, 5, 6):
        counter = short_break_sec
        current_period_text = "Break"
        current_period_color = PINK
    elif reps == 8:
        counter = long_break_sec
        current_period_text = "Long Break"
        current_period_color = RED
    else:
        counter = 0
        current_period_text = "Reset"
        current_period_color = BLACK

    title_label.config(text=current_period_text, fg=current_period_color)
    count_down(counter)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    global CHECKMARK

    count_min = "{:01d}".format(count // 60)
    count_sec = "{:02d}".format(count % 60)
    clock_text = count_min + ":" + count_sec
    canvas.itemconfig(timer_text, text=clock_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps in (1, 3, 5, 7):
            checkmarks = CHECKMARK * ((reps + 1) // 2)
            session_label.config(text=checkmarks)
    start_timer()


# ---------------------------- UI SETUP ------------------------------- #
timer_sec = '00'
timer_min = '00'
session_count = 2

# Window
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=325, height="250")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# Title Label
title_label = Label(fg=GREEN, text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

# Start Button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text="Reset", command=reset_function, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Session Counter
session_label = Label(fg=GREEN, text=" ", font=(FONT_NAME, 15, "bold"), bg=YELLOW)
session_label.grid(column=1, row=4)

window.mainloop()
