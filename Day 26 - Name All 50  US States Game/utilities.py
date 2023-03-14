import pandas
from state_text import StateText
STATES_FILE = "50_states.csv"


def prompt(correct_answers, screen):
    """Provide an input prompt for answering the States."""
    num_correct = len(correct_answers)
    answer_state = screen.textinput(title=f"{num_correct}/50 States Correct", prompt="What's another state's name?")
    if answer_state is None:
        answer_state = "Cancel"
    return answer_state.title()


def list_of_states():
    """Provide a list of all 50 States."""
    df = pandas.read_csv(STATES_FILE)
    return df["state"].tolist()


def put_state_on_map(answer):
    """Get coordinates for a state and pass it to a turtle function."""
    df = pandas.read_csv(STATES_FILE)
    row = df[df.state == answer]
    state_text = StateText(row.state.item(), int(row.x), int(row.y))


def write_missed_states_to_file(answers_list):
    """Writes the missed states to a CSV file."""
    missed_states = []
    df = pandas.read_csv(STATES_FILE)
    for state in list_of_states():
        if state not in answers_list:
            missed_states.append(state)
    missed_states_df = pandas.DataFrame()
    missed_states_df['Missed States'] = missed_states
    missed_states_df.index += 1
    missed_states_df.to_csv("Missed_States.csv")

