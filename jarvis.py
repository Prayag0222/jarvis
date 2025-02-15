import subprocess
import requests
import ollama

def is_internet_available():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except requests.ConnectionError:
        return False

def chat_with_ai(prompt):
    if is_internet_available():
        print("🔵 Online Mode: Using API")
        response = requests.post("https://api.together.ai/v1/chat/completions", json={
            "model": "openchat/openchat-7b",
            "messages": [{"role": "user", "content": prompt}],
        }, headers={"Authorization": "Bearer YOUR_API_KEY"})
        print(response.json()["choices"][0]["message"]["content"])
    else:
        print("🟢 Offline Mode: Using Llama-2")
        response = ollama.chat(model="llama2", messages=[{"role": "user", "content": prompt}])
        print(response["message"]["content"])

while True:
    user_input = input("👤 You: ")
    if user_input.lower() == "exit":
        break
    chat_with_ai(user_input)
