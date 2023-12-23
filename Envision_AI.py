import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import pywhatkit as kit
import warnings
import subprocess as sp
import psutil


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)  
    engine.runAndWait()
    

warnings.simplefilter("ignore") 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query =r.recognize_google(audio, language='en-in')
        # speak(query)
        print("User said: ",query,end='\n')
        
      
    except:
        return "None"
    return query.lower()


def wishme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
 
    speak("I am Envision. please tell me how may i help you")
    
    


def openapps():
    
    if 'microsoft edge' in query:
        codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(codePath)
        
    if 'open notepad' in query:
        codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
        os.startfile(codePath)
        
    elif 'open photoshop' in query:
        codePath = "C:\\Program Files\\Adobe\\Adobe Photoshop 2023\\Photoshop.exe"
        os.startfile(codePath)
          
    elif 'open powerpoint' in query:
        codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
        os.startfile(codePath)
        
    elif 'open word'in query:
        codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
        os.startfile(codePath)
        
    elif 'open excel'in query:
        codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
        os.startfile(codePath)
        
    elif 'open zoom' in query:
        codePath = "C:\\Users\\MD FAISAL KHAN\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
        os.startfile(codePath)
              
    elif 'movie folder' in query:
        codePath = "D:\Movies"
        os.startfile(codePath)
              
    elif 'open telegram' in query:
        codePath = "C:\\Users\\MD FAISAL KHAN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
       
    elif 'open filmora' in query:
        codePath = "C:\\Program Files\\Wondershare\\Filmora9\\Wondershare Filmora9.exe"
        os.startfile(codePath)
        
    elif 'play music on youtube' in query:
        speak("sir, which music do you want to listen?")
        cm = takecommand()
        kit.playonyt(cm)
    
    elif 'open camera' in query:
        try:
            sp.Popen('start microsoft.windows.camera:', shell=True)
            speak("Opening the camera")
        except Exception as e:
            print(e)
            speak("Sorry, I couldn't open the camera.")
        
    
         
    elif 'play movie' in query:
        speak("Which movie do you want to play sir?")
        MovieName = takecommand()
        movie_path_mp4 = f"D:\\Movies\\{MovieName}.mp4"
        movie_path_mkv = f"D:\\Movies\\{MovieName}.mkv"
        
        if os.path.exists(movie_path_mp4):
            os.startfile(movie_path_mp4)
            speak(f"Okay sir, take your seat and enjoy {MovieName}")
        elif os.path.exists(movie_path_mkv):
            os.startfile(movie_path_mkv)
            speak(f"Okay sir, take your seat and enjoy {MovieName}")
        else:
            speak(f"Sorry, {MovieName} is not found in the Movies directory")
            
    elif 'play song' in query:
        speak("Which song do you want to play sir?")
        songName = takecommand()
        
        if songName: 
            codePath = f"D:\\music\\{songName}.mp3"
            
            if os.path.exists(codePath):
                os.startfile(codePath)
                speak(f"playing {songName}")
            else:
                speak("Sorry sir, the song was not found.")
        else:
            speak("Sorry sir, unable to understand the song name.")
                    
      
                
if __name__ == "__main__":

    wishme()
    while True:
        query =takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching Sir...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia ")
            speak(result)
            
        elif 'open youtube' in query:
            speak("opening youtube sir")
            wb.open("https://www.youtube.com/")
            
        
        elif 'open irctc' in query:
            speak("opening I R C T C platform sir")
            wb.open("https://www.irctc.co.in/nget/train-search")
            
            
        elif 'open instagram' in query:
            speak("opening instagram sir")
            wb.open("https://www.instagram.com/")
       
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            wb.open("C:\\Users\\MD FAISAL KHAN\\Desktop\\WhatsApp.lnk")
            
        elif 'open facebook' in query:
            speak("opening facebook sir")
            wb.open("https://www.facebook.com/")
            
        elif 'open twitter' in query:
            speak("opening twitter sir")
            wb.open("https://www.twitter.com/")
        
        elif (("open google")or("open new tab")) in query:
            speak("sir, what do you want to search?")
            cm = takecommand()
            speak(f"Searching {cm}")
            wb.open(f"{cm}")
        
        elif 'the time' in query:
            strtime1 = datetime.datetime.now().strftime("%H")
            strtime2 = datetime.datetime.now().strftime("%M")
            speak(f"Sir the time is {strtime1}:{strtime2}")
            
            
        elif "today's date" in query:
            today_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today's date is {today_date}")
        
        elif 'shutdown' in query:
            while True:
                speak("Do you want to shutdown the computer ?")
                command = takecommand()
                if 'no' in command:
                    speak("Thank u sir I will not shut down the computer ")
                    break
                elif 'yes' in command:
                    speak("Shutting down , goodbye")
                    os.system('shutdown /s /t 1')
                else:
                    speak("say again")
                    
        elif 'battery' in query:
            battery = psutil.sensors_battery()
            if battery is not None:
                percent = battery.percent
                speak(f"Your laptop's battery is currently at {percent} percent.")
            else:
                speak("I couldn't retrieve the battery information at the moment.")

