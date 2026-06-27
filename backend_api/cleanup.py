from pathlib import Path
from time import time


GENERATED_AUDIO_DIR = Path("backend_api/generated_audio")
TTS_CACHE_DIR = Path("scripts/audio_outputs/cache")

GENERATED_AUDIO_TTL_SECONDS = 60 * 60          # 1 hour
TTS_CACHE_TTL_SECONDS = 24 * 60 * 60          # 24 hours


def cleanup_old_files(directory: Path, ttl_seconds: int) -> int:
    """
    Deletes files older than ttl_seconds from the given directory.
    Returns number of deleted files.
    """
    if not directory.exists():
        return 0

    now = time()
    deleted = 0

    for file_path in directory.glob("*"):
        if not file_path.is_file():
            continue

        try:
            age_seconds = now - file_path.stat().st_mtime

            if age_seconds > ttl_seconds:
                file_path.unlink()
                deleted += 1

        except FileNotFoundError:
            continue
            # File may have been removed by another request.
        except PermissionError:
            continue

    return deleted


def cleanup_audio_files() -> dict:
    generated_deleted = cleanup_old_files(
        GENERATED_AUDIO_DIR,
        GENERATED_AUDIO_TTL_SECONDS,
    )

    cache_deleted = cleanup_old_files(
        TTS_CACHE_DIR,
        TTS_CACHE_TTL_SECONDS,
    )

    return {
        "generated_audio_deleted": generated_deleted,
        "tts_cache_deleted": cache_deleted,
    }