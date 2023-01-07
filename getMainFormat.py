from config import weatherImgDict
from PIL import Image
from botMain import weatherMain
import requests
import config
import getRandomNumber


def formatGreeting(date,standardGreet):
    if date==config.startDate:
        #start day message
        greetingMessage='{} This is Benni, your personal Bot. I\'ll be sending you daily messages informing you of the weather, daily events, or providing you with entertaining videos.'.format(standardGreet)
    else:
        randomNumber=getRandomNumber.getRandom(0,4)
        greetingMessage='{} {}'.format(config.greetMessageGroup[randomNumber],standardGreet)
    
    return greetingMessage




def formatWeather(weatherData):
    print(weatherData)
    weatherMessage='The forecast for today includes {}. The average temperature will be {}, with a high of {} and low of {}.'.format(weatherData[0],weatherData[2],weatherData[3],weatherData[4])
    print(weatherMessage)

    """
    weatherImgDict={'clear sky':'sunny.png','broken clouds':'partalcloud.png','few clouds':'partialcloud.png','scattered clouds':'partialcloud.png','broken clouds':'brokencloud.png','shower rain':'rain.png','rain':'rain.png','thunderstorm':'thunderstorm.png'}
    try:
        imageLink=Image.open('../icons/{}'.format(weatherImgDict[weatherData[0]]))  
    except Exception as e:
        imageLink=Image.open('../icons/rain.png')  
    #print(weatherImgDict[weatherData[0]])
    
    imageLink.show()
    """
    
    
    return weatherMessage

def formatNews(news):
    newsString='Here are todays top news stories.  Select the link to read more:\n'
    for i in news.items():
        newsString+=str(i[0]+'\n')
        newsString+=str(i[1]+'\n')
    return newsString        




def formatMotivation(motivationQuote):
    return 'Here\'s a motivational quote to start your day: {}.'.format(motivationQuote)

def formatComedy(comedyURL):
    return 'Here\'s a funny video from YouTube you might like. {}'.format(comedyURL)

def formatHistory(historyEvent):
    discription=historyEvent['text']
    link=historyEvent['link']
    #print(discription)
    #print(link)
    return 'Today\'s event in history: {}. You can learn more about this by clicking the link: {}.'.format(discription,link)

def formatGoogle(event_dict,eventCounter):
    eventString=''
    if eventCounter==0:
        eventMessage='You have no events on your P####### Gmail calendar for today.'
    else:
        eventMessage='You have {} events on your P######## Gmail calendar today.'.format(eventCounter)
        for event,time in event_dict.items():
            eventString+=('\n{} at {}'.format(event,time))
    
    return eventMessage+"\n"+eventString
    
    

#sendMessage Function moved to separate messageSend.py file
def sendMessage(greetingMessage,googleMessage,weatherMessage,motivationMessage,comedyMessage,historyMessage):
    fullMessage='\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}.'.format(greetingMessage,googleMessage,weatherMessage,motivationMessage,comedyMessage,historyMessage)

    #https://github.com/npicciano79/personalBot/blob/main/icons/brokencloud.png
    #send message via twilio
    client=Client(config.account_sid,config.auth_token)

    message=client.messages.create(
        body=fullMessage,
        from_=config.twilio_number,
        to=config.target_number
    )
    print(message.body)
    
    
def dataFormat(dataArr):
    greetingMessage=formatGreeting(dataArr[0],dataArr[1])
    print(greetingMessage)
    #sends weather message include high,low,forecast
    weatherMessage=formatWeather(dataArr[2])
    print(weatherMessage)
    newsFormated=formatNews(dataArr[3])
    print(newsFormated)
    motivationMessage=formatMotivation(dataArr[4])
    comedyMessage=formatComedy(dataArr[5])
    print(comedyMessage)
    historyMessage=formatHistory(dataArr[6])
    print(historyMessage)
    googleMessage=formatGoogle(dataArr[7],dataArr[8])
    print(googleMessage)
    dataArrFormatted=[greetingMessage,weatherMessage,newsFormated,motivationMessage,comedyMessage,historyMessage,googleMessage]
    return dataArrFormatted
    #sendMessage(greetingMessage,googleMessage,weatherMessage,motivationMessage,comedyMessage,historyMessage)


