from ast import Try
import urllib.request
import re
from config import ytCharacters
import getRandomNumber

def getNumber(start,stop):
    return getRandomNumber.getRandom(start,stop)



def getComedyURL(randomNumber):
    try: 
        videoURL="https://www.youtube.com/watch?v={}".format(ytCharacters[randomNumber])
        #url=urllib.request.urlopen('https://www.youtube.com/results?search_query=comedy+clips')
        #video_ids=re.findall(r"watch\?v=(\S{11})",url.read().decode())
    except:
        videoURL="https://youtu.be/F71xQC6SJgE"
    return videoURL


def getComedyLinkMain():
    randomNumber=getNumber(0,61)
    return getComedyURL(randomNumber)
   


