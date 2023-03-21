import string
from json import JSONDecodeError
from tkinter import *
import json
import tkinter.messagebox as msgbox


# ---------------------------- REFERENCES --------------------------------------#
# https://tkdocs.com/tutorial/canvas.html

# ---------------------------- CONSTANTS ----------------------------------------#
FONT_SIZE = 10
DATABASE = "password.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    """Return a random 24 character password."""
    from random import shuffle

    letters = [x for x in string.ascii_letters]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', "="]
    password = letters + numbers + special
    shuffle(password)
    password = password[0:24]
    password = "".join(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)

    # Set the clipboard
    window.clipboard_clear()
    window.clipboard_append(password)


# --------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    """Return a username and password from a json database based on the website."""
    website = website_entry.get()

    # address blank input
    if not website:
        return

    # Open the database, and handle if it doesn't exist.
    try:
        with open(DATABASE, "r") as data_file:
            # reading old data
            data = json.load(data_file)

    except FileNotFoundError:
        msgbox.showerror("Error", "The database is empty.")
        return

    # Return results from the database:
    try:
        record = data[website]
        username = record["username"]
        password = record["password"]
        username_entry.delete(0, END)
        username_entry.insert(0, username)
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    except KeyError:
        msgbox.showerror("Error", "The database does not contain this key.")
        return

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    """Add a new password to a json database."""
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # catch invalid input
    if not website or not username or not password:
        msgbox.showerror("Error", "Missing fields are required.")
        return

    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    try:
        with open(DATABASE, "r") as data_file:
            # reading old data
            data = json.load(data_file)
            # updating old data with new data
            data.update(new_data)
    except (JSONDecodeError, FileNotFoundError):
        with open(DATABASE, "w") as data_file:
            # saving initial data
            json.dump(new_data, data_file, indent=4)
    else:
        with open(DATABASE, "w") as data_file:
            # saving updated data
            json.dump(data, data_file, indent=4)
    finally:
        website_entry.focus()
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

# Logo
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
# x, y, and picture required.
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_entry_length = 35
username_entry_length = 55
password_entry_length = 35

# website
website_label = Label(text="Website:", font=("Arial", FONT_SIZE, "bold"))
website_label.grid(sticky="e", column=0, row=1)
website_entry = Entry(width=website_entry_length)
website_entry.grid(sticky="w", column=1, row=1, columnspan=1)
website_entry.focus()
search_button = Button(text="Search", command=search)
search_button.grid(sticky="ew", column=2, row=1)


# username
username_label = Label(text="Email/Username:", font=("Arial", FONT_SIZE, "bold"))
username_label.grid(sticky="e", column=0, row=2)
username_entry = Entry(width=username_entry_length)
username_entry.grid(sticky="w", column=1, row=2, columnspan=2)

# password
password_label = Label(text="Password:", font=("Arial", FONT_SIZE, "bold"))
password_label.grid(sticky="e", column=0, row=3)
password_entry = Entry(width=password_entry_length)
password_entry.grid(sticky="w", column=1, row=3)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(sticky="ew", column=2, row=3)

# add button
add_button = Button(text="Add", command=add_password)
add_button.grid(sticky="ew", column=1, row=4 , columnspan=2)

window.mainloop()