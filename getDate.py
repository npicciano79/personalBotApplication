from timeConversion import timeConversion
from datetime import datetime


def timedate():
    #get current date and time
    now=datetime.now().strftime('%H:%M:%S %B,%dth')
    time,date=now.split()
    print(now)
    #get day_index and current day
    day_index=datetime.today().weekday()
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    currentDay=days[day_index]
    dateFormat='{}, {}'.format(currentDay,date)

    #convert from military to standard
    #get current hour
    """
    n_hour=int(time.split(":")[0])
    setting="PM"
    if n_hour<12:
        setting='AM'
        message='morning'
    else:
        n_hour-=12
        if n_hour<3:
            message='afternoon'
        else:
            message='evening'
    """
    currentTimeFormat,message=timeConversion(time,1)
    #print(currentTimeFormat,message)


    #get current minute 
    #minute=str(time.split(':')[1])
    #currentTimeFormat='{}:{} {}'.format(str(n_hour),minute,setting)

    #set morning, afternoon, evening 
    



    #formate current day, date and time
    """
    sample message:Good morning, today is WEDNESDAY, October 19 and it is 5:50am. 
    """

    timedateFormat='Good {}, today is {} and the current time is {}.'.format(message,dateFormat,currentTimeFormat)

    return timedateFormat, date

def getCurrent():
    timedateFormat,date=timedate()
    #print(timedateFormat)
    return timedateFormat,date


