
import pyttsx3 as tts #pyttsx is Python text to speech module 
import pyaudio
import speech_recognition as sr
import datetime #To get date and time
import webbrowser
import pyjokes
import randfacts
import os #For OS files
import psutil #For CPU and system info
import wikipedia
import pyautogui #For GUI functions
import requests#To get requests from API
import json
import weathercom
import PyPDF2
import os.path
from selenium import webdriver
import wmi
import random
import pywhatkit as py
import time
import wolframalpha
import re

engine = tts.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio:str):
    engine.say(audio)
    print(audio)
    engine.runAndWait()




def errors():
    error = ['I couldn\'t understand what you were trying to tell me',
             'Sorry! Didn\'t get you.',
             'I lost track of what you were saying',
             'I am sorry! Can you please repeat what you said?',
             'Something went wrong! Please try again.',
             'Sorry?',
             ]
    speak(random.choice(error))
    





def myCommand(i:int =0):
     x=i
     if (x==5):
         speak('Sorry, but this is quite a lot of errors which i can\'t handle. Please try again later')
         return 'xyza'
     r = sr.Recognizer()
     with sr.Microphone() as source:
        recognized_text = ''
        r.pause_threshold = 0.5 #waits for a second before listening
        r.adjust_for_ambient_noise(source, duration = 0.5)  #then adjusts the energy threshold based on surrounding noise
        print('Listening...')
        text = r.listen(source)
        r.pause_threshold = 1
        
        try:
            print("Recognizing...")
            recognized_text = str(r.recognize_google(text))
            print("User said:", recognized_text)
        except Exception as e:
            errors()
            recognized_text = myCommand(x+1)
  
        return str(recognized_text)
        





def open(command):
    if "youtube" in command:
        speak("Opening Youtube")
        webbrowser.open(url="https://youtube.com")
    elif "spotify" in command:
        speak("Opening Spotify")
        webbrowser.open(url="https://open.spotify.com/?_ga=2.197659179.524608783.1618325836-531289674.1618028968")  
    elif "instagram"in command:
        speak("Opening Instagram")
        webbrowser.open(url="https://instagram.com")  
    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open(url="https://facebook.com")
    elif 'word' in command:
        speak('Opening word')
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Word 2010.lnk"#Add // in place of /
        os.startfile(path)
    elif 'excel' in command:
        speak('Opening Excel')
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Excel 2010.lnk"#Add // in place of /
        os.startfile(path)
    elif 'powerpoint' in command:
        speak('Opening Powerpoint')
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Powerpoint 2010.lnk"#Add // in place of /
        os.startfile(path)
    elif 'discord' in command:
        speak('Opening Discord')
        path = "C:\\Users\\Jilin Stephen Biju\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk"
        os.startfile(path)
    elif 'teams' in command:
        speak('Opening Teams')
        path = "C:\\Users\\Jilin Stephen Biju\\AppData\\Local\\Microsoft\\Teams"
        os.startfile(path)
    else:
        errors()
        return -1




def joke():
    j = pyjokes.get_joke('en','neutral')
    speak(j)


def fact():
    f = randfacts.getFact()
    speak(f)


def sys_info():
    speak('What do you want to know about your system?')
    text = myCommand()
    if "battery"and"percentage"in text:
        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        percent = str(battery.percent)
        plugged = "Plugged In" if plugged else "Not Plugged In"
        speak(percent+'% | '+plugged)
    elif "disk" and "storage" in text:
        usage=psutil.disk_usage("c:")
        usage2=psutil.virtual_memory()
        speak(f"Your disk is currently {usage.percent} percent used and virtual memory is {usage2.percent} percent used ")
    else:
        errors()
        return -1



def take(text):
    if "screenshot" in text:
        img = pyautogui.screenshot()
        speak("Done....")
        img.save('C:\\Users\\Jilin Stephen Biju\\Pictures\\Screenshots\\img.png')#Add img.png to file location
        img.open('C:\\Users\\Jilin Stephen Biju\\Pictures\\Screenshots\\img.png')
        
    elif "notes" in text:
        speak("What should I write sir ?")
        notes=myCommand() #notes has been saved from our speech
        file=open('notes.txt','w') #file writing
        curDate=datetime.datetime.now().strftime("%d:%B:%Y")#Gets date and time from system
        curDay=datetime.datetime.now().strftime("%A")
        file.write(curDay)
        file.write(curDate)
        file.write("\n")
        file.write(notes)
        speak("Done Taking notes")
    else:
        errors()
        return -1



def read(text):
    if "pdf" in text:
            speak("Sure, Please name the PDF file you want me to read")
            pdf=myCommand()
            if(pdf!="None" and os.path.exists(pdf+".pdf")):
                book=open(str(pdf+".pdf"),'rb')
                pdfReader = PyPDF2.PdfFileReader(book)
                pages = pdfReader.pages
                print(pages)
                num = pdfReader.numPages
                engine = tts.init('sapi5')
                print('playing....')
                for i in range(0,num):
                    page = pdfReader.getPage(i)
                    text=page.extractText()
                    engine.say(text)
                engine.runAndWait()
    elif "notes" in text:
            speak("Opening notes.....")
            file2=open('notes.txt','r')
            speak(file2.read())
    else:
        errors()
        return -1



def date_or_time(command):
    if "time" in command:
            curTime=datetime.datetime.now().strftime("%I :%M :%S %p")#For getting Time
            # %H-Hour
            # %M-mins
            # %I-Hour(12hr)
            speak(f"The time is {curTime}")
            print(f"The time is {curTime}")
            
        
        
    elif "date" in command:
            curDate=datetime.datetime.now().strftime("%d:%B:%Y")#Gets date and time from system
            curDay=datetime.datetime.now().strftime("%A")
            # %d=Date
            # %B=month
            # %Y=Year
            # %A-day
            speak(f"The date is {curDate} and day is {curDay}")
            print(f"The date is {curDate} and day is {curDay}")



class Wiki():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=r'D:\VIT_CLASS\WIN20-21\IIP\chromedriver.exe') #Chrome Driver saved place
        
    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')#xpath is short form of that inspect element
        search.send_keys(query)#sends query to wikipedia page
        enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')#xpath for search button
        enter.click()
        time.sleep(1)




def sleep():
    speak('For how many minutes should i sleep?')
    t = myCommand()
    t = re.findall('[0-9]+',t)
    t = ''.join(t)
    t = int(t) * 60
    speak('Going to sleep now')
    time.sleep(t)
    speak('I am wide awake now!')



def wiki():
            speak("Please name the topic")
            topic=myCommand()
            speak("Searching {} in wikipedia".format(topic))
            info=Wiki()
            info.get_info(topic)



