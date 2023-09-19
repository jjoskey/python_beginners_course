import time
import requests
from requests.exceptions import RequestException

API_KEY = ""


def retry(func):
    def wrapper_retry(*args, **kwargs):
        retries = [5, 30]
        for seconds in retries:
            try:
                return func(*args, **kwargs)
            except RequestException:
                print(f'Failed to get data. Retrying in {seconds} seconds...')
                time.sleep(seconds)
        return func(*args, **kwargs)
    return wrapper_retry


@retry
def get_weather_by_hours_for_day_from_api(*, date: str, city: str) -> list[dict]:
    response = requests.get(
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}/{date}?unitGroup=us&key={API_KEY}")
    data = response.json()
    weather_by_days = data["days"]

    return weather_by_days[0]["hours"]


def get_dangerous_hours(*, weather_by_hour: list[dict]) -> list[dict]:
    dangerous_hours = []
    for weather in weather_by_hour:
        uvindex = weather["uvindex"]
        time = weather["datetime"]
        celsious_temperature = fahrenheit_to_celsius(weather["temp"])
        if uvindex >= 3:
            dangerous_hours.append({"time": time, "uvindex": uvindex, "temperature": celsious_temperature})
    return dangerous_hours


def fahrenheit_to_celsius(fahrenheit_temperature: float) -> int:
    return round((fahrenheit_temperature - 32) * 5 / 9)


date = "2023-08-04"
city = "London,UK"
day_weather = get_weather_by_hours_for_day_from_api(date=date, city=city)
dangerous_hours = get_dangerous_hours(weather_by_hour=day_weather)
print(dangerous_hours)
