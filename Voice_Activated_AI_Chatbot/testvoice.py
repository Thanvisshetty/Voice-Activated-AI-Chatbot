import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)

engine.say("Hello. This is a voice test.")
engine.runAndWait()
