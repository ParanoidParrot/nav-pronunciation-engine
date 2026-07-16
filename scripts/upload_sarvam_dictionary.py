import os
from pathlib import Path

from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

DICT_PATH = Path("sarvam_pronunciation_dict.json")


def main() -> None:
    api_key = os.getenv("SARVAM_API_KEY")

    if not api_key:
        raise RuntimeError("SARVAM_API_KEY is not set")

    if not DICT_PATH.exists():
        raise FileNotFoundError(f"Dictionary file not found: {DICT_PATH}")

    client = SarvamAI(api_subscription_key=api_key)

    with open(DICT_PATH, "rb") as f:
        result = client.pronunciation_dictionary.create(file=f)

    print("Dictionary upload result:")
    print(result)

    dict_id = (
        getattr(result, "dictionary_id", None)
        or getattr(result, "dict_id", None)
        or getattr(result, "id", None)
    )

    if dict_id:
        print("\nAdd this to .env and Railway variables:")
        print(f"SARVAM_PRONUNCIATION_DICT_ID={dict_id}")
    else:
        print("\nCould not automatically find dictionary ID.")
        print("Inspect the printed result above and copy the dictionary ID manually.")


if __name__ == "__main__":
    main()