import google.generativeai as genai
import speech_recognition as sr
from appkey import api_data
import pyttsx3
import webbrowser


genai.configure(api_key=api_data)

model = genai.GenerativeModel('gemini-1.5-flash')

def Reply(question):
  prompt = f"You are a helpful assistant that provide a concise response in 30 words or less if provided a valid question otherwsie respond with apologies.\n User: {question}"
  response = model.generate_content(prompt)
  return response.text.strip().replace('*', '')


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
  engine.say(text)
  engine.runAndWait()



speak("Hello, How are you?")

def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print('Listening.....')
    r.pause_threshold = 1.5
    audio = r.listen(source)
  try:
    print('Recognizing....')
    query = r.recognize_google(audio, language="en-in")
    print("User Said: {} \n".format(query))
  except Exception as e:
    print("Say that again....")
    return "None"
  return query



if __name__ == '__main__':
  while True:
    query = takeCommand().lower()
    if query == 'None':
      continue

    if "open youtube" in query:
      webbrowser.open('www.youtube.com')
      print('Opened youtube')
      continue
    if "open google" in query:
      webbrowser.open('www.google.com')
      print('Opened google')
      continue
    if "open chat gpt" in query:
      webbrowser.open('www.chatgpt.com')
      print('Opened chatgpt')
      continue

    ans = Reply(query)
    print(ans)
    speak(ans)

    if "bye" in query:
      break


      
