import string
from tkinter import *


# ---------------------------- REFERENCES --------------------------------------#
# https://tkdocs.com/tutorial/canvas.html

# ---------------------------- CONSTANTS ----------------------------------------#
FONT_SIZE = 10
DATABASE = "password.csv"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
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

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    import pandas

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # catch invalid input
    if not website or not username or not password:
        import tkinter.messagebox
        tkinter.messagebox.showerror("Error", "Missing fields are required.")
        return

    # Create database if missing:
    import os.path
    if not os.path.isfile(DATABASE):
        database_template = {
            "Website": [],
            "Username": [],
            "Password": []
        }

        df = pandas.DataFrame(database_template)
        df.to_csv(DATABASE, index=False)

    df = pandas.read_csv(DATABASE)

    # see if website already loaded
    websites = df.Website
    websites = list(websites)
    if website in websites:
        import tkinter.messagebox
        tkinter.messagebox.showerror("Error", "Website already in password file.")
        return

    df2 = {
            "Website": website,
            "Username": username,
            "Password": password
    }

    df = df.append(df2, ignore_index=True)
    df.to_csv(DATABASE, index=False)

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

website_username_entry_length = 55
password_entry_length = 35

# website
website_label = Label(text="Website:", font=("Arial", FONT_SIZE, "bold"))
website_label.grid(sticky="e", column=0, row=1)
website_entry = Entry(width=website_username_entry_length)
website_entry.grid(sticky="w", column=1, row=1, columnspan=2)
website_entry.focus()

# username
username_label = Label(text="Email/Username:", font=("Arial", FONT_SIZE, "bold"))
username_label.grid(sticky="e", column=0, row=2)
username_entry = Entry(width=website_username_entry_length)
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
