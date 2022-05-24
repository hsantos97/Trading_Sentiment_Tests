#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 23 19:29:01 2022

@author: harison
"""

import requests
import json
import pandas as pd
import os.path
import time
import datetime

previousDay = datetime.datetime.today() - datetime.timedelta(days=30)
print(time.mktime(previousDay.timetuple()) * 1000)

'''def processor():
  flag = True
  while flag:
      if(os.path.isfile('file.csv')):
          
          test = pd.read_csv('file.csv')
          data = requests.get(
        f"https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m"
        )
          webContent = json.loads(data.content)
          df = pd.DataFrame(webContent)
          #print(df)
          dfConcat = pd.concat([test,df])
          dfConcat.to_csv('file.csv')
          time.sleep(1)
          if len(test.index) < 100:
              flag = False
      else:          
          data = requests.get(
            f"https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m"
            )
          webContent = json.loads(data.content)
          df = pd.DataFrame(webContent)
          #print(df)
          df.to_csv('file.csv')
          time.sleep(1)


processor()'''



  