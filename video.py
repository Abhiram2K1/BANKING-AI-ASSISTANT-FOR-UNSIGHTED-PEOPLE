import sys

import pyjokes as pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

import cv2
from simple_facerec import SimpleFacerec
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("faces/")

# Load Camera
cap = cv2.VideoCapture(0)

def talk(text):

    engine.say(text)
    engine.runAndWait()
    newVoiceRate = 125
    engine.setProperty('rate', newVoiceRate)

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'wisdom' in command:
                command = command.replace('wisdom', '')
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'work' in command:

        print('I can work by taking the user text and converting to the machine understandable form, through Speech Recognition.And the working process is simple one can tell the required options through the speaker and i can fill the forms and give them through the printer ')
        talk('i can work by taking the user text and converting to the machine understandable form, through Speech Recognition.And the working process is simple one can tell the required options through the speaker and i can fill the forms and give them through the printer')
    elif 'purpose' in command:
        print('I am wisdom banking bot. i am developed to solve the problems that are facing by the blind people in banking system. I can fill forms , i can tell the bank balance,and can talk multiple languages.')
        talk('I am wisdom banking bot. i am developed to solve the problems that are facing by the blind people in banking system.')
        talk('I can fill forms , i can tell the bank balance,and can talk multiple languages')
    elif 'operations' in command:
        print('one for form filling , two for banking services')
        talk('one for form filling , two for banking services')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'close' in command:
        sys.exit()
    else:
        talk('Please say the command again.')


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    print(face_locations,face_names)
    for face_loc, name in zip(face_locations, face_names):
        print("loc", face_loc)
        print("names", name)
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
    if len(face_names)>0:
        run_alexa()

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()