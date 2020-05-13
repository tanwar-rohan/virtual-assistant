#pip install pyaudio
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        print("Good Afternoon!")
        speak("Good Afternoon!")   


    else:
        print("Good Evening!")  
        speak("Good Evening!")  

    print("I am your virtual assistant ")
    speak("I am your virtual assistant ")
    
    now = datetime.datetime.now()
    print ("today's date & time is ")
    strTime = datetime.datetime.now().strftime("%m-%d-%Y")
    print (f"date is {strTime}")
    speak(f"today's date is {strTime}")
     
    strTime = datetime.datetime.now().strftime(" %H:%M:%S")
    print (f"time is {strTime}")
    speak(f"& time is {strTime}")


           
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tanwarrohan632@gmail.com', 'sxoncldnaxcfbois')
    server.sendmail('tanwarrohan632@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    flag='yes'
    while flag=='yes':
        print("Sir. Please tell me how may I help you")
        speak("Sir. Please tell me how may I help you")
       
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print("According to Wikipedia")
            speak("According to Wikipedia")
            
            print(results)
            speak(results)

        elif 'open youtube' in query:
            url='youtube.com'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            url='google.com'
            webbrowser.get(chrome_path).open(url)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\rohan\\Documents\\Rockstar Games\\GTA V\\User Music'
            songs = os.listdir(music_dir)
            file=random.choice(songs)
            ext3=['.mp3']
            print('song: '+file)    
            os.startfile(os.path.join(music_dir, file))
        

        elif 'send email' in query:
            try:
                a='yes'
                while a=='yes':
            
                    print("enter the email")
                    speak("enter the email")
                    user_email = takeCommand().lower()
                    print(user_email)
                    speak("confirm the email")
                    speak("'YES' to continue")
                    speak("'no' to enter email again")
                    con_email=takeCommand()
                    if 'yes' in con_email:
                        print("What should I say?")
                        speak("What should I say?")
                        content = takeCommand()
                        sendEmail(user_email, content)
                        speak("Email has been sent!")
                        a='no'
                    else:
                        a='yes'

                    
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'bye ' in query:
            print("bye sir. hope you are satisfied")
            speak("bye sir. hope you are satisfied")
            exit()
        

        print("\t \n want to continue ")
        speak("\t \n want to continue ")

        print(" 'yes' or 'no' :")
        speak(" 'yes' or 'no' :")
        retry = takeCommand()
        if 'yes' in retry:
            flag='yes'
        else:
            flag='no'
            print("bye sir. hope you are satisfied")
            speak("bye sir. hope you are satisfied")
            exit()
        
             
