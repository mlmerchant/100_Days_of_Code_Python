from tkinter import *

API_ENDPOINT = "https://api.kanye.rest/"


def get_quote():
    import requests
    response = requests.get(url=API_ENDPOINT)
    response.raise_for_status()
    data = response.json()
    quote = data['quote']
    count = len(quote)
    if count < 15:
        font_size = 45
    elif count < 30:
        font_size = 35
    elif count < 50:
        font_size = 30
    elif count < 70:
        font_size = 25
    else:
        font_size = 20

    canvas.itemconfig(
        quote_text,
        text=quote,
        font=("Arial", font_size, "bold")
    )


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

get_quote()

window.mainloop()