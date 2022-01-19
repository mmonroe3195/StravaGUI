#lines 2-25 borrowed from franchyze923 (https://github.com/franchyze923/Code_From_Tutorials/blob/master/Strava_Api/strava_api.py)
import requests
import urllib3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "76571",
    'client_secret': '0f94a401bc48a0309db35e1bfcabf48e8638b416',
    'refresh_token': '5fee084a3a6f508226832571c6a0a6fdcbd63278',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

stravaposts = pd.json_normalize(my_dataset)
cols = ['name', 'type', 'distance', 'moving_time',
         'average_speed', 'max_speed','total_elevation_gain',
         'start_date_local', 'average_cadence', 'average_heartrate',
       ]
stravaposts = stravaposts[cols]

stravaposts.groupby(['type']).sum().plot(kind='pie', y='distance', autopct='%1.0f%%')
#plt.show() #shows the pie chart

total_dist = total_bike_dist = total_run_dist = 0
total_walk_dist = total_kayak_dist = total_hike_dist = total_swim_dist= 0


for i in range(len(stravaposts['distance'])):
    total_dist += stravaposts.at[i,'distance']

    if stravaposts.at[i,'type'] == 'Ride':
        total_bike_dist += stravaposts.at[i,'distance']

    elif stravaposts.at[i,'type'] == 'Run':
        total_run_dist += stravaposts.at[i,'distance']

    elif stravaposts.at[i,'type'] == 'Walk':
        total_walk_dist += stravaposts.at[i,'distance']

    elif stravaposts.at[i,'type'] == 'Hike':
        total_hike_dist += stravaposts.at[i,'distance']

    elif stravaposts.at[i,'type'] == 'Kayaking':
        total_kayak_dist += stravaposts.at[i,'distance']

    elif stravaposts.at[i,'type'] == 'Swim':
        total_swim_dist += stravaposts.at[i,'distance']

total_dist /= 1609.344 #converting meters to miles
total_run_dist /= 1609.344
total_bike_dist /= 1609.344
total_walk_dist /= 1609.344
total_hike_dist /= 1609.344
total_kayak_dist /= 1609.344
total_swim_dist /= 1609.344

print(f'You traveled a total distance of {round(total_dist, 2)} miles with Strava.\n')
print(f'You biked a total distance of {round(total_bike_dist, 2)} miles.\n')
print(f'You ran a total distance of {round(total_run_dist, 2)} miles.\n')
print(f'You walked a total distance of {round(total_walk_dist, 2)} miles.\n')
print(f'You swam a total distance of {round(total_swim_dist, 2)} miles.\n')
print(f'You kayaked a total distance of {round(total_kayak_dist, 2)} miles.\n')
print(f'You hiked a total distance of {round(total_hike_dist, 2)} miles.\n')

distancedf = pd.DataFrame({'Activity':['Run', 'Bike', 'Hike', 'Swim', 'Walk', 'Kayak'], 'Distance (miles)':[total_run_dist, total_bike_dist, total_hike_dist, total_swim_dist, total_walk_dist, total_kayak_dist]})


display(distancedf)
ax = distancedf.plot.bar(x = 'Activity', y = 'Distance (miles)', rot=0)
plt.show();
