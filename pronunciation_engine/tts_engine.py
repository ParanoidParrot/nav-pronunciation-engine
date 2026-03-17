import os
import base64
from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

def text_to_speech_file(text: str, filename: str):

    response = client.text_to_speech.convert(
        text=text,
        target_language_code="en-IN",
        speaker="anushka"
    )

    audio_base64 = response.audios[0]

    audio_bytes = base64.b64decode(audio_base64)

    with open(filename, "wb") as f:
        f.write(audio_bytes)

    return filename