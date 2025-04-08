import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "95314b26a2ba413eacdfdb7022ae9769"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiprocess(command):
    client = OpenAI( api_key="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",
    )

    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud."},
        { "role": "user", "content": "command"}
    ]
    )

    return print(completion.choices[0].message.content)


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            #parse the json response
            data = r.json()

            #Extract the articles
            articles = data.get('articles', [])

            # Print the headlines
            for article in articles:
                speak(article['title'])

    else:
        # let OpenAIchandle the request
        output = aiprocess(c)
        speak(output)


    

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        # listen for the wake word "Jarvis"
        # Obtain audio from microphone
        r = sr.Recognizer()
        

        print("recognizing...")
        # recognize speech using sphinx
        try:
            with sr.Microphone() as source:
                  print("Listening...")
                  audio = r.listen(source ,timeout=2, phrase_time_limit=1)
            word  = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("hello ")
                #Listen for command
                with sr.Microphone() as source:
                  print("jarvis active...")
                  audio = r.listen(source)
                  command = r.recognize_google(audio)

                  processCommand(command)

       
        except Exception as e:
            print("Error; {0}".format(e))
