import requests
from twilio.rest import Client


# Using open weahter's weather API

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "2b97093ae7d892795952740476ce1d86"

# Twilio's

account_sid = "AC7861562d3c2f4fd45400d4a6bfff9a4a"
auth_token =  "7e7b1bc230c675ef45362e4899e9b76d"

# lat, lon set to San Francisco based on https://www.latlong.net/
# current, minutely weather data have been excluded.

weather_params = {
    "lat": 37.789072,
    "lon": -122.401452,
    "appid": api_key,
    "exclude": "current,minutely",
    "units": "metric"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# next 18 hours' weather data 
weather_slice = weather_data["hourly"][:18]
# next 18 hours' tempature of the weather data

will_warm = False

for hour_data in weather_slice:
    temperature = hour_data["temp"]
    if int(temperature) > 20:
        will_warm = True

if will_warm:
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="A high in the next 18 hours in San Francisco is above 20 Celsius.",
                     from_='+18666291367',
                     to='+17372020401'
                 )
    print(message.status)
    

else:
    print("Please dress warm. A high in the next 18 hours in San Francisco is below 20 Celsius.")
 

