import config
import os
from twilio.rest import Client 

def sendMessage(dataArrFormatted,weatherImageLink):
    fullMessage='\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}\n\n{}.'.format(dataArrFormatted[0],dataArrFormatted[1],dataArrFormatted[2],dataArrFormatted[3],dataArrFormatted[4],dataArrFormatted[5],dataArrFormatted[6])

    #account_sid=os.getenv('account_sid')
    #auth_token=os.getenv('auth_token')
    

    #https://github.com/npicciano79/personalBot/blob/main/icons/brokencloud.png
    #send message via twilio
    try: 
        client=Client(config.account_sid,config.auth_token)
        message=client.messages.create(
        body=fullMessage,
        #from_=os.getenv('twilio_number'),
        #to=os.getenv('target_number')
        media_url=[weatherImageLink],
        from_=config.twilio_number,
        to=config.target_number
        )
        return 'success {}'.format(message.body)
    except Exception as e: 
        return 'Error sending Twilio text {}'.format(e)

def sendMain(dataArrFormatted,weatherImageLink):
    return sendMessage(dataArrFormatted,weatherImageLink)

