from bs4 import BeautifulSoup
import requests
from config import historyURL


def dayinHistory():
    historyInfo={}
    page=requests.get(historyURL)

    pageData=BeautifulSoup(page.text,'html.parser')
    historyData=pageData.find('div',class_='card-body')
    historyInfo['text']=historyData.text
    historyInfo['link']=str(historyData.find('a')).split('href=')[1].split('>')[0].replace('"'," ")
    historyInfo['image']=str(pageData.find('div',class_='card-media position-relative').find('img')).split('src=')[1].split('/>')[0].replace('"'," ")

    return historyInfo





def getHistoryMain():
    return dayinHistory()