package com.mapvoice.android.ui

import android.content.Context
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.input.KeyboardCapitalization
import androidx.compose.ui.unit.dp
import com.mapvoice.android.network.CompareRequest
import com.mapvoice.android.network.CompareResponse
import com.mapvoice.android.network.RetrofitClient
import com.mapvoice.android.player.AudioPlayer
import kotlinx.coroutines.launch

@Composable
fun MapVoiceScreen(context: Context) {
    val scope = rememberCoroutineScope()
    val player = remember { AudioPlayer(context) }

    var input by remember {
        mutableStateOf("Turn left onto NH 44 after 500m near Hosakerehalli")
    }
    var loading by remember { mutableStateOf(false) }
    var error by remember { mutableStateOf<String?>(null) }
    var result by remember { mutableStateOf<CompareResponse?>(null) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp)
    ) {
        Text("MapVoice Android Prototype", style = MaterialTheme.typography.headlineSmall)

        OutlinedTextField(
            value = input,
            onValueChange = { input = it },
            modifier = Modifier.fillMaxWidth(),
            label = { Text("Navigation instruction") },
            keyboardOptions = KeyboardOptions(
                capitalization = KeyboardCapitalization.Sentences
            ),
            minLines = 3
        )

        Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
            Button(
                onClick = {
                    loading = true
                    error = null
                    result = null

                    scope.launch {
                        try {
                            result = RetrofitClient.api.compareAudio(
                                CompareRequest(instruction = input)
                            )
                        } catch (e: Exception) {
                            error = e.message ?: "Unknown error"
                        } finally {
                            loading = false
                        }
                    }
                }
            ) {
                Text("Normalize + Generate Audio")
            }
        }

        if (loading) {
            CircularProgressIndicator()
        }

        error?.let {
            Text("Error: $it", color = MaterialTheme.colorScheme.error)
        }

        result?.let { response ->
            Card(modifier = Modifier.fillMaxWidth()) {
                Column(modifier = Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
                    Text("Original", style = MaterialTheme.typography.titleMedium)
                    Text(response.original_text)

                    Text("Normalized", style = MaterialTheme.typography.titleMedium)
                    Text(response.normalized_text)

                    Row(horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                        Button(onClick = {
                            player.play(buildAbsoluteUrl(response.raw_audio_url))
                        }) {
                            Text("Play Raw")
                        }

                        Button(onClick = {
                            player.play(buildAbsoluteUrl(response.normalized_audio_url))
                        }) {
                            Text("Play Normalized")
                        }
                    }
                }
            }
        }
    }
}

private fun buildAbsoluteUrl(path: String): String {
    val base = com.mapvoice.android.BuildConfig.BASE_URL.removeSuffix("/")
    return if (path.startsWith("http")) path else "$base$path"
}