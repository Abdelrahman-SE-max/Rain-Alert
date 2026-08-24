import os
import requests
import smtplib

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.environ.get("OWM_API_KEY")

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

weather_params = {
    "appid": api_key,
    "lat": 29.9611,
    "lon": 30.9296,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject: Rain Alert\n\nIt's going to rain today. Remember to bring an umbrella."
        )
