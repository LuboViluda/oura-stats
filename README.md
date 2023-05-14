# Oura stats
- handy to examinate impact of self experiment on sleet

## What is doing
- script to get daily sleep stats from API and compute weekly average of values "light_sleep_duration", "rem_sleep_duration, "average_hrv"
and "average_heart_rate"
- compute long term average (base line)
- compute diff of each week against baseline 
- save computed values as csv. and json values for next processing/visualization  
- build human readble markdown (week averages, long term average, diff between long term average and each week)

## How to use
- generate oura API key
- set the key as env var `OURA_API_KEY` 
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
- markdown
```
# Your sleep data    

## Average week values
week|week-start|deep_sleep|light_sleep|rem_sleep|average_hrv|average_heart_rate
---|---|---|---|---|---|---
1|2023-01-02|42|42|42|42|42

## Long term average (base line)
week|week-start|deep_sleep|light_sleep|rem_sleep|average_hrv|average_heart_rate
---|---|---|---|---|---|---
baseline|avg|42|42|42|42|42

    
## Differences against baseline data
week|week-start|deep_sleep_diff|light_sleep_diff|rem_sleep_diff|average_hrv_diff|average_heart_rate_diff
---|---|---|---|---|---|---
1|2023-01-02|0|0|0|0|0
```

## Next work/Todos
- add integration test
- slip to methods
- use only float internally
- add option to select arbitrary baseline (x weeks)
- mark in markdown by color if some values are above or below certain threshold