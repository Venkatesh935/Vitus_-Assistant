from voice.speech_to_text import listen
from voice.text_to_speech import speak


print("==============================")
print("       VITUS VOICE TEST")
print("==============================")


speak("Hello. I am Vitus. Please say something.")


command = listen()


if command:

    speak("You said " + command)

else:

    speak("I did not hear anything.")