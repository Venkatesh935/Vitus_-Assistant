import openwakeword
from openwakeword.model import Model


# Download the available pre-trained wake-word models
openwakeword.utils.download_models()


# Load the wake-word model
model = Model()


def detect_wake_word():
    print("🎧 Waiting for wake word...")

    # This function will be completed with
    # microphone audio processing.
    return False