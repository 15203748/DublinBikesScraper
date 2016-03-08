# Name:         John F Windsor
# Student ID:   15203748
# Date:         February 7th, 2016
# Project:      Software Engineering / Dublin Bikes
# API Key:      731c17d62f2813202e7be680d1447737c3ee0601

import requests
import time
from time import strftime
import json
import pandas as pd


NAME="Dublin" # name of contract
STATIONS="https://api.jcdecaux.com/vls/v1/stations" # and the JCDecaux endpoint
APIKEY = "731c17d62f2813202e7be680d1447737c3ee0601"

iCtr = 0

while (True):
    strCSV = (strftime("%Y%m%d-%H%M") + ".csv")
    iCtr += 1
    print(strCSV + ":  Rotation:  " + str(iCtr))
    try:
        r = requests.get(STATIONS, params={"apiKey": APIKEY, "contract": NAME})
        json_data = json.loads(r.text)
        df = pd.read_json(r.text)
        df.to_csv(strCSV)
        time.sleep(300)
    except:
        print("Error...")
