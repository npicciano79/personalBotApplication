#convert from military to standard
    #get current hour

def timeConversion(time,code):
    if code==1:
        n_hour=int(time.split(":")[0])
        minute=str(time.split(':')[1])

        setting="PM"
        if n_hour<12:
            setting='AM'
            message='morning'
        elif n_hour==12:
            message='afternoon'
        else:
            n_hour-=12
            if n_hour<3:
                message='afternoon'
            else:
                message='evening'
    currentTimeFormat='{}:{} {}'.format(str(n_hour),minute,setting)
    return currentTimeFormat,message
  
       