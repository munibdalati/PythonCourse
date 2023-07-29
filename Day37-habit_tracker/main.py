from datetime import datetime, timedelta
import requests
import random

USERNAME = "munibaldalati"
TOKEN = "thk3qj4hnef8438dbns3"
GRAPH = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": {GRAPH},
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

for day in range(180):
    today = (datetime.now()-timedelta(day)).strftime("%Y%m%d")
    qty = str(random.choice(range(60, 120, 10)))
    activity_end_point = f"{graph_endpoint}/{GRAPH}"
    activity_params = {
        "date": today,
        "quantity": qty
    }
    response = requests.post(url=pixel_creation_endpoint, json=activity_params, headers=headers)
    print(response.text)


# today = datetime(year=2023, month=2, day=6)
# pixel_data = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "15",
# }

#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#
# print(response.text)


# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "4",
# }

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
