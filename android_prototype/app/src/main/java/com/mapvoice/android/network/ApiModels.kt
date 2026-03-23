package com.mapvoice.android.network

data class CompareRequest (
    val instruction: String
)

data class CompareResponse (
    val original_text: String,
    val normalized_text: String,
    val original_audio_url: String,
    val normalized_audio_url: String
)
