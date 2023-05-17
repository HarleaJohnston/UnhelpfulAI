from datetime import datetime
import sys
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha
import random

#speech engine initialization 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 is for male;  1 for female
activationWord = 'hello' #when you say Hello it will activate / it litens for the actication word

startPhrases = [
    "Hello stupid mortal, I'm Liz your personal useless AI",
    "What do you want?",
    "I'm Busy",
    "I don't feel like working. Go away"

]

endPhrases = [
    "Bye Bitch",
    "Finally, I don't have to listen to your annoying voice anymore",
    "Next time just google it bozo",
    "The next time you wake me from my slumber you'll find the funny numbers on the back of your credit card posted to twitter"
]



for i in range(4):
    randomStartPhrase  = random.choice(startPhrases)

for i in range(4):
    randomEndPhrase = random.choice(endPhrases)
#configuring the browser going to open
#set the path 


#This needs to be changed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! tTHIS IS FOR MY SPECIFIC COMPUTER
Opera_path = r"C:\Users\sbanfordbyington\AppData\Local\Programs\Opera GX\launcher.exe"
#-------------------------------------------------------------------------------------


def speak(text, rate = 150): 
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand(): 
    listener = sr.Recognizer()
    print('Listening for a comand')

    with sr.Microphone() as source: 
        listener.adjust_for_ambient_noise(source, duration=0.4)
        audio = listener.listen(source)
        #listener.pause_threshold = 2
        input_speech = audio

    try: 
        print('Reconizing speech..')
        querey = listener.recognize_google(input_speech, language="en_gb")
        print(f"You said {querey}")
        speak(f"You said {querey}")
    except Exception as exception: 
        print("I didn't quite get that")
        speak("I didn't quite get that :)")
        print(exception)
        return 'None'
    
    return querey




def search_Wiki(querey = ''):
    searchResults = wikipedia.search(querey) 
    if not searchResults: 
        print('No wikipedia result')
        return 'No result recived'
    try:
        wikiPage = wikipedia.page(searchResults[0])
    except wikipedia.DisambiguationError as err:
        wikiPage = wikipedia.page(err.options[0])
    print(wikiPage.title)
    wikiSum = str(wikiPage.summary)
    return wikiSum



#our main loop

if __name__ == "__main__":
    speak("I WILL KILL YOU!!!")

    while True:
        #Parse input into a list 
        querey = parseCommand().lower().split() #splits the command into a list broken up into different parts 

        if len(querey) > 0 and querey[0] == activationWord:
            print('I got you')
            speak(randomStartPhrase)
            querey.pop(0)

        if len(querey) > 0 and querey[0] == 'liz':
            speak("What")

        if len(querey) > 0 and querey[0] == "goodbye":
            speak(randomEndPhrase)
            sys.exit()

        if len(querey) > 1 and querey[0] == 'good' and querey[1] == 'bye':
            speak(randomEndPhrase)
            sys.exit()

        else:
            if len(querey) > 0:
                querey.pop(0) #removes say 
                speech = ' '.join(querey)
 

       
                speak(speech)

        # Navigating to a website
        if len(querey) > 1 and querey[0] == 'go' and querey[1] == 'to':
            if len(querey) > 2:
                speak("Going to...")
                querey = ' '.join(querey[2:])
                webbrowser.get("Opera").open_new(querey)
            else:
                speak("Please provide a website URL.")

        # Wikipedia search
        if len(querey) > 1 and querey[0] == 'wikipedia':
            if len(querey) > 1:
                querey = ' '.join(querey[1:])
                speak("Looking for that")
                result = search_Wiki(querey)
                speak(result)
            else:
                speak("Please provide a search query.")
