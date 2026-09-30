import speech_recognition as sr
from core.state import state
import time

recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            state.emit("system", "🎤 Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            except sr.WaitTimeoutError:
                return ""
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as error:
            state.emit("system", f"❌ Speech recognition error: {error}")
            return ""
    except Exception as e:
        if "PyAudio" in str(e) or "pyaudio" in str(e):
            state.emit("system", "⚠️ PyAudio missing. Switch to terminal input for this session.")
            print("\n⚠️ PyAudio is missing. Please type your command below:")
            command = input("You: ")
            return command
        else:
            state.emit("system", f"❌ Microphone error: {e}")
            time.sleep(2)
            return ""