class youtube():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path=r'D:\VIT_CLASS\WIN20-21\IIP\chromedriver.exe') #Chrome Driver saved place
        
    def play(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        xpath=' //*[@id="video-title"]/yt-formatted-string'
        video=self.driver.find_element_by_xpath(xpath)
        self.driver.maximize_window()
        video.click()
        time.sleep(2)



def playvid():
    speak("What do You want to play")
    title=myCommand()
    speak('playing {}'.format(title))
    bot=youtube()
    bot.play(title)



def weatherreport(city):
    weatherdetails=weathercom.getCityWeatherDetails(city)
    humidity=json.loads(weatherdetails)["vt1observation"]["humidity"]#Observation from json code
    temp=json.loads(weatherdetails)["vt1observation"]["temperature"]#Observation from json code
    phrase=json.loads(weatherdetails)["vt1observation"]["phrase"]#Observation from json code
    return humidity,temp,phrase



def weather():
    try:
        speak("Sure, please name the city")
        city= myCommand()
        humidity,temp,phrase=weatherreport(city)
        speak("Today's Weather :Currently in "+ city +" the temprature is "+str(temp)+" degree celcius,with humidity of "+str(humidity)+" percent and sky is "+phrase)
    except Exception as e:
        errors()
        weather()



def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Hello")
        
def news():
    api_address="https://newsapi.org/v2/top-headlines?country=in&apiKey=42b031c2a53343d899b837fb582108f1"#Enter ur API key
    response=requests.get(api_address)
    news_json=json.loads(response.text)#load as json
    count=10      #10 Headlines-No of Head lines I need 
    speak("Here are today's Top headlines")
    for news in news_json['articles']:
        if count>0:
            T=str(news['title'])#visit the api address entering the apikey to check json 
            speak(T)
            count-=1



def expressions():
    express = ['I am also fine',
               'Happy as usual',
               'Really excited',
               'Good',
               'I\'m great!'
               ]
    speak(random.choice(express))



def anything_else():
    statements = ['Anything else?',
                  'What else do you want me to do?',
                  'How else can I help you?',
                  'Is there anything else I can help you with?']
    speak(random.choice(statements))



def forWolframalpha():
    speak("I can do computational and geographical calculations and also answer some basic GK questions. You may ask me any such question, right about now")
    
    try:
        question = myCommand()
        appid = 'WYVXQ8-7YH93V3255'
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        res = client.query(question)
        answer = next(res.results).text
        speak(answer)
    except Exception as e:
        speak("I am sorry but i quite didn't get your question")
        forWolframalpha()



def WhatsApp():
    try: 
        temp = 0
        speak('Since I cannot access your contact list right now, you will have to type the mobile number to which you want me to send a message.')
        while (temp==0):
            speak('Please type the receiver\'s mobile number')
            mob = int(input())
            mob1 = str(mob)
            if len(mob1)!=(10):
                speak('This is an invalid number. Please try again.')
            else:
                speak('Now, please tell me the message that you want me to send')
                message = myCommand()
                print(message)
                speak('In the 24 hour format, please type the time at which you want to send the message in the format HH:MM')
                time = input().split(':')
                hr, min = int(time[0]), int(time[1])
                speak(f'Sending the message to {mob1} in a minute after Whatsapp Web is opened. Please do keep the WhatsApp app on your phone switched on for web.whatsapp.com to work')
                py.sendwhatmsg(f'+91{mob1}', message, hr, min, 60)
                speak('Do you want to send a message to someone else also? Type 0 for no and 1 for yes')
                t = int(input())
                if t==0:
                    temp = 1
                else:
                    continue
                
    except Exception as e:
        errors()
        WhatsApp()



def aboutJenny():
    speak("I am Jenny.")
    speak('Here is the list of commands that i can currently understand. I need the Internet to function properly, so please do connect your device to the Internet before calling me. Whenever you say something, please do add the keywords listed below')
    print('''
    1. How are you -- Gives you an expression about how Jenny is feeling.
    2. What can you do -- Triggers this page
    3. Math or GK -- Triggers computational and geographical analysis intelligence of Jenny
    4. time --  tells the current time
    5. date -- tells the current date
    6. open <app_name> -- opens a application or browser window based on what you say after open (currently supports Word, Excel, Powerpoint,  YouTube, Instagram, Spotify, Discord and Facebook).
    7. joke -- tell a random joke
    8. fact -- tell a random fact
    9. system -- you can ask battery status, cpu status etc using this
    10. wikipedia -- perform a search in wikipedia and prompts for a topic to search
    11. take -- take a screenshot or notes from the user based on what is aid after take
    12. read -- read a pdf or a already created note, based on what is said after read.
    13. news -- Speaks the top 10 headlines of the day
    14. weather -- asks for the city and then tells the weather info for that particular city
    15. play video online -- Asks the user what you want to watch, and then searches the whatever the user tells and plays the first video from the search suggestions on youtube
    ##16. sleep -- makes Jenny to go to sleep for a certain number of minutes
    ##17. reminder or remind -- creates a temporary reminder with a title and time
    18. whatsapp -- triggers a Whatsapp bot, which asks you a message to send, the number to send and the time to send the message. Uses WhatsApp Web to send the message
    19. stop -- Close Jenny
           ''')
    speak('I will wait for half a minute for you to go through the list of commands that you can give.')
    time.sleep(30)
    speak('So, what should I help you with?')



def reminder():
    try :
        speak('What do you want me to remind you about?')
        topic = myCommand()
        speak('Please type in how many minutes should the reminder go off.')
        mins = float(input())
        req_time = mins*60
        speak('Reminder set! Now I will not be able to assist you in any pther way till the reminder goes off')
        time.sleep(req_time)
        speak(f'Hey! You had a reminder set for {topic}')
    except Exception as e:
        errors()
        reminder()

# #######  MAIN CODE  #############


flag = 1
abcd = 0

if __name__=='__main__':
    
    wishMe()
    speak("Jenny at your service. After you see 'Listening' pop up, please tell me what i can help you with.")
    speak('If you want to know what i can do, tell \'What can you do\'')
    while flag == 1:
        command = myCommand().lower()
        if 'how' in command and 'are' in command and 'you' in command:
            expressions()
            anything_else()
            abcd = 0
        elif 'what can you do' in command:
            aboutJenny()
            abcd = 0
        elif 'math' in command or 'gk' in command:
            forWolframalpha()
            anything_else()
            abcd = 0
        elif 'time' in command or 'date' in command:
            date_or_time(command)
            anything_else()
            abcd = 0
        elif 'open' in command:
            open(command)
            anything_else()
            abcd = 0
        elif 'joke' in command:
            joke()
            anything_else()
            abcd = 0
        elif 'fact' in command:
            fact()
            anything_else()
            abcd = 0
        elif 'system' in command:
            sys_info()
            anything_else()
        elif 'wikipedia' in command:
            wiki()
            anything_else()
            abcd = 0
        elif 'take' in command:
            take(command)
            anything_else()
            abcd = 0
        elif 'read' in command:
            read(command)
            anything_else()
            abcd = 0
        elif 'news' in command:
            news()
            anything_else()
            abcd = 0
        elif 'weather' in command:
            weather()
            anything_else()
            abcd = 0
        elif 'play' in command and 'online' in command:
            playvid()
            anything_else()
            abcd = 0
        elif 'whatsapp' in command:
            WhatsApp()
            anything_else()
            abcd = 0
        elif 'sleep' in command:
            sleep()
            anything_else()
            abcd = 0
        elif 'stop' in command or 'no' in command:
            speak('It was nice talking to you. Hope you have a good day ahead!')
            flag = 0
        elif 'xyza' in command:
            flag = 0
        else:
            speak('Your command does not belong to the list of commands that i can interpret. Please try again.')
            abcd += 1
        if abcd == 5:
            speak('Sorry, but these are quite a lot of errors which i can\'t handle. Please try again later')
            flag = 0
