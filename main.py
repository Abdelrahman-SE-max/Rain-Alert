import os
import datetime as dt
import pandas as pd
import smtplib
from random import choice

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
month = now.month
day = now.day

data = pd.read_csv("birthdays.csv")
dict_data = data.to_dict(orient="records")

all_letters = []
for i in range(3):
    with open(f"letter_templates/letter_{i + 1}.txt") as letter:
        all_letters.append(letter.read())


for person in dict_data:
    if person["month"] == month and person["day"] == day:
        name = person["name"]
        email = person["email"]

        person_letter = choice(all_letters)
        letter_with_name = person_letter.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday\n\n{letter_with_name}"
            )





