import csv
import requests
import json
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pandas as pd


def build_stats():
    url = 'https://api.ouraring.com/v2/usercollection/sleep'
    params = {
        'start_date': '2023-01-02',
        'end_date': '2023-04-29'
    }
    headers = {
        'Authorization': 'Bearer {oura-auth-token}'
    }
    response = requests.request('GET', url, headers=headers, params=params)

    json_response = json.loads(response.text)
    days = json_response["data"]

    dicts = []
    for day in days:
        d = create_dict_for_day(day["day"],
                                day["deep_sleep_duration"],
                                day["light_sleep_duration"],
                                day["rem_sleep_duration"],
                                day["average_hrv"],
                                day["average_heart_rate"])
        dicts.append(d)

    json_str = json.dumps(dicts)

    # save the JSON string to a file
    with open("daily.json", "w") as f:
        f.write(json_str)

    with open("daily.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["day", "deep_sleep", "light_sleep", "rem_sleep", "average_hrv",
                                               "average_heart_rate"])
        writer.writeheader()
        for d in dicts:
            writer.writerow(d)

    # compute weekly averages
    week_dict = {}
    for d in dicts:
        day = datetime.strptime(d["day"], "%Y-%m-%d")
        week = (day - timedelta(days=day.weekday())).strftime("%Y-%m-%d")
        if week not in week_dict:
            week_dict[week] = {"deep_sleep": [], "light_sleep": [], "rem_sleep": [], "average_hrv": [],
                               "average_heart_rate": []}
        week_dict[week]["deep_sleep"].append(d["deep_sleep"])
        week_dict[week]["light_sleep"].append(d["light_sleep"])
        week_dict[week]["rem_sleep"].append(d["rem_sleep"])

        if d["average_hrv"] is not None:
            week_dict[week]["average_hrv"].append(d["average_hrv"])

        if d["average_hrv"] is not None:
            week_dict[week]["average_heart_rate"].append(d["average_heart_rate"])

    weekly_averages = []
    count = 1
    for week, data in week_dict.items():
        weekly_averages.append({
            "week": count,
            "week-start": week,
            "deep_sleep": "{:.2f}".format(sum(data["deep_sleep"]) / len(data["deep_sleep"])),
            "light_sleep": "{:.2f}".format(sum(data["light_sleep"]) / len(data["light_sleep"])),
            "rem_sleep": "{:.2f}".format(sum(data["rem_sleep"]) / len(data["rem_sleep"])),
            "average_hrv": "{:.2f}".format(sum(data["average_hrv"]) / len(data["average_hrv"])),
            "average_heart_rate": "{:.2f}".format(sum(data["average_heart_rate"]) / len(data["average_heart_rate"]))
        })
        count = count + 1

    # save the weekly averages as a JSON file
    weekly_averages_json = json.dumps(weekly_averages)
    with open("weekly_averages.json", "w") as f:
        f.write(weekly_averages_json)

    # save the weekly averages as a CSV file
    with open("weekly_averages.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["week", "week-start", "deep_sleep", "light_sleep", "rem_sleep",
                                               "average_hrv",
                                               "average_heart_rate"])
        writer.writeheader()
        for d in weekly_averages:
            writer.writerow(d)

    df = pd.read_csv('weekly_averages.csv')

    # Select column to plot
    x = df['deep_sleep']
    x1 = range(len(x))
    print(x1)

    # Plot data
    plt.plot(x1, x)

    # Add title and labels
    plt.title('Plot Title')
    plt.xlabel('week')
    plt.ylabel('deep sleep')

    # Show plot
    plt.show()


def create_dict_for_day(day, deep_sleep_duration, light_sleep_duration, rem_sleep_duration, average_hrv,
                        average_heart_rate):
    return {
        "day": day,
        "deep_sleep": seconds_to_minutes(deep_sleep_duration),
        "light_sleep": seconds_to_minutes(light_sleep_duration),
        "rem_sleep": seconds_to_minutes(rem_sleep_duration),
        "average_hrv": average_hrv,
        "average_heart_rate": average_heart_rate
    }


def seconds_to_minutes(duration_seconds: int) -> int:
    minutes = duration_seconds // 60
    return minutes


if __name__ == '__main__':
    build_stats()
