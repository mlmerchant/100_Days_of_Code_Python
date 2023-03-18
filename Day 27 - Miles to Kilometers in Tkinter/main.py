# References
# https://docs.python.org/3/library/tkinter.html
# https://tcl.tk/man/tcl8.6/TkCmd/
# https://replit.com/@appbrewery/tkinter-widget-demo

import tkinter

FONT_SIZE = 18


def button_clicked():
    if not miles_entry.get() == "":
        if miles_entry.get().isnumeric():
            km = 1.609344 * int(miles_entry.get())
            km = round(km)
            result_label["text"] = str(km)
        else:
            result_label["text"] = 0
    else:
        result_label["text"] = 0


window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width="300", height="140")
window.config(padx=10, pady=20)

# Entry
miles_entry = tkinter.Entry(width=15)
miles_entry.grid(column=1, row=0)
window.config(padx=10)

my_label1 = tkinter.Label(text="is equal to", font=("Arial", FONT_SIZE))
my_label1.grid(column=0, row=1)

my_label2 = tkinter.Label(text="Km", font=("Arial", FONT_SIZE))
my_label2.grid(column=2, row=1)

my_label3 = tkinter.Label(text=" Miles", font=("Arial", FONT_SIZE))
my_label3.grid(column=2, row=0)

# Button
button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Result Label
result_label = tkinter.Label(text="0", font=("Arial", FONT_SIZE))
result_label.grid(column=1, row=1)

# Keeps window on the screen.
window.mainloop()
