import requests
from datetime import datetime


My_LAT = 17.385044
MY_LONG = 78.486671
parameters = {
    "lat": My_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise= (data["results"]["sunrise"])
sunset = (data["results"]["sunset"])
sunrise_hr = int((sunrise.split("T")[1].split(":")[0]))
sunrise_min = int((sunrise.split("T")[1].split(":")[1]))
sunset_hr = int((sunset.split("T")[1].split(":")[0]))
sunset_min = int((sunset.split("T")[1].split(":")[1]))
print(sunrise)
print(sunrise_hr)
print(sunrise_min)
print(sunset)
print(sunset_hr)
print(sunset_min)


time_now = datetime.now()
print(time_now)

