
<h1>Personal Bot Program</h1>
<h2>Application sends a daily text to user</h2>
<br>
<div id='intropara'>
  Personal bot program is written in Python. The application utilzes Beautiful Soup to scrape daily news events, today in history events, as well as motvational quotes from news, history, and quotes websites. Beautiful soup is also used to scrape links to random Youtube comedy videos.  Google Calendar API and OpenWeather API's are called returning an array of daily calendar events and times and an array consisting of the daily forecast, maximum, minimum, and average temperature.  
  
  Functions within the getMainFormat.py document, format the daily random greeting message, weather forecast, Google Calendar data, Youtube video links, daily news, motivational quote, and today in history event, and returns the data to send as an array.  The sendMessage function located within messageSend.py, calls the Twilio API and sends the formatted array message to the phone number on the config file.  
  
  </div>
  
  <h2>Techology used:</h2>
  The application was written in Python with VScode, utilizing Beautiful Soup and API calls using requests module.  
 
<h2>Application Output</h2>
<img src='https://user-images.githubusercontent.com/34743660/211169899-243ca509-6865-4f50-8697-112949041357.png'>
