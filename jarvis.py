import os
import pyttsx3
import speech_recognition as sr
import requests

# ✅ Voice Engine Initialize (For Termux)
engine = pyttsx3.init()
engine.say("Hello, this is Termux AI Assistant")
engine.runAndWait()
engine.setProperty('voice', 'english')  # 'hi' for Hindi
engine.setProperty('rate', 150)
engine.setProperty('espeak_path', '/data/data/com.termux/files/usr/bin/espeak')


# ✅ Speech Recognition Initialize
recognizer = sr.Recognizer()

# ✅ Function: Speak Out
def speak(text):
    print(f"🤖 AI: {text}")
    engine.say(text)
    engine.runAndWait()

# ✅ Function: Listen
def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"👤 You: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("⚠️ Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            print("⚠️ Internet issue, switching to offline mode.")
            return "offline"

# ✅ Function: AI Chat (Online)
def chat_with_ai(user_input):
    api_key = "YOUR_OPENAI_API_KEY"  # 🔴 API Key Replace karo
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": user_input}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    return "Sorry, I couldn't process that."

# ✅ Function: AI Assistant Loop
def ai_assistant():
    speak("Hello! I am your AI assistant. How can I help you?")
    
    while True:
        command = listen()
        
        if "exit" in command or "stop" in command:
            speak("Okay, Goodbye!")
            break

        if command == "offline":
            responses = ["I am working offline!", "Sorry, I need internet for full features.", "Ask something else!"]
            speak(random.choice(responses))
        else:
            # ✅ Online Mode
            response = chat_with_ai(command)
            speak(response)

# ✅ Start AI Assistant
ai_assistant()
