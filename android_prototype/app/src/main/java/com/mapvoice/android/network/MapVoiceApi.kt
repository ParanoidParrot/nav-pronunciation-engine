package com.mapvoice.android.network

import retrofit2.http.Body
import retrofit2.http.Post

interface MapVoiceApi {
    @POST("demo/compare")
    suspend fun compareAudio (
        @Body request: CompareRequest
    ) : CompareResponse
}