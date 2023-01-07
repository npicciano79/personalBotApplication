from urllib import request
from bs4 import BeautifulSoup
import requests
import config
from config import api_key,lat,lon
import json
import csv


def getForecast():
    #weather API call
    try:
        PARAMS={'latitude':lat,'longitude':lon,'key':api_key}
        url="https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}".format(config.lat,config.lon,config.api_key)
        #url="https://api.openweathermap.org/data/2.5/weather?"
        raw=requests.get(url)
    except Exception as e:
        print(e)
        #with open('errorCatch.csv','w',newline='')as f:
        #    csvWrite=csv.writer(f)
        #    csvWrite.writerow(e) 
         
           
        
    raw=raw.text
    #parse data
    weatherData=[]
    rawData=json.loads(raw)
    #print(rawData)
    description=rawData['weather'][0]['description']
    currTemp=rawData['main']['temp']
    highTemp=rawData['main']['temp_max']
    lowTemp=rawData['main']['temp_min']
    humidity=rawData['main']['humidity']
    weatherImageLink=config.weatherImgDict[description]
    weatherData=[description,weatherImageLink,currTemp,highTemp,lowTemp,humidity]
    #print(weatherData)
    return weatherData
    
def formatDataDegree(weatherData):
    #convert to farehneight 
    #add degree sign to temp
    for i in range(2,5):
        tempVal=str(((weatherData[i]-273.15)*9)//5+32)
        tempVal=tempVal.split('.')[0]
        weatherData[i]=(f"{tempVal}\N{DEGREE SIGN}")
    
    return weatherData

    



def getweatherMain():
    weatherData=getForecast()
    weatherDataDegree=formatDataDegree(weatherData)

    return weatherDataDegree









