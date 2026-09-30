from voice.speech_to_text import listen
from voice.text_to_speech import speak

from core.command_processor import process_command


class VitusAssistant:

    def start(self):

        print("================================")
        print("          VITUS AI")
        print("================================")

        speak("Hello, I am Vitus. I am ready to help you.")

        while True:

            print()
            print("🎤 Waiting for your command...")

            command = listen()

            if not command:
                continue

            command = command.lower().strip()

            print("Recognized command:", command)

            # Exit command
            if (
                "exit" in command
                or "quit" in command
                or "stop vitus" in command
            ):

                speak("Goodbye. See you later.")
                break

            # Process command
            response = process_command(command)

            # Speak response
            speak(response)