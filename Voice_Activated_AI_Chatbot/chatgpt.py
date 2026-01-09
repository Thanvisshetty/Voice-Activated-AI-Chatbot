import pyttsx3
import wikipedia
import webbrowser
import datetime

def speak(text):
    print("Bot:", text)
    engine = pyttsx3.init('sapi5')   # 🔥 re-initialize every time
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your AI chatbot. Type your command below.")

if __name__ == "__main__":
    wishMe()

    while True:
        query = input("You: ").lower()

        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "wikipedia" in query:
            speak("Searching Wikipedia")
            topic = query.replace("wikipedia", "").strip()
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
            except:
                speak("Sorry, I could not find that information")

        elif "time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")

        elif "exit" in query or "quit" in query:
            speak("Goodbye")
            break

        else:
            speak("Sorry, I did not understand that command")
