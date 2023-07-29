import requests
from datetime import datetime
import smtplib
import uncertainties
import time

my_email = "munibtrial@gmail.com"
password = "jeayascsjopqibze"

MY_LAT = 31.964962 # Your latitude
MY_LONG = 35.874036 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

hour_now = time_now.hour


while True:
    time.sleep(60)
    if iss_longitude == uncertainties.ufloat(MY_LAT, 5) and iss_latitude == uncertainties.ufloat(MY_LONG, 5):
        if hour_now > sunset or hour_now < sunrise:
            with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
                # connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="munibaldalati@yahoo.com",
                    msg="Subject:look up\n\n"
                        "look to the sky, ISS is near you!"
            )

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



