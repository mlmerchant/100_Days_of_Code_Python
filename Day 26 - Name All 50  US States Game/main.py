import turtle
from utilities import *

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_answers = []

while len(correct_answers) < 50:
    answer = prompt(correct_answers, screen)
    # Skip to next if no answer provided.
    if answer:
        if answer in list_of_states():
            if answer not in correct_answers:
                correct_answers.append(answer)
                put_state_on_map(answer)
        # Captures cancel from prompt to exit program.
        elif answer == "Cancel":
            write_missed_states_to_file(correct_answers)
            break



screen.exitonclick()
