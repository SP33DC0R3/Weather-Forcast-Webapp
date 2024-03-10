import requests

api_key = "3e3bbd8a6c780941f0435a929e4bfedf"


def get_data(place, forecast_days=None, type_data=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    result = requests.get(url)
    data = result.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    if type_data == "Temperature":
        filtered_data = [i["main"]["temp"] for i in filtered_data]
    if type_data == "Sky":
        filtered_data = [i["weather"][0]["main"] for i in filtered_data]
    return filtered_data


if __name__=="__main__":
    print(get_data("Faisalabad", 4, "Temperature"))