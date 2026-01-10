import requests
from datetime import datetime
import time
My_LAT = 17.385044
MY_LONG = 78.486671

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"ISS latitude :{iss_latitude}")
    print(f"ISS longitude :{iss_longitude}")

    if My_LAT-5 <= iss_latitude <= My_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        print("@ISS is above you")
        return True
    else:
        print("@ISS is not above you")
        return False

def is_night():
    #print("Checking if it is night")
    parameters = {
    "lat": My_LAT,
    "lng": MY_LONG,
    "tzid": "Asia/Kolkata",
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

    #print(sunrise)
    print(f"sunrise hr :{sunrise_hr}")
    #print(f"sunrise min :{sunrise_min}")
    #print(sunset)
    print(f"sunset hr :{sunset_hr}")
    #print(f"sunset min :{sunset_min}")
    time_now = datetime.now()
    print(f"curr hr :{time_now.hour}")
    if time_now.hour >= sunset_hr or time_now.hour <= sunrise_hr:
        print("@It is night")
        return True
    else:
        print("@It is day")
        return False


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        print("ISS is above you and it is night....")
        # Can send notification in mail here..
    else:
        print("ISS is not above you or it is not night....")

#time_now = datetime.now()
#print(time_now)
#y = is_night()
#print(y)

