# iKHOM my Virtual Assistant 

# (motivated from Amazon's Alexa)

# @author: KhomZ 
# code coming soon
# coding started at 18th Nov 2021,

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # 1 is for female voice and 0 is for male voice


# now lets define a function that accepts the user's command
def input_query():
    recognizer = sr.Recognizer() # to recognize  from an audio source
    with sr.Microphone() as source: # source of recognition
        print('recognition is on....') 
        recognizer.pause_threshold = 0.7
        voice =recognizer.listen(source) # this method in turnwill record the input from the audio source as long as there's some voice or someone is speaking
        try:
            # print(x)
            query = recognizer.recognize_google(voice).lower()
            print('This is the query that was made....', query)
            return query
        except Exception as ex:
            print('An exception occurred', ex)


# now create function for action
def activate_va():
    user_query = input_query()
    print('user query ....', user_query)

while True:
    activate_va()