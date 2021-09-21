from random import random
import speech_recognition as sr     # sr module
import datetime                     # d&t module
import requests
import pyjokes
import random
import webbrowser as wb              # web module
from translate import Translator     # t mod
import pyttsx3 as p
from pprint import pprint
now = datetime.datetime.now()       # m.c.method format


r = sr.Recognizer()                     # instance of the recognizer class
r1 = sr.Recognizer()
r2 = sr.Recognizer()
engine = p.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 196)
engine.setProperty('volume', 2.7)
engine.setProperty('voice', voices[1].id)

translation = {'translate', 'Translation'}
searching = {'search', 'open', 'visit', 'webpage'}
zoe_close = {'stop', 'end', 'close', 'thank you', 'thank you Lara'}
weather = {'weather', 'What is today\'s weather'}
joc = {'joke', 'jokes', 'tell me a joke'}
action = ["What can I do for you?",
          "How can I help?", "What can I do for you today?"]
with sr.Microphone() as source:
    engine.say("Lara is listening. Who is this ?")
    engine.runAndWait()
    print("Lara is listening. Who is this ?")
    lan = r1.listen(source)
    r1.adjust_for_ambient_noise(source)
    lan1 = r1.recognize_google(lan)
    print("Hello "+lan1+". Lara here !")
    engine.say("Hello "+lan1+",Lara here !")
    engine.runAndWait()
    while True:
        ac = random.choice(action)
        print(ac)
        engine.say(ac)
        engine.runAndWait()
        au = r.listen(source)
        p = r.recognize_google(au)
        print(p)
        if p == "today":
            engine.say(now)
            engine.runAndWait()
            print(now)
        elif p in translation:
            print("From which language you wanna translate?")
            engine.say("From which language you wanna translate?")
            engine.runAndWait()
            lan = r1.listen(source)
            r1.adjust_for_ambient_noise(source)
            lan1 = r1.recognize_google(lan)
            print(lan1)

            print("Enter the sentence: ")
            engine.say("Enter the sentence: ")
            engine.runAndWait()
            lan = r1.listen(source)
            r1.adjust_for_ambient_noise(source)
            t = r1.recognize_google(lan)
            print(t)

            print("To which language? ")
            engine.say("To which language? ")
            engine.runAndWait()
            lan = r1.listen(source)
            r1.adjust_for_ambient_noise(source)
            dest = r1.recognize_google(lan)
            print(dest)
            translator = Translator(from_lang=lan1, to_lang=dest)
            print(translator.translate(t))
            engine.say(translator.translate(t))
            engine.runAndWait()

        elif p in searching:
            au = r1.listen(source)
            p = r1.recognize_google(au)
            print(p)
            engine.say("Searching"+p)
            engine.runAndWait()
            wb.open('https://www.google.com/search?q='+p)

        elif p in weather:
            print("Of which city ?")
            engine.say("Of which city ?")
            engine.runAndWait()
            lan = r1.listen(source)
            r1.adjust_for_ambient_noise(source)
            city = r1.recognize_google(lan)
            print(city)
            base_url = "http://api.openweathermap.org/data/2.5/weather?q=" + \
                city+"&appid=701a37e959185e85b400911493cc5ca4"
            data = requests.get(base_url).json()
            print(data)

        elif p in joc:
            My_joke = pyjokes.get_joke(language="en", category="all")
            print(My_joke)
            engine.say(My_joke)
            engine.runAndWait()

        elif p in zoe_close:
            break
        else:
            print("Sorry couldn't understand. Can you repeat?")
            engine.say("Sorry couldn't understand. Can you repeat?")
            engine.runAndWait()


print("Thank you & Always here for you!!")
engine.say("Thank you & Always here for you!!")
engine.runAndWait()
