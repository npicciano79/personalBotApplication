#gets daily news briefing 
import requests
from config import newsAPIKey,newsAPIURL
import configparser
import json 


def create_session():
    s=requests.Session()
    s.headers.update({
        'newAPIKey':newsAPIKey,
        'content-type':'application/jSON'
    })

    return s

def main():
    newsTitleURLDict={}
    sess=create_session()
    resp=sess.get("https://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(newsAPIKey))
    resp=resp.text
    news=json.loads(resp)
    for count in range(0,2):
        #newsTitle.append(news['articles'][count]['title'])
        #newsURL.append(news['articles'][count]['url'])
        newsTitleURLDict[news['articles'][count]['title']]=news['articles'][count]['url']
    

    #print(newsTitleURLDict)        
    return newsTitleURLDict

#if __name__=="__main__":
#    main()
        

