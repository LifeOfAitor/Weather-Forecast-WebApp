import pandas as pd
import requests

# read api key file
with open("api.txt") as file:
    api_key = file.read()


# function to get only necessary data from api call
def get_data(place, days):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?q="
           f"{place}&appid={api_key}&units=metric")
    response = requests.get(url)
    data = response.json()
    # create a list to format api data
    filtered_data = data["list"]
    # separate data by days and return that data
    if days < 5:
        prompt_day = filtered_data[0]["dt_txt"].split(" ")[0]
        for i in range(len(filtered_data)):
            while filtered_data[i]["dt_txt"].split(" ")[0] == prompt_day:
                i += 1
            filtered_data = filtered_data[:i + ((days - 1) * 8)]
            break
        return filtered_data
    else:
        return filtered_data


# process and clean the filtered data
def get_dates_temp_cond(filtered_data):
    # create all necessary lists
    date_list = []
    temperature = []
    condition = []
    # append info on each list
    for i in range(len(filtered_data)):
        date_list.append(filtered_data[i]["dt_txt"])
        temperature.append(filtered_data[i]["main"]["temp"])
        condition.append(filtered_data[i]["weather"][0]["main"].title())
    return date_list, temperature, condition


if __name__ == "__main__":
    data = get_data("Irun", 2)
    date, temp, condition = get_dates_temp_cond(data)
    print(date, temp, condition)
