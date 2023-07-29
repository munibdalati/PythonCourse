##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import pandas
import random
import os
import smtplib

my_email = "munibtrial@gmail.com"
password = "jeayascsjopqibze"

now = dt.datetime.now()
month = now.month
day = now.day
data = pandas.read_csv("birthdays.csv")
birthdays_list = data.to_dict(orient="records")
for i in birthdays_list:
    if i["month"] == month and i["day"] == day:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as file:
            contents = file.read()
            contents = contents.replace("[NAME]", i["name"])
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            # connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=i["email"],
                msg=f"Subject:Happy Birthday\n\n{contents}"
    )



