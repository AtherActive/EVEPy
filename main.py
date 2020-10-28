# Created by IAmSalt Salty with help of the EVEMarketer-API.

import json as js
import requests as rq
import structures as str
import settings


def UpdateMarketValues(data):
    # create structure for storage purposes
    dataStruct = str.MarketItem

    # sets all values.....
    dataStruct.buyValues.avgPrice = data[0]['buy']['avg']
    dataStruct.buyValues.volume = data[0]['buy']['volume']
    dataStruct.buyValues.maxPrice = data[0]['buy']['max']
    dataStruct.buyValues.minPrice = data[0]['buy']['min']

    dataStruct.sellValues.avgPrice = data[0]['sell']['avg']
    dataStruct.sellValues.volume = data[0]['sell']['volume']
    dataStruct.sellValues.maxPrice = data[0]['sell']['max']
    dataStruct.sellValues.minPrice = data[0]['sell']['min']
    return dataStruct

# does what it says. Takes the data form the API.
def PullDataFromAPI(id):

    url = 'https://api.evemarketer.com/ec/marketstat/json?typeid={}'.format(id)
    data = rq.get(url)
    jsData =  data.json()

    if settings.developerMode == 1:
        str.PrintS("Received from {}: ".format(url), jsData)


    itemStruct = UpdateMarketValues(jsData)

    return itemStruct
