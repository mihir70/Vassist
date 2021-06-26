import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[0].id)
print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#speak('Hi My name is Jarvis')

def wish():
    hr=int(datetime.datetime.now().hour)
    if hr>=6 and hr<12:
        speak('Good Morning Sir')
    elif hr>=12 and hr<16:
        speak('Good Afternoon Sir')
    elif hr>=16 and hr<20:
        speak('Good Evening sir')
    else:
        speak('Good Night sir')
    speak('How may I help you sir')
wish()

def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print('Trying to recognize..')
        query=r.recognize_google(audio,language='en-in')
        print('User said: ',query)
        return query
    except:
        print('Say that again')
        return "None"
while True:
    query= take().lower()
    if 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
    elif 'open linkedin' in query:
        webbrowser.open("linkedin.com")
    elif 'open instagram' in query:
        webbrowser.open("instagram.com")
    elif 'time' in query:
        strt=datetime.datetime.now().strftime("%H:%M:%S")
        print('the time is: ',strt)
    elif 'song' in query:
        webbrowser.open('https: // www.youtube.com/results?search_query='+ query)
    elif 'wikipedia' in query:
        query=query.replace('wikipedia','')
        result=wikipedia.summary(query,sentences=2)
        print(result)
        speak(result)
    elif 'leave' in query or 'break' in query or 'live' in query:
        speak("Goodbye Sir")
        break
    


