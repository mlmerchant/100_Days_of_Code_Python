import smtplib
import os
import datetime as dt

QUOTES_FILE = "quotes.txt"

# Never Hard Code Credentials!
# password is app password - follow URL returned in the error message.
my_email = os.environ.get('MY_EMAIL')
password = os.environ.get('PASSWORD')
to_email = os.environ.get('TO_EMAIL')


def send_mail(from_address, email_provider, to_address, subject, text):
    """Send email from Google, Hotmail, or Yahoo using SMTP."""
    message = "Subject:" + subject + "\n\n" + text
    if email_provider == "Google":
        smtp_server = "smtp.gmail.com"
    elif email_provider == "Hotmail":
        smtp_server = "smtp.live.com"
    elif email_provider == "Yahoo":
        smtp_server = "smtp.mail.yahoo.com"
    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(user=from_address, password=password)
        connection.sendmail(
            from_addr=from_address,
            to_addrs=to_address,
            msg=message
        )


def random_quote():
    """Return a random quote from the QUOTES_FILE."""
    from random import choice
    with open(QUOTES_FILE) as f:
        quote = f.read()
    quote = quote.split("\n")
    quote = choice(quote)
    return quote


now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 4:
    send_mail(
        email_provider="Google",
        from_address=my_email,
        to_address=to_email,
        subject="Random Quote",
        text=random_quote()
    )
