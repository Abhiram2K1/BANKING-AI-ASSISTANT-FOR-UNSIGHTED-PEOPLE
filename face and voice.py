import cv2
import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize OpenCV video capture
cap = cv2.VideoCapture(0)

# Initialize speech recognition engine
r = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Load pre-trained face detection classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # Capture video frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Check if a face is detected
    # if len(faces) > 0:
    #     # Capture audio from microphone
    #     # with sr.Microphone() as source:
    #     #     print("Say something!")
    #     #     audio = r.listen(source)
    #
    #     # Recognize speech using Google Speech Recognition
    #     try:
    #         # command = r.recognize_google(audio)
    #         # print("Google Speech Recognition thinks you said " + command)
    #
    #         # Perform action based on recognized command
    #         if "hello" in command:
    #             engine.say("Hello there!")
    #             engine.runAndWait()
    #
    #         elif "goodbye" in command:
    #             engine.say("Goodbye!")
    #             engine.runAndWait()
    #
    #         elif "what time is it" in command:
    #             engine.say("The time is currently " + str(datetime.now().strftime('%I:%M %p')))
    #             engine.runAndWait()
    #
    #         else:
    #             engine.say("I'm sorry, I didn't understand what you said.")
    #             engine.runAndWait()
    #
    #     except sr.UnknownValueError:
    #         print("Google Speech Recognition could not understand audio")
    #
    #     except sr.RequestError as e:
    #         print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()