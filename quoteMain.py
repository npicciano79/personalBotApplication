
from bs4 import BeautifulSoup
import csv
import requests
import re
from config import quoteURL
import getRandomNumber



def getQuote(quoteURL):
    try:
        page=requests.get(quoteURL)

        #call random number function
        randomNumber=getRandomNumber.getRandom(1,67)
    
        pageData=BeautifulSoup(page.text,'html.parser')
        quotePart=pageData.find('div',id='pos_1_'+str(randomNumber))
        dailyQuote=quotePart.find('div',style="display: flex;justify-content: space-between").text 
    except Exception as e:
        dailyQuote='Me fail english, that\'s unpossible' 



    return dailyQuote




def getQuoteMain():
    motivationalQuote=getQuote(quoteURL)
    return motivationalQuote