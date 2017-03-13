import requests
import os
import numpy as np
import pandas as pd
import time


# Category IDs: 4, 6, 13
def getData(categoryID):
    headers = "Accept: application/json"
    baseURL = "https://www.predictit.org/api/marketdata/category/"

    url = baseURL + str(categoryID)
    response = requests.get(url, headers)


    data = response.json()

    data3 = np.asarray(data["Markets"])
    return data3


def cleanData(data):
    a = data[0]["TimeStamp"]
    print(a)

def saveData(data,marketID):
    df = pd.DataFrame(data)
    time = data[0]["TimeStamp"]

    fixed = time.replace(":", ".")
    fixed2 = fixed.replace(".", "-")

    fileName = "%s%s%s%s.txt" % ("MarketID-", marketID, "-", fixed2)
    out = os.path.join("data", fileName)
    print(out)

    df.to_csv(out)

def scrapeData():
    d1 = getData(4)
    d2 = getData(6)
    d3 = getData(13)

    saveData(d1,"4")
    saveData(d2, "6")
    saveData(d3, "13")


if __name__ == "__main__":
    while(True):
        scrapeData()
        time.sleep(60)
