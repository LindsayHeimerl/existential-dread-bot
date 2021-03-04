import pyaudio 
from win32com.client import Dispatch
import speech_recognition as sr

#tests device microphone list
print(sr.Microphone.list_microphone_names())