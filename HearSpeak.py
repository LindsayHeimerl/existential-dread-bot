import pyaudio 
import wave
import os 
import numpy as np
from win32com.client import Dispatch
import threading
import speech_recognition as sr


r = sr.Recognizer()
p = pyaudio.PyAudio()
audio = None
speak = Dispatch("SAPI.SpVoice").Speak

mic = sr.Microphone(device_index = 1)
#find mic through sr.Microphone.list_microphone_names()

#Listen to audio input
def AudioThread():
    global audio
    while True: 
        with mic as source:
            try:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                print(audio)
            except sr.UnknownValueError:
                print("audio input unknown")
        

#give audio output in responce
def OutputThread():
    global audio
    while True:
        if audio is not None:
            speak("god fucking damn it") #Will have to replace with code for output speaker 
            audio = None


audio_input_thread = threading.Thread(target=AudioThread)
audio_input_thread.start()

output_thread = threading.Thread(target=OutputThread)
output_thread.start()



