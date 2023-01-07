#import local packages
import weatherMain,quoteMain,comedyMain,getDate, historyMain,getMainFormat,googleMain,messageSend,news

import sys




def main():
   
   #get current date time message
   print('Getting date,time')
   currentDateTime,date=getDate.getCurrent()
   
   #API call that access openweather API 
   #retrieves description, current, max, min temps, humidity
   print('getting weather forecast')
   weatherMainFormated=weatherMain.getweatherMain()
   weatherImageLink=weatherMainFormated[1]

   print('getting news')
   newsDict=news.main()
   #print(newsDict)

   #scraper that accesses motivational quote
   print('getting motivational quote')
   motivationQuote=quoteMain.getQuoteMain()
   
   #get comedy video URL
   print('getting comedy video')
   comedyVideoURL=comedyMain.getComedyLinkMain()

   #get day in history fact
   print('getting history fact')
   historyFact=historyMain.getHistoryMain()

   #get Google calendar data
   print('getting google calendar')
   event_dict,eventCount=googleMain.getGoogleMain()
   #print(event_dict,eventCount)

   dataArr=[date,currentDateTime,weatherMainFormated,newsDict,motivationQuote,comedyVideoURL,historyFact,event_dict,eventCount]
   #format data and message into readable form
   print('formatting and sending data')
   dataArrFormatted=getMainFormat.dataFormat(dataArr)
   #print(dataArrFormatted)
   print(weatherImageLink)
   confirmation=messageSend.sendMain(dataArrFormatted,weatherImageLink)
   print(confirmation)
   #print test

   





if __name__=="__main__":
   #print(sys.path)
   main()
   

