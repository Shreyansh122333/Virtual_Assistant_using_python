import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def speak(audio):
engine.say(audio)
engine.runAndWait()
def wishMe():
hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
speak("Good Morning!")
elif hour>=12 and hour<18:
speak("Good Afternoon!")
else:
speak("Good Evening!")
speak("I am your virtual assistant. Please tell me how may I help you")
def takeCommand():
#It takes microphone input from the user and returns string output
r = sr.Recognizer()
with sr.Microphone() as source:
print("Listening...")
r.pause_threshold = 1
audio = r.listen(source)
try:
print("Recognizing...")
query = r.recognize_google(audio, language='en-in')

print(f"User said: {query}\n")
except Exception as e:
# print(e)
print("Say that again please...")
return "None"
return query
def talk(text):
engine.say(text)
engine.runAndWait()
if __name__ == "__main__":
wishMe()
while True:
# if 1:
query = takeCommand().lower()
# Logic for executing tasks based on query
if 'search' in query:
speak('Searching in Wikipedia wait for a moment Sir...')
query = query.replace("search", "")
results = wikipedia.summary(query, sentences=2)
speak("According to Wikipedia")
print(results)
speak(results)
elif 'open youtube' in query:
webbrowser.open("youtube.com")
elif 'play' in query:
song = query.replace('play', '')
talk('playing ' + song)
pywhatkit.playonyt(song)
elif 'thank you' in query:
talk('your welcome')
elif 'team members' in query:
talk('Vikas, Nitin, Utkarsh, Shreyansh')
elif 'open google' in query:
webbrowser.open("google.com")
elif 'open nit bhopal' in query:
webbrowser.open("manit.ac.in")
elif 'python project' in query:
codePath = "C:\\Users\\91895\\PycharmProjects\\firstProject"
os.startfile(codePath)
elif 'the time' in query:
strTime = datetime.datetime.now().strftime("%H:%M:%S")
speak(f"Sir, the time is {strTime}")
