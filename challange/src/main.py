import requests
import json
import time
import datetime
import pandas as pd

'''
fonte:
https://stackoverflow.com/questions/43983622/remove-unnamed-columns-in-pandas-dataframe
referencia ex:
 dfConcat.drop(dfConcat.columns[dfConcat.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
'''
flag = True
path = False
webContent = 0
counter = 29


def getUnixTimeStamp(day_ago=0):
    millisecond = datetime.datetime.now()-datetime.timedelta(days=day_ago)
    timeStamp = int(time. mktime(millisecond. timetuple()) * 1000)
    return timeStamp


def feedDatabase(init, final):
    data = requests.get(
        f"https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m&endTime={final}&startTime={init}"
    )
    webContent = json.loads(data.content)
    webContent = [{"longShortRatio": content["longShortRatio"],
                   "timestamp":content["timestamp"], "symbol":content["symbol"]} for content in webContent]
    webContent = pd.DataFrame(webContent)
    localContent = pd.read_csv('./challange/src/data/file.csv')
    try:
        dfConcat = pd.concat([localContent.set_index(
            'timestamp'), webContent.set_index('timestamp')])
        dfConcat.drop(dfConcat.columns[dfConcat.columns.str.contains(
            'unnamed', case=False)], axis=1, inplace=True)

        dfConcat.to_csv('./challange/src/data/file.csv')
    except:
        print('------warning------')
        print(webContent)
        print("Nenhum conteúdo referente ao range do timestamp:")
        print("início: ", init, " fim: ", final)


while flag:
    init = getUnixTimeStamp(counter)
    final = getUnixTimeStamp(counter-1)

    if counter <= 1:
        flag = False

    if path != False:
        feedDatabase(init, final)
    else:
        ''''''
        data = requests.get(
            f"https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol=BTCUSDT&period=5m&endTime={final}&startTime={init}"
        )
        webContent = json.loads(data.content)
        webContent = [{"longShortRatio": content["longShortRatio"],
                       "timestamp":content["timestamp"], "symbol":content["symbol"]} for content in webContent]
        webContent = pd.DataFrame(webContent)
        webContent.to_csv('./challange/src/data/file.csv')
        path = "./challange/src/data/file.csv"
    counter -= 1
