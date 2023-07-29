import requests
API_KEY ="5dVXi99QiYV950PalNNpamuJ0icJPKMk"


# class FlightData:
    #This class is responsible for structuring the flight data.
search_point = "api.tequila.kiwi.com//v2/search"
headers = {
    "apikey": API_KEY
}
query = {
    "fly_from": "FRA",
    "date_from": "13/02/2023",
    "date_to": "13/03/2023",
}
response = requests.get(url=search_point, headers=headers, params=query)
results = response.json()
print(results)

