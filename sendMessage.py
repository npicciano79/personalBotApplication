import requests

while True:
    whom='#'
    message='test message'

    resp=requests.post("https://textbelt.com/text",{
        'phone':{}.format(whom),
        'message':{}.format(message),
        'key':'textbelt',
    })

print(resp.json())

