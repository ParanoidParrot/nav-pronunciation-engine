# MapVoice

**MapVoice** is a navigation pronunciation engine that improves the pronunciation of Indian street names in GPS navigation systems.

This project demonstrates how mixed-language street names (e.g., English + Indian languages) can be normalized and converted into natural-sounding speech for navigation instructions.

## Repository

`nav-pronunciation-engine`

## Problem

Navigation systems often mispronounce Indian street names due to:

- abbreviations (Rd, Dr, St)
- mixed-language tokens
- transliterated names
- acronyms (BDA, NIT)

Example:

Google Maps instruction:

Turn right onto **Dr Rajkumar Rd**

Typical pronunciation:

"Turn right onto **D-R Rajkumar R-D**"

MapVoice output:

"Turn right onto **Doctor Rajkumar Road**"

## System Architecture