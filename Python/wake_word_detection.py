import pyttsx3 # we can use gtts of google, tts-watson of ibm
import os
import speech_recognition as sr
import warnings
import time

warnings.filterwarnings('ignore')

def recordAudio():
    r = sr.Recognizer()

    #recoding of audio
    with sr.Microphone() as source:  
       print('Say something!')
       audio = r.listen(source)

    # add your recognizer code. We can use some prebuilt api or create our custom code
    print('recognizing!')
    try: 
        text = r.recognize_google(audio,language='en-US')
    except Exception as e:
        return "None" #better error handling
    print(text)

    # save sample disable for saving space

    # saveAudio(audio)

    return text.lower()


def saveAudio(audio):
    os.chdir("sample")
    timestr = time.strftime("%Y%m%d-%H%M%S")
    with open(timestr +'.wav', 'wb') as file:
        wav_data = audio.get_wav_data()
        file.write(wav_data)
    os.chdir("..")


def talk(engine,text):
    # engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#future aspect
def change_voice(engine,choice=1):
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[choice].id)
    engine.say("Here is my new voice")
    engine.runAndWait()

def is_wake(words):
    # variants that we accept as wake word
    return {
        'hey rodney': True,
        'hi rodney': True,
        'hi' : True,
        'hello' : True,
        # 'hey rocky': True,
        # 'hi rocky': True,
        # 'hey rob me': True,
        # 'hi rob me': True,
        # 'hey rugby': True,
        # 'hi rugby': True,
        # 'i wrote me': True,
    }.get(words, False)


print("Begin")
engine = pyttsx3.init()

talk(engine,"Good Morning")
while True:
    s = recordAudio() #get audio from mic 
    if is_wake(s): #check speek equal to wake word
        print("Wake word detected")
        # begin collecting audio and sending to HTTP endpoint in wav format.
        print("detected")
        s = recordAudio() #get audio from mic
