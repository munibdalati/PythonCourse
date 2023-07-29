import requests
Affil_ID = "munibaldalatiflightsearch"
API_KEY ="5dVXi99QiYV950PalNNpamuJ0icJPKMk"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_point = "https://tequila-api.kiwi.com/locations/query"
        headers = {
            "apikey": API_KEY
        }
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=location_point, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["id"]
        return code


    #

    #
    # exercise_endpoint = "api.tequila.kiwi.com/"
    #
    # parameters = {
    #     "booking_token": "",
    #     "fly_from": "",
    #     "fly_to": "",
    #     "date_from": "",
    #     "date_to": ""
    #
    # }
    #
    # headers = {
    #     "apikey": API_KEY
    #     "Content_Type": "application / json"
    # }

