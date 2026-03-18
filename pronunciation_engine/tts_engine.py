import os
import json
import base64
import hashlib
from pathlib import Path

from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

client = SarvamAI(api_subscription_key=os.getenv("SARVAM_API_KEY"))

CACHE_DIR = Path("scripts/audio_outputs/cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)


def _build_cache_key(
    text: str,
    target_language_code: str = "en-IN",
    speaker: str = "anushka",
) -> str:
    payload = {
        "text": text,
        "target_language_code": target_language_code,
        "speaker": speaker,
    }
    raw = json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _cache_path_from_key(cache_key: str) -> Path:
    return CACHE_DIR / f"{cache_key}.wav"


def text_to_speech_file(
    text: str,
    filename: str,
    target_language_code: str = "en-IN",
    speaker: str = "anushka",
    use_cache: bool = True,
) -> str:
    if not isinstance(text, str):
        raise TypeError(f"text must be a string, got {type(text).__name__}")

    output_path = Path(filename)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cache_key = _build_cache_key(
        text=text,
        target_language_code=target_language_code,
        speaker=speaker,
    )
    cached_file = _cache_path_from_key(cache_key)

    if use_cache and cached_file.exists():
        output_path.write_bytes(cached_file.read_bytes())
        return str(output_path)

    response = client.text_to_speech.convert(
        text=text,
        target_language_code=target_language_code,
        speaker=speaker,
    )

    audio_base64 = response.audios[0]
    audio_bytes = base64.b64decode(audio_base64)

    cached_file.write_bytes(audio_bytes)
    output_path.write_bytes(audio_bytes)

    return str(output_path)