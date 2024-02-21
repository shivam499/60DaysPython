import requests

apiKey = "05e3aec398c0f2e706325828ef1a4e98"


def get_data(place, forecast_days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={apiKey}"
    response = requests.get(url)
    content = response.json()
    filtered_data = content["list"]
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Lucknow", forecast_days=3))
