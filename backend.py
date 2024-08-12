import pandas as pd
import requests

with open("api.txt") as file:
    api_key = file.read()


def get_data(place, days, info_type):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?q="
           f"{place}&appid={api_key}&units=metric")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    if days < 5:
        prompt_day = filtered_data[0]["dt_txt"].split(" ")[0]
        for i in range(len(filtered_data)):
            while filtered_data[i]["dt_txt"].split(" ")[0] == prompt_day:
                i += 1
            filtered_data = filtered_data[:i+((days-1)*8)]
            break
        return filtered_data
    else:
        return filtered_data



if __name__ == "__main__":
    print(get_data("Tokyo", 4, "temperature"))
