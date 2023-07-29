import requests
from twilio.rest import Client
import os

api_key = "938448f596d4d7ac0cbbfe730326da2f"
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
account_sid = 'AC3e09ae250855d60eca0f88453f22b8ec'
auth_token = '1ef44e8d9ee5e4c5f995184183ddf417'

weather_params = {
    "lat": 31.945368,
    "lon": 35.928371,
    "exclude": "current,minutely,daily",
    "APPID": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.raise_for_status())
weather_data = response.json()
weather_list = []
will_rain = False
for i in range(0, 12):
    weather_code = weather_data["hourly"][i]["weather"][0]["id"]
    weather_list.append(weather_code)
print(weather_list)
for i in weather_list:
    if i < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+16143899121',
        to='+962785056637'
    )
    print(message.status)


