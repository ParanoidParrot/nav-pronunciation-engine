# MapVoice

**MapVoice** is a navigation pronunciation engine that improves the pronunciation of Indian street names in GPS navigation systems.

This project demonstrates how mixed-language street names (e.g., English + Indian languages) can be normalized and converted into natural-sounding speech for navigation instructions. The system transforms raw navigation instructions into speech-friendly text before generating audio. Aim is to improve TTS output for Indian place names by combining:

- map-derived linguistic data
- suffix-aware normalization
- word splitting
- speech synthesis using Sarvam AI



## Problem

Navigation systems often mispronounce Indian street names due to:

- abbreviations (Rd, Dr, St)
- mixed-language tokens
- transliterated names
- acronyms (BDA, NIT)


## Tech Stack

Python (FastAPI, data processing)

OpenStreetMap (geospatial data)

Sarvam AI (Text-to-Speech)

Regex + rule-based NLP

## How to Run
1. Setup environment
python3 -m venv .venv
source .venv/bin/activate
2. Install dependencies
python -m pip install -r requirements.txt
3. Run demo
python -m scripts.voice_demo


Audio files will be generated in:
scripts/audio_outputs/


# Key Highlights

- Data-driven linguistic modeling using real map data

- Handles Indian multilingual naming patterns

- Improves TTS without modifying the speech model

- Modular pipeline (normalization → parsing → TTS)

# Future Work

Multi-language script injection (e.g, Kannada, Hindi, Tamil)

Route playback simulation (real-time navigation)

Before vs after pronunciation comparison engine

Expanded linguistic lexicon with regional metadata

Android / iOS prototype integration



## System Architecture