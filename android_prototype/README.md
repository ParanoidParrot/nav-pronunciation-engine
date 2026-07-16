# MapVoice Android Prototype

Native Android MVP for MapVoice.

## What it does

- Calls the MapVoice backend endpoint `POST /demo/compare`
- Shows original and normalized navigation text
- Plays raw and normalized Sarvam TTS audio

## How to run

1. Open this folder in Android Studio:

```text
android_prototype
```

2. Let Gradle sync.

3. Confirm `BASE_URL` in `app/build.gradle.kts` points to your deployed Railway backend:

```kotlin
"https://nav-pronunciation-engine-production.up.railway.app/"
```

4. Run on an Android emulator or physical Android phone.

## Backend response expected

This Android code currently expects your existing backend response fields:

```json
{
  "original_text": "...",
  "normalized_text": "...",
  "speech_text":"...",
  "raw_audio_url": "/audio/...wav",
  "normalized_audio_url": "/audio/...wav"
}
```
