package com.mapvoice.android.network

import com.google.gson.annotations.SerializedName

data class CompareRequest(
    val instruction: String
)

// This matches your current FastAPI response:
// original_audio_url + normalized_audio_url.
// The app labels original_audio_url as "Raw Audio" in the UI.
data class CompareResponse(
    @SerializedName("original_text")
    val originalText: String,

    @SerializedName("normalized_text")
    val normalizedText: String,

    @SerializedName("speech_text")
    val speechText: String,

    @SerializedName("raw_audio_url")
    val rawAudioUrl: String,

    @SerializedName("normalized_audio_url")
    val normalizedAudioUrl: String
)


