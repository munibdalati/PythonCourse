# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()
# print(day_of_week)
# print(now)
# date_of_birth = dt.datetime(year=1997, month=4, day=11, hour=21)
# print(date_of_birth)

import datetime as dt
import random
import smtplib

my_email = "munibtrial@gmail.com"
password = "jeayascsjopqibze"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
    print(random_quote)

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        # connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="munibaldalati@yahoo.com",
            msg=f"Subject:Thursday quote!\n\n{random_quote}"
        )
