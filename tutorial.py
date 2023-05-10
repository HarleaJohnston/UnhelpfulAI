from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

#speech engine initialization 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 is for male;  1 for female
activationWord = 'Liz' #when you say Hello it will activate / it litens for the actication word


#configuring the browser going to open
#set the path 
edge_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))


def speak(text, rate = 150): 
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()


def parseCommand(): 
    listener = sr.Recognizer()
    print('Listening for a comand')

    with sr.Microphone() as source: 
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try: 
        print('Reconizing speech..')
        querey = listener.recognize_google(input_speech, language="en_gb")
        print(f"You said {querey}")
    except Exception as exception: 
        print("I didn't quite get that")
        speak("I didn't quite get that")
        print(exception)
        return 'None'
    
    return querey




def search_Wiki(querey = ''):
    searchResults = wikipedia.search(querey) 
    if not searchResults: 
        print('NO wikipedia result')
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
    speak("All systems nominal")

    while True:
        #Parse input into a list 
        querey = parseCommand().lower().split() #splits the command into a list broken up into different parts 

        if querey[0] == activationWord: #if the first word in the querey is hello do this thing
            querey.pop(0)

            if querey[0] == 'hello': 
                speak("Hi there!")
            #list commands 
         
            else: 
                querey.pop(0) #removes say 
                speech = ' '.join(querey) 
                speak(speech)

            #Navigating to a webstie 
            if querey[0] == 'go' and querey[1] == 'to':
                speak("Going to... ")
                querey = ' '.join(querey[2])
                webbrowser.get('edge').open_new(querey)

            #wikipedia 
            if querey[0] == 'wikipedia':
                querey = ' '.join(querey[1:])
                speak("Looking for that")
                result = search_Wiki(querey)
                speak(result)
                speak(search_Wiki(querey))