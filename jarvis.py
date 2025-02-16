import speech_recognition as sr
import pyttsx3

# AI voice setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speech speed
engine.setProperty('voice', 'english')  # Voice type

def speak(text):
    """AI ka jawab bolne ke liye function"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """User ki voice sunne ke liye function"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Background noise adjust
        try:
            audio = recognizer.listen(source, timeout=5)  # Sunne ka time limit
            command = recognizer.recognize_google(audio)  # Speech to Text
            print(f"👤 You: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Sorry, couldn't understand.")
            return ""
        except sr.RequestError:
            print("⚠️ No internet, working offline.")
            return ""

# Main AI loop
while True:
    user_input = listen()
    if "exit" in user_input or "bye" in user_input:
        speak("Goodbye! Have a nice day.")
        break
    elif "hello" in user_input:
        speak("Hello! How can I help you?")
    elif "your name" in user_input:
        speak("I am your personal assistant.")
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
    else:
        speak("I didn't understand that.")
