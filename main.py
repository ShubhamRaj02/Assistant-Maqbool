import pyttsx3  # pip install pyttsx3 #text to speech
import datetime 
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia
import webbrowser
import os
import random
import mailer
import subprocess
from googlesearch import search #to search on program
import urllib
import string
import smtplib

yt_url = 'https://www.youtube.com'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

asname = 'MAQBOOL'
#text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)
print("What you have to say ...")
print("Query = Email : For sending informal email")
print("Query =  Wikipedia : for searching in wikipidea")
print("Query = Search MAQBOOL : for Searching and opening first five tab in browser")
print("Query = open Youtube : For opening youtube")
print("Query = open Instagram : For Instagram")
print("Query = Say time : For saying time and date")
print("Query = open shop2day :For opening shop2day site")
print("Query = open Url : For opening url")
print("Query = open turkish tv : For opening turkfans.com website")
print("Query = open Blackboard : For Opening blackbord login page")
print("Query = music from pc : For play music from pc")
print("Query = Video from pc : For playing video from pc")
print("Query = open teams :For opening teams")
print("Query = open today class : For opening today classes")
print("Query = open notepad : For opening notepad")
print("Query =  open whatsapp : For opening wahatsapp")
print("Query = open powershell : Opening commandline interface")
print("Query = good bye : For shutting down assistant")



def speak(audio): # there is audo is var which contain text 
    engine.say(audio)      #text to speech
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)

def Wikipidea_search():
    query = (takeCommand())
    print(query)
    speak("Searching Details....wait")
    query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences=6)
    print(results)
    speak(results)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(day)
    speak(month)
    speak(year)

def Search():
    k = "What you want me to search ? "
    print(k)
    speak(k)
    query = (takeCommand())
    print(query)
    speak("searching on google....wait")
    for j in search(query, tld="co.in", num=5, stop=5,pause=2):
        webbrowser.open(j)
        print(j)


def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        A = "Good Morning  sir, I am your Assistent MAQBOOL at your service"
        speak(A)
        print(A)

    elif hour >= 12 and hour < 18:
        B="Good Afternoon and Welcome back Sir, I am your Assistent MAQBOOL at your service"
        speak(B)
        print(B)
    elif hour >= 18 and hour < 24:
        C="Good Evening and Welcome back Sir, I am your Assistent MAQBOOL at your service"
        speak(C)
        print(C)
    else:
        D = "Good night and Welcome back Sir, I am your Assistent MAQBOOL at your service"
        speak(D)
        print(D)
        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizning...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please")
        
        return "None"
    return query

def url():
    Maqbool= 'MAQBOOL :-> what is your url, you want to open ?'
    print(Maqbool)
    speak(Maqbool)
    query = (takeCommand())
    query = query.translate({ord(c): None for c in string.whitespace})
#    webbrowser.open("www."+query)
#    speak("opening website")
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# chrome_path = '/usr/bin/google-chrome %s'

    webbrowser.get(chrome_path).open(query)
    speak ('opening'+query)

def Email():
    Reciver = "please type Recipeant's E-mail"
    speak(Reciver)
    REmail = input("What is Recpent's Email :- ")
    speak(REmail)
    Massage = input("Type your message, Please :- ")
    speak (Massage)
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("wtfisthisooo7@gmail.com","8541991003")
    server.sendmail("wtfisthisooo7@gmail.com",
                    REmail,
                    Massage)
    print("E-mail Sent")
    server.quit()

def calculator():
    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    speak("opening Calculator")


# For main function
if __name__== "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            W = "What you want to search in wikipidea"
            speak(W)
            
            Wikipidea_search()

        elif "search" in query:
            Search()

        elif "calculator" in query or "open calculator" in query:
            calculator()
        elif 'open youtube' in query or "youtube" in query:
                webbrowser.open("www.youtube.com")
                speak("opening youtube")
                
        elif 'open instagram' in query or "please open instagram" in query:
                webbrowser.open("www.instagram.com")
                speak("opening Instagram")

        elif 'Time' in query or "Date" in query:
            speak("The current time is")
            time()
            speak("the Today date is")
            date()

        elif 'email' in query or 'mail' in query:
            Email()
                
        elif 'open shop2day' in query or 'open shop today' in query:
                webbrowser.open("www.soap2day.video")
                speak("opening.....Shop2day")

        elif 'open url' in query:
            url()
                
        elif 'open Turkish TV' in query or 'open turk fans' in query:
                webbrowser.open("www.turkfans.com/")
                speak("opening.....Turkfans")
                
        elif 'open Blackboard' in query or 'open blackboard' in query:
                webbrowser.open("https://cuchd.blackboard.com/")
                speak("opening.....Blackboard")
                
        elif 'music from pc' in query or "play music from laptop" in query:
                speak("ok I am playing music")
                music_dir = "D:\Semester 5\Code with herry\python\Projects Youtube\jarvis\music"
                musics = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,musics[0]))
                
        elif 'video from pc' in query or "play video from laptop" in query:
                speak("ok I am playing videos")
                video_dir = "D:\\Semester 5\\Code with herry\\python\\Projects Youtube\\jarvis\\video"
                videos = os.listdir(video_dir)
                os.startfile(os.path.join(video_dir,videos[0]))
                
        elif 'open teams' in query or "start my class" in query:
            webbrowser.open("https://teams.microsoft.com/_#/school//?ctx=teamsGrid")
            speak("opening microsoft teams")

        elif 'open today class' in query or "what is my today shedule " in query:
            webbrowser.open("https://teams.microsoft.com/_#/calendarv2")
            speak("opening microsoft teams  calanders")

        elif 'open notepad' in query or " open notepad " in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            speak("opening Notepad")

        elif 'open whatsapp' in query or " open whats app " in query:
            subprocess.Popen("C:\\Users\\chitranjan\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            speak("opening Whatsapp")

        elif 'open powershell' in query or " open command prompt " in query:
            subprocess.Popen("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")
            speak("opening powershell")


        elif 'send email ' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "shubhamsharmaisback@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as Q:
                print (Q)
                speak("Sorry Sir , I am not able to send your e-mail ")
                
                
        elif 'good bye' in query or 'goodbye' in query:
                speak('good bye sir')
                exit()

        elif 'abort' in query or 'mission failed' in query:
            speak("Abort, Abort, Abort!!! Abort the mission, Delete and Destroy the data base")
            print("Abort, Abort, Abort!!! Abort the mission, Delete and Destroy the data base")

        elif "shutdown" in query or "shutdown laptop" in query:
                choice= True
                while(choice):
                    shutdown = "Do you wish to shutdown your computer ? (yes or no): "
                    print(shutdown)
                    speak(shutdown)
                    query = (takeCommand())
                    print(query)
                    if query == 'yes':
                        speak("Shutting down")
                        print("Shutting down")
                        choice= False
                        os.system("shutdown /s /t 1")
                    elif query == 'no':
                        speak("OK Sir")
                        choice=False
                    elif query != 'yes' or 'no':
                        print("INVALID INPUT !!!!!")
                        speak("invalid input")
                    
                
