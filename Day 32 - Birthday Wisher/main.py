import smtplib
import os
import datetime as dt
import pandas
from random import choice

# Never Hard Code Credentials!
# password is app password - follow URL returned in the error message.
my_email = os.environ.get('MY_EMAIL')
password = os.environ.get('PASSWORD')

BIRTHDAYS = "./birthdays.csv"
LETTER_TEMPLATES_FOLDER = "./letter_templates/"


def return_letter(recipient_name):
    letter_files = os.listdir(LETTER_TEMPLATES_FOLDER)
    letter_file = choice(letter_files)
    letter_file = LETTER_TEMPLATES_FOLDER + letter_file
    with open(letter_file) as file:
        raw_letter_contents = file.read()
    mail_merged_letter = raw_letter_contents.replace('[NAME]', recipient_name)
    return mail_merged_letter


def send_mail(from_address, email_provider, to_address, subject, text):
    """Send email from Google, Hotmail, or Yahoo using SMTP."""
    message = "Subject:" + subject + "\n\n" + text
    if email_provider == "Google":
        smtp_server = "smtp.gmail.com"
    elif email_provider == "Hotmail":
        smtp_server = "smtp.live.com"
    elif email_provider == "Yahoo":
        smtp_server = "smtp.mail.yahoo.com"
    else:
        raise Exception('send_mail only supports "Google, Hotmail, and Yahoo for email_provider!')
    with smtplib.SMTP(smtp_server) as connection:
        connection.starttls()
        connection.login(user=from_address, password=password)
        connection.sendmail(
            from_addr=from_address,
            to_addrs=to_address,
            msg=message
        )

# #################### Extra Hard Starting Project ######################


now = dt.datetime.now()
currentDay = now.day
currentMonth = now.month

# 1. Update the birthdays.csv
df = pandas.read_csv(BIRTHDAYS)
birthdays = df.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
for record in birthdays:
    if int(record["month"]) == currentMonth:
        if int(record["day"]) == currentDay:
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
            # with the person's actual name from birthdays.csv
            letter = return_letter(record["name"])
            # 4. Send the letter generated in step 3 to that person's email address.
            send_mail(
                from_address=my_email,
                email_provider="Google",
                to_address=record["email"],
                subject="Happy Birthday!",
                text=letter
            )
