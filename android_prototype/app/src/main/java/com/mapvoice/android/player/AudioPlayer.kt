package com.mapvoice.android.player

import android.content.Context
import android.media.AudioAttributes
import android.media.MediaPlayer
import android.net.Uri

class AudioPlayer(private val context: Context) {
    private var mediaPlayer: MediaPlayer? = null

    fun play(url: String, onError: (String) -> Unit = {}) {
        stop()

        try {
            mediaPlayer = MediaPlayer().apply {
                setAudioAttributes(
                    AudioAttributes.Builder()
                        .setUsage(AudioAttributes.USAGE_MEDIA)
                        .setContentType(AudioAttributes.CONTENT_TYPE_SPEECH)
                        .build()
                )

                setDataSource(context, Uri.parse(url))
                setOnPreparedListener { it.start() }
                setOnCompletionListener { stop() }
                setOnErrorListener { _, what, extra ->
                    stop()
                    onError("Audio playback failed. what=$what extra=$extra")
                    true
                }
                prepareAsync()
            }
        } catch (e: Exception) {
            stop()
            onError(e.message ?: "Audio playback failed")
        }
    }

    fun stop() {
        mediaPlayer?.let {
            try {
                if (it.isPlaying) {
                    it.stop()
                }
            } catch (_: Exception) {
                // Ignore release-time state issues.
            }
            it.release()
        }
        mediaPlayer = null
    }
}