# ----------open apps-------------

        elif 'microsoft edge' in query:
            speak("opening microsoft edge ")
            openapps()
            
        elif 'open notepad' in query:
            speak("opening Notepad ")
            openapps()

        elif 'photoshop' in query:
            speak("opening photoshop")
            openapps()
            
        elif 'word' in query:
            speak("opening microsoft word")
            openapps()
            
        elif 'excel' in query:
            speak("opening microsoft Excel")
            openapps()
            
        elif 'powerpoint' in query:
            speak("opening powerpoint")
            openapps()
                        
        elif 'zoom' in query:
            speak("opening zoom sir ")
            openapps()
            
        elif 'microsoft word' in query:
            speak("opening microsoft word")
            openapps() 
               
        elif 'movie folder' in query:
            speak ("Opening movie folder")          
            openapps()
            
        elif 'open telegram' in query:
            speak ("Opening telegram")          
            openapps()
            
        elif 'open filmora' in query:
            speak ("Opening filmora9")          
            openapps()
            
        elif 'play movie' in query:
            openapps()
            
        elif 'play song' in query:
            openapps()
      
        elif 'play music on youtube' in query:
            openapps()
            
        elif 'open camera' in query:
            openapps()
            
        
# ---------------------------------------------------------
        elif 'hello' in query:
            speak("hello Sir")
            
        elif ('hi envision' or 'hi') in query:
            speak("hi Sir")
            
        elif ('quit')  in query:
            speak("Quitting sir")
            break
        
        elif ('turn off')  in query:
            speak("turning off sir")
            break
        
        elif ('envision')  in query:
            speak("Yes sir , tell me how can i help you")

        elif 'i am fine' in query:
            speak("Thats great")    
            
        elif (("what is my name") or ("what's my name")) in query:
            speak("Your name is Md Faisal Khan")
            
        elif ("who are you" or "hu r u") in query:
            speak("I am envision. A Artificial intelligence")
            
        elif ("my birthday") in query:
            speak ("your birthday is 18 December")
            
        elif ("how are you") in query:
            speak("I am fine sir.")
       
       
        elif 'group members' in query:
           
            print(''' 
                  1. Munzir hashmi 
                  2. Shaharyar hashmi 
                  3. Md Faisal khan
                  4. Sourav mondal  
                  5. Raj Rakshit 
                  6. Raunak raj ''')
            speak(''' The group members name is 
                  1. Munzir hashmi 
                  2. Shaharyar hashmi 
                  3. Md Faisal khan
                  4. Sourav mondal  
                  5. Raj Rakshit 
                  6. Raunak raj ''')
            
            
    
        #============Automation==============
        
        elif 'send message' in query:
               
            speak("who do you want to message")
            name = takecommand()
            speak(f"Whats the message for {name}")
            msg = takecommand()
            speak(f"sending messege to {name}")
            from Automation import wtspmsg
            wtspmsg(name,msg) 
                               
         
        elif 'search on youtube' in query:
            speak("What do you want to search ?")
            search=takecommand()
            speak(f"Searching {search}")
            from Automation import youtubeSearch
            youtubeSearch(search)
        
        elif 'send email' in query:
            speak("Who to you want to email, please enter the email ID")
            name=input("Email id: ")
            if name!="":
                speak("What's the message")
                msg=takecommand()
                from Automation import mail
                mail(name,msg)
            else:
                speak("Sorry! Something went wrong")
                
            
        elif 'voice call' in query:
            speak("Who do you want to call")
            name = takecommand()
            speak(f"calling {name}")
            from Automation import VoiceCall
            VoiceCall(name)
          
        elif 'video call' in query:
            speak("Who do you want to video call")
            name = takecommand()
            speak(f"calling {name}")
            from Automation import VideoCall
            VideoCall(name)
        
        elif 'university portal' in query:
            speak("Please Enter your student Username: ")
            username=input("Username: ")
            speak("Please Enter your student Password: ")
            password=input("Password: ")
            if username!="" and password!="":
  
                speak("Login to Makaut Portal")
                from Automation import makautlogin
                makautlogin(username,password)                
                
            else:
                speak("please enter you Username password correctly")
            