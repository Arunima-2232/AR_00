from os import path
import speech_recognition as sr
import sys
import whisper
import os
import pyttsx3
engine=pyttsx3.init()

base_model_path=os.path.expanduser('~/.cache/whisper/base.pt')
base_model=whisper.load_model(base_model_path)
r=sr.Recognizer()
source=sr.AudioFile("harvard.wav")

def listen_for_command():

    with source as s:
        print("listening for command...")
        r.adjust_for_ambient_noise(s)
        audio=r.listen(s)

    try:
        command=base_model.transcribe("harvard.wav")
        if command and command['text']:
            return command['text'].lower()
        return None
    except sr.UnknownValueError:
        return "could not understand"
    except sr.RequestError as e:
        return "error {0}".format(e)

def respond(text):
    if sys.platform!='darwin':
        engine.say(text)
        engine.runAndWait()
    

if __name__=="__main__":
    textToSay=listen_for_command()
    respond(textToSay)
