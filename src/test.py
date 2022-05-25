#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 09:04:50 2022

@author: harison
"""

import requests
import json
import pandas as pd
import os.path
import time
import datetime
import csv

flag = True

while(flag):
    if(os.path.isfile('file.csv')):
        data = requests.get(
        f"https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m"
        )
        webContent = json.loads(data.content)
        df = pd.DataFrame(webContent)
        dfExist = pd.read_csv('file.csv')
        dfConcat = pd.concat([dfExist, df])
        print(dfConcat)
        flag = False
    else:
        with open('file.csv', 'w') as csvfile:
           print("Creating csv file")
           flag = False
           
                  