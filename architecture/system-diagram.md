# MapVoice System Diagram

## Overview

MapVoice is a navigation pronunciation engine that improves TTS output for Indian place names by combining:

- map-derived linguistic data
- suffix-aware normalization
- word splitting
- speech synthesis using Sarvam AI

The system transforms raw navigation instructions into speech-friendly text before generating audio.

---

## End-to-End Flow

```mermaid
flowchart TD
    A[Raw Navigation Instruction] --> B[Tokenizer]
    B --> C[Rule-based Normalizer]
    C --> D[Distance / Number Expansion]
    D --> E[Road / Highway Expansion]
    E --> F[Suffix Detector]
    F --> G[Word Splitter]
    G --> H[Normalized Speech-friendly Text]
    H --> I[Sarvam TTS Engine]
    I --> J[Generated Audio Output]