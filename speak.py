engine = pyttsx3.init()

def speak(text):
    """Function to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    try:
        speak("How are you, Ritik?")
    except Exception as e:
        print(f"An error occurred: {e}")
