import requests
import datetime
import os

GENDER = "male"
WEIGHT_KG = "75"
HEIGHT_CM = "177"
AGE = "26"


API_ID = os.environ["API_ID"]
API_KEY = os.environ.get("API_KEY")
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
TOKEN = os.environ.get("TOKEN")


# API_ID="17aaef1d"
# API_KEY="3fc9f7654cd9e647b28d223d1131ba6f"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(response.text)
#
#
# SHEET_ENDPOINT = "https://api.sheety.co/6bf453063a19e55020c2d8323cfad58c/workoutTracking/sheet1"

today = datetime.datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")

bearer_headers = {
"Authorization": TOKEN
}


for exercise in result['exercises']:
    data = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
    # response1 = requests.post(url=SHEET_ENDPOINT, json=data, auth=(USERNAME, PASSWORD))
    response1 = requests.post(url=SHEET_ENDPOINT, json=data, headers=bearer_headers)
    print("response.status_code =", response1.status_code)
    print("response.text =", response1.text)


