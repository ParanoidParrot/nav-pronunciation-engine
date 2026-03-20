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

| Python | FastAPI, data processing |
| OpenStreetMap | Geospatial data |
| Sarvam AI | Text-to-Speech | 


## How to Run
-  Setup environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Install dependencies
```bash
python -m pip install -r requirements.txt
```

- Run demo
```bash
python -m scripts.voice_demo
```

Audio files will be generated in:
scripts/audio_outputs/



## Audio Comparison

MapVoice can generate before / after speech samples for the same navigation instruction:

- **Raw**: original navigation text
- **Normalized**: text after MapVoice expansion and suffix-aware processing

Try it out: [TryItHere](https://nav-pronunciation-engine-production.up.railway.app/demo)


## Key Highlights

- Data-driven linguistic modeling using real map data
- Handles Indian multilingual naming patterns
- Improves TTS without modifying the speech model
- Modular pipeline (normalization → parsing → TTS)

## Future Work

- Multi-language script injection (e.g, Kannada, Hindi, Tamil)
- Route playback simulation (real-time navigation)
- Before vs after pronunciation comparison engine
- Expanded linguistic lexicon with regional metadata
- Android / iOS prototype integration



## System Architecture

```mermaid
flowchart TD 
    A[Raw Navigation Instruction] --> B[Tokenizer] 
    B --> C[Rule-based Normalizer]
     C --> D[Number & Distance Expansion] 
     D --> E[Abbreviation Expansion] 
     E --> F[Suffix Detector] 
     F --> G[Word Splitter] 
     G --> H[Phonetic-friendly Text] 
     H --> I[Sarvam TTS Engine] 
     I --> J[Audio Output] 
     
     %% Data pipeline 
     K[OpenStreetMap India Dataset] --> L[Named Road Extraction] 
     L --> M[Suffix Mining]
     M --> N[Suffix Cleaning & Clustering] 
     N --> O[Lexicon Builder] 
     O --> P[lexicon.json] 
     P --> F