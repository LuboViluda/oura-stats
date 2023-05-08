# Oura stats

- script to get daily sleep stats from API and compute weekly average of values "light_sleep_duration", "rem_sleep_duration, "average_hrv"
and "average_heart_rate"
- compute averages for selected base line weeks
- compute diff of each week against baseline weeks
- save computed values as csv. and json values for next processing/visualization  
- handy to examinate impact of self experiment on sleet  

## How to use
- generate oura API key
- fill key in the script
- run the script

## Output data example
- csv
```
week,week-start,deep_sleep,light_sleep,rem_sleep,average_hrv,average_heart_rate
1,2023-01-02,42,42,42,42,42
```
- json
```json
  {
    "week": 1,
    "week-start": "2023-01-02",
    "deep_sleep": "42",
    "light_sleep": "42",
    "rem_sleep": "42",
    "average_hrv": "42",
    "average_heart_rate": "42"
  },
```