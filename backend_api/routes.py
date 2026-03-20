import hashlib
import re
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from backend_api.schemas import Instruction, DemoCompareResponse
from pronunciation_engine.normalizer import normalize_instruction
from pronunciation_engine.tts_engine import text_to_speech_file

router = APIRouter()

GENERATED_AUDIO_DIR = Path("backend_api/generated_audio")
GENERATED_AUDIO_DIR.mkdir(parents=True, exist_ok=True)


def _slugify(text: str, max_len: int = 40) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text[:max_len] if text else "sample"


def _hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


@router.post("/normalize")
def normalize(data: Instruction):
    result = normalize_instruction(data.instruction)
    return {"normalized": result}


@router.get("/audio/{filename}")
def get_audio(filename: str):
    file_path = GENERATED_AUDIO_DIR / filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="Audio file not found")

    return FileResponse(
        path=str(file_path),
        media_type="audio/wav",
        filename=file_path.name,
    )


@router.post("/demo/compare", response_model=DemoCompareResponse)
def compare_audio(data: Instruction):
    original_text = data.instruction
    normalized_text = normalize_instruction(original_text)

    raw_slug = _slugify(original_text)
    norm_slug = _slugify(normalized_text)

    raw_hash = _hash_text("raw::" + original_text)
    norm_hash = _hash_text("norm::" + normalized_text)

    raw_file = GENERATED_AUDIO_DIR / f"raw_{raw_slug}_{raw_hash}.wav"
    norm_file = GENERATED_AUDIO_DIR / f"normalized_{norm_slug}_{norm_hash}.wav"

    text_to_speech_file(
        text=original_text,
        filename=str(raw_file),
        target_language_code="en-IN",
        speaker="anushka",
        use_cache=True,
    )

    text_to_speech_file(
        text=normalized_text,
        filename=str(norm_file),
        target_language_code="en-IN",
        speaker="anushka",
        use_cache=True,
    )

    return DemoCompareResponse(
        original_text=original_text,
        normalized_text=normalized_text,
        original_audio_url=f"/audio/{raw_file.name}",
        normalized_audio_url=f"/audio/{norm_file.name}",
    )