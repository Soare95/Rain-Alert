import request
from twilio.rest import Client


API_KEY = "WEATHER_API"
MY_LAT = "44.940399"
MY_LONG = "26.023821"
account_sid = "TWILIO_ACC"
auth_token = "TWILIO_TOKEN"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

data_12h = data["hourly"][:12]
for hour_data in data_12h:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today",
        from_="+17732506672",
        to="TO_PHONE_NUMBER"
    )
    print(message.status)
