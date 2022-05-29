#lines 9-27 borrowed from franchyze923 (https://github.com/franchyze923/Code_From_Tutorials/blob/master/Strava_Api/strava_api.py)
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

i = 1
dataset = []

#can only get 200 results max at a time.
#must loop through to check if there are multiple pages of data
while True:
    param = {'per_page': 200, 'page': i}
    currdataset = requests.get(activites_url, headers=header, params=param).json()

    if not currdataset:
        break

    else:
        dataset += currdataset
        i += 1

stravaposts = pd.json_normalize(dataset)
cols = ['name', 'type', 'distance', 'moving_time',
         'average_speed', 'max_speed','total_elevation_gain',
         'start_date_local', 'average_cadence', 'average_heartrate',
       ]
stravaposts = stravaposts[cols]
years = []
months = []
for i in range(len(stravaposts['start_date_local'])):
    years.append(stravaposts.at[i,'start_date_local'][:4])
    months.append(stravaposts.at[i,'start_date_local'][5:7])

stravaposts.insert(8, "year", years, True)
stravaposts.insert(9, "month", months, True)

#getting the years of activities and activitytypes
years = [stravaposts.at[0, 'year']]
activitytypes = [stravaposts.at[0, 'type']]
for i in range(len(stravaposts['year'])):
    #adds a new year if the year hasn't been recorded yet
    if stravaposts.at[i,'year'] != years[-1]:
        years.append(stravaposts.at[i,'year'])

    #adds a new type if the activity time has not been recorded yet
    if stravaposts.at[i, 'type'] not in activitytypes:
       activitytypes.append(stravaposts.at[i,'type'])

#stravaposts[stravaposts.type != 'Ride'].groupby(['type']).sum().plot(kind='pie', y='distance', autopct='%1.0f%%')
#plt.show() #shows the pie chart
