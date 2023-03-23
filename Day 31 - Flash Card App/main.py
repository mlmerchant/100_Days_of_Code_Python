from tkinter import *
import pandas
import os

# --------------------------- GLOBAL VARIABLES ------------------------------#

dictionary = {}
front_card = "N/A"
first_turn = True
timer = "N/A"

# ---------------------------- CONSTANTS ------------------------------------#

BACKGROUND_COLOR = "#B1DDC6"
CARD_FRONT = "./images/card_front.png"
CARD_BACK = "./images/card_back.png"
RIGHT = "./images/right.png"
WRONG = "./images/wrong.png"
DICTIONARY = "./data/french_words.csv"
WORDS_LEFT_TO_LEARN = "./words_to_learn.csv"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
FRONT_LANGUAGE = "French"
BACK_LANGUAGE = "English"


# ----------------------------- WRONG ANSWER ---------------------------------- #

def wrong_answer():
    """Returns the card to the deck and calls a new card."""
    global first_turn
    try:
        window.after_cancel(timer)
    except NameError:
        pass
    if first_turn:
        first_turn = False
        show_new_card_front()
    else:
        show_new_card_front()


# ----------------------------- RIGHT ANSWER ---------------------------------- #

def right_answer():
    """Removes the current card from the deck and calls a new card."""
    global first_turn
    try:
        window.after_cancel(timer)
    except NameError:
        pass
    if first_turn:
        first_turn = False
        show_new_card_front()
    else:
        del dictionary[front_card]
        save_dictionary_to_file()
        show_new_card_front()


# ---------------------------- HELPERS ------------------------------------------- #

def show_new_card_front():
    """Show the front of a new random card from the remaining deck."""
    global timer
    global front_card
    global dictionary
    from random import choice
    if not dictionary:
        dictionary = {
            "Lesson Complete": "Restart App"
        }
        os.remove(WORDS_LEFT_TO_LEARN)
    front_card = choice(list(dictionary.keys()))
    canvas.itemconfig(word_text_object, text=front_card, fill="black")
    canvas.itemconfig(title_text_object, text=FRONT_LANGUAGE, fill="black")
    canvas.itemconfig(card_image, image=card_front)
    timer = window.after(3000, show_current_card_back)


def show_current_card_back():
    """Selects a new card from the deck and shows the front."""
    canvas.itemconfig(word_text_object, text=dictionary[front_card], fill="white")
    canvas.itemconfig(title_text_object, text=BACK_LANGUAGE, fill="white")
    canvas.itemconfig(card_image, image=card_back)


def save_dictionary_to_file():
    the_words_left_to_learn = [f"{x},{y}" for (x, y) in dictionary.items()]
    the_words_left_to_learn = "\n".join(the_words_left_to_learn)
    with open(WORDS_LEFT_TO_LEARN, "w") as f:
        f.write(the_words_left_to_learn)


def load_dictionary_from_file():
    with open(WORDS_LEFT_TO_LEARN, "r") as file:
        words_left_to_learn = file.read()
    words_left_to_learn = words_left_to_learn.split('\n')
    words_left_dictionary = {}
    for line in words_left_to_learn:
        temp = line.split(",")
        words_left_dictionary[temp[0]] = temp[1]
    return words_left_dictionary


# ---------------------------- LOAD DICTIONARY -------------------------- #

if not os.path.isfile(WORDS_LEFT_TO_LEARN):
    df = pandas.read_csv(DICTIONARY)
    dictionary = df.to_dict()   # Could have used:  df.to_dict(orient="records")
    front_dictionary = (dictionary[FRONT_LANGUAGE]).values()
    back_dictionary = (dictionary[BACK_LANGUAGE]).values()
    dictionary = {x: y for (x, y) in zip(front_dictionary, back_dictionary)}
    save_dictionary_to_file()
else:
    dictionary = load_dictionary_from_file()


# ---------------------------- CREATE GUI ------------------------------- #

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas Area
card_front = PhotoImage(file=CARD_FRONT)
card_back = PhotoImage(file=CARD_BACK)
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
# x, y, and picture required. Typically, half x and y of canvas to place in the middle.
card_image = canvas.create_image(400, 263, image=card_front)
title_text_object = canvas.create_text(400, 150, text="Click Any Button", fill="black", font=LANGUAGE_FONT)
word_text_object = canvas.create_text(400, 263, text="To Begin", fill="black", font=WORD_FONT)
canvas.grid(column=0, row=0, columnspan=2)

# Wrong Button
wrong_image = PhotoImage(file=WRONG)
wrong_button = Button(highlightthickness=0, image=wrong_image, command=wrong_answer, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

# Right Button
right_image = PhotoImage(file=RIGHT)
right_button = Button(highlightthickness=0, image=right_image, command=right_answer, bg=BACKGROUND_COLOR)
right_button.grid(column=1, row=1)

window.mainloop()
