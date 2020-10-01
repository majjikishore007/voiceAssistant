import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import wolframalpha

print("alexa startup")
print("hello world")
machine = pyttsx3.init('sapi5')
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[2].id)


def start_up():
    speak('Hello world , i am rose a bot ')


def speak(text):
    machine.say(text)
    machine.runAndWait()



def listen():
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold()
        print("say anything : ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print("sorry, could not recognise")
    return text





if __name__ == '__main__':
    start_up()
    while True:
        query = listen().lower()
        print(query)
        if 'open' in query:
            if 'open youtube' in query:
                webbrowser.open("https://www.youtube.com/")

            elif 'open google' in query:
                webbrowser.open("https://google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("https://stackoverflow.com")
            elif 'open spotify' in query:
                webbrowser.open("https://www.spotify.com/in/")

        else:
            try:
                result = wikipedia.summary(query, sentences=1)
                if result is None:
                    client = wolframalpha.Client("Client-id")#here u need to provide ur own clientID
                    result = next(client.query(query).results).text
                print("speaking results ")
                print(result)
                speak(result)
            except:
                print("no data found")
