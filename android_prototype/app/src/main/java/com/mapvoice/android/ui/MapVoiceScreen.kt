package com.mapvoice.android.ui

import android.content.Context
import android.content.Intent
import android.net.Uri
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.imePadding
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.statusBarsPadding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.ButtonDefaults
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ElevatedCard
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.OutlinedTextFieldDefaults
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Brush
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.KeyboardCapitalization
import androidx.compose.ui.unit.dp
import com.mapvoice.android.network.CompareRequest
import com.mapvoice.android.network.CompareResponse
import com.mapvoice.android.network.RetrofitClient
import com.mapvoice.android.player.AudioPlayer
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

private val Bg = Color(0xFF111827)
private val BgSoft = Color(0xFF1F2937)
private val CardBg = Color(0xFF1F2937)
private val CardBorder = Color(0x33D1D5DB)
private val Accent = Color(0xFFA7C957)
private val AccentSoft = Color(0xFFCDE990)
private val TextPrimary = Color(0xFFF9FAFB)
private val TextMuted = Color(0xFFD1D5DB)
private val ErrorRed = Color(0xFFFB7185)

private data class SampleInstruction(
    val label: String,
    val instruction: String
)

@OptIn(ExperimentalLayoutApi::class)
@Composable
fun MapVoiceScreen(context: Context) {
    val scope = rememberCoroutineScope()
    val scrollState = rememberScrollState()
    val player = remember { AudioPlayer(context) }

    var input by remember {
        mutableStateOf("Turn left onto NH 44 after 500m near MG Marg")
    }

    var loading by remember { mutableStateOf(false) }
    var error by remember { mutableStateOf<String?>(null) }
    var result by remember { mutableStateOf<CompareResponse?>(null) }

    val sampleInstructions = listOf(
        SampleInstruction(
            label = "Hindi · MG Marg",
            instruction = "Continue to MG Marg"
        ),
        SampleInstruction(
            label = "Kannada · Hosakerehalli",
            instruction = "Turn left after 500m to Hosakerehalli"
        ),
        SampleInstruction(
            label = "Tamil · Anna Salai",
            instruction = "Take the next right near Anna Salai"
        ),
        SampleInstruction(
            label = "Telugu · Ameerpet Veedhi",
            instruction = "Continue towards Ameerpet Veedhi"
        ),
        SampleInstruction(
            label = "Marathi · Shivaji Peth",
            instruction = "Head towards Shivaji Peth"
        ),
        SampleInstruction(
            label = "Bengali · Rabindra Sarani",
            instruction = "Continue to Rabindra Sarani"
        ),
        SampleInstruction(
            label = "Gujarati · Manek Chowk",
            instruction = "Turn right after 100m near Manek Chowk"
        )
    )

    LaunchedEffect(result) {
        if (result != null) {
            delay(250)
            scrollState.animateScrollTo(scrollState.maxValue)
        }
    }

    DisposableEffect(Unit) {
        onDispose {
            player.stop()
        }
    }

    Surface(
        modifier = Modifier.fillMaxSize(),
        color = Bg
    ) {
        Box(
            modifier = Modifier
                .fillMaxSize()
                .background(
                    brush = Brush.radialGradient(
                        colors = listOf(
                            Accent.copy(alpha = 0.16f),
                            Bg
                        ),
                        radius = 900f
                    )
                )
        ) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .statusBarsPadding()
                    .navigationBarsPadding()
                    .imePadding()
                    .verticalScroll(scrollState)
                    .padding(20.dp),
                verticalArrangement = Arrangement.spacedBy(18.dp)
            ) {
                HeaderSection(context = context)

                DemoInputCard(
                    input = input,
                    onInputChange = {
                        input = it
                        error = null
                    },
                    sampleInstructions = sampleInstructions,
                    onSampleClick = { sample ->
                        input = sample.instruction
                        result = null
                        error = null
                    },
                    loading = loading,
                    onGenerateClick = {
                        scope.launch {
                            loading = true
                            error = null
                            result = null
                            player.stop()

                            try {
                                result = RetrofitClient.api.compareAudio(
                                    CompareRequest(instruction = input)
                                )
                            } catch (e: Exception) {
                                error = e.message ?: "Something went wrong"
                            } finally {
                                loading = false
                            }
                        }
                    }
                )

                if (loading) {
                    LoadingCard()
                }

                error?.let {
                    ErrorCard(message = it)
                }

                AnimatedVisibility(visible = result != null) {
                    result?.let { response ->
                        ResultSection(
                            response = response,
                            onPlayRaw = {
                                player.play(buildAbsoluteUrl(response.rawAudioUrl))
                            },
                            onPlayNormalized = {
                                player.play(buildAbsoluteUrl(response.normalizedAudioUrl))
                            },
                            onStop = {
                                player.stop()
                            }
                        )
                    }
                }

                FooterNote()

                Spacer(modifier = Modifier.height(12.dp))
            }
        }
    }
}

@Composable
private fun HeaderSection(context: Context) {
    Column(verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(10.dp)
        ) {
            Box(
                modifier = Modifier
                    .clip(RoundedCornerShape(12.dp))
                    .background(
                        Brush.linearGradient(
                            colors = listOf(AccentSoft, Accent)
                        )
                    )
                    .padding(horizontal = 10.dp, vertical = 8.dp),
                contentAlignment = Alignment.Center
            ) {
                Text(
                    text = "MV",
                    color = Bg,
                    fontWeight = FontWeight.Black
                )
            }

            Text(
                text = "MapVoice",
                color = TextPrimary,
                style = MaterialTheme.typography.titleLarge,
                fontWeight = FontWeight.Bold
            )
        }

        Text(
            text = "Make Indian place names sound more speech-friendly.",
            color = TextPrimary,
            style = MaterialTheme.typography.headlineMedium,
            fontWeight = FontWeight.ExtraBold
        )

        Text(
            text = "MapVoice normalizes navigation-style instructions, expands road abbreviations, applies Indian place-name pronunciation hints, and sends the speech-friendly text to Sarvam AI Text-to-Speech for raw vs normalized audio comparison.",
            color = TextMuted,
            style = MaterialTheme.typography.bodyMedium
        )


        Button(
            onClick = { openApiDocs(context) },
            colors = ButtonDefaults.buttonColors(
                containerColor = Color.White.copy(alpha = 0.08f),
                contentColor = TextPrimary
            ),
            modifier = Modifier
                .border(1.dp, CardBorder, CircleShape)
                .clip(CircleShape)
        ) {
            Text("API Docs")
        }
    }
}

private fun openApiDocs(context: Context) {
    val url = com.mapvoice.android.BuildConfig.BASE_URL.removeSuffix("/") + "/docs"
    val intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
    context.startActivity(intent)
}

@Composable
private fun TagPill(text: String) {
    Box(
        modifier = Modifier
            .border(1.dp, CardBorder, CircleShape)
            .clip(CircleShape)
            .background(Color.White.copy(alpha = 0.05f))
            .padding(horizontal = 12.dp, vertical = 8.dp)
    ) {
        Text(
            text = text,
            color = AccentSoft,
            style = MaterialTheme.typography.labelMedium,
            fontWeight = FontWeight.SemiBold
        )
    }
}

@OptIn(ExperimentalLayoutApi::class)
@Composable
private fun DemoInputCard(
    input: String,
    onInputChange: (String) -> Unit,
    sampleInstructions: List<SampleInstruction>,
    onSampleClick: (SampleInstruction) -> Unit,
    loading: Boolean,
    onGenerateClick: () -> Unit
) {
    ElevatedCard(
        modifier = Modifier
            .fillMaxWidth()
            .border(1.dp, CardBorder, RoundedCornerShape(24.dp)),
        shape = RoundedCornerShape(24.dp),
        colors = CardDefaults.elevatedCardColors(
            containerColor = CardBg
        )
    ) {
        Column(
            modifier = Modifier.padding(18.dp),
            verticalArrangement = Arrangement.spacedBy(14.dp)
        ) {
            Text(
                text = "Live pronunciation demo",
                color = TextPrimary,
                style = MaterialTheme.typography.titleLarge,
                fontWeight = FontWeight.Bold
            )

            Text(
                text = "Pick a sample or enter your own navigation instruction.",
                color = TextMuted,
                style = MaterialTheme.typography.bodyMedium
            )

            OutlinedTextField(
                value = input,
                onValueChange = onInputChange,
                modifier = Modifier.fillMaxWidth(),
                label = {
                    Text("Navigation instruction")
                },
                minLines = 3,
                enabled = !loading,
                keyboardOptions = KeyboardOptions(
                    capitalization = KeyboardCapitalization.Sentences
                ),
                colors = OutlinedTextFieldDefaults.colors(
                    focusedTextColor = TextPrimary,
                    unfocusedTextColor = TextPrimary,
                    disabledTextColor = TextMuted,
                    focusedBorderColor = Accent,
                    unfocusedBorderColor = CardBorder,
                    focusedLabelColor = AccentSoft,
                    unfocusedLabelColor = TextMuted,
                    cursorColor = Accent,
                    focusedContainerColor = BgSoft,
                    unfocusedContainerColor = BgSoft,
                    disabledContainerColor = BgSoft
                )
            )

            Text(
                text = "Try a sample",
                color = TextPrimary,
                style = MaterialTheme.typography.titleMedium,
                fontWeight = FontWeight.SemiBold
            )

            FlowRow(
                horizontalArrangement = Arrangement.spacedBy(8.dp),
                verticalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                sampleInstructions.forEach { sample ->
                    TextButton(
                        onClick = { onSampleClick(sample) },
                        enabled = !loading,
                        modifier = Modifier
                            .border(1.dp, CardBorder, CircleShape)
                            .clip(CircleShape)
                            .background(Color.White.copy(alpha = 0.04f)),
                        colors = ButtonDefaults.textButtonColors(
                            contentColor = AccentSoft
                        )
                    ) {
                        Text(sample.label)
                    }
                }
            }

            Button(
                onClick = onGenerateClick,
                enabled = !loading && input.isNotBlank(),
                modifier = Modifier.fillMaxWidth(),
                colors = ButtonDefaults.buttonColors(
                    containerColor = Accent,
                    contentColor = Bg,
                    disabledContainerColor = CardBorder,
                    disabledContentColor = TextMuted
                )
            ) {
                Text(
                    text = if (loading) "Generating..." else "Normalize + Generate Audio",
                    fontWeight = FontWeight.Bold
                )
            }
        }
    }
}

@Composable
private fun LoadingCard() {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .border(1.dp, CardBorder, RoundedCornerShape(20.dp)),
        shape = RoundedCornerShape(20.dp),
        colors = CardDefaults.cardColors(
            containerColor = CardBg
        )
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            horizontalArrangement = Arrangement.spacedBy(12.dp),
            verticalAlignment = Alignment.CenterVertically
        ) {
            CircularProgressIndicator(
                color = Accent,
                strokeWidth = 3.dp
            )

            Text(
                text = "Generating raw and normalized speech...",
                color = TextMuted
            )
        }
    }
}

@Composable
private fun ErrorCard(message: String) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .border(1.dp, ErrorRed.copy(alpha = 0.5f), RoundedCornerShape(20.dp)),
        shape = RoundedCornerShape(20.dp),
        colors = CardDefaults.cardColors(
            containerColor = Color(0xFF2A121A)
        )
    ) {
        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            Text(
                text = "Error",
                color = ErrorRed,
                fontWeight = FontWeight.Bold
            )

            Text(
                text = message,
                color = TextPrimary
            )
        }
    }
}

@Composable
private fun ResultSection(
    response: CompareResponse,
    onPlayRaw: () -> Unit,
    onPlayNormalized: () -> Unit,
    onStop: () -> Unit
) {
    Column(verticalArrangement = Arrangement.spacedBy(14.dp)) {
        ResultCard(
            title = "Original",
            body = response.originalText
        )

        ResultCard(
            title = "Normalized",
            body = response.normalizedText
        )

        ResultCard(
            title = "Speech Text",
            body = response.speechText
        )

        ElevatedCard(
            modifier = Modifier
                .fillMaxWidth()
                .border(1.dp, CardBorder, RoundedCornerShape(24.dp)),
            shape = RoundedCornerShape(24.dp),
            colors = CardDefaults.elevatedCardColors(
                containerColor = CardBg
            )
        ) {
            Column(
                modifier = Modifier.padding(18.dp),
                verticalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                Text(
                    text = "Audio comparison",
                    color = TextPrimary,
                    style = MaterialTheme.typography.titleLarge,
                    fontWeight = FontWeight.Bold
                )

                Text(
                    text = "Play raw audio first, then normalized audio to hear the difference.",
                    color = TextMuted,
                    style = MaterialTheme.typography.bodyMedium
                )

                Button(
                    onClick = onPlayRaw,
                    modifier = Modifier.fillMaxWidth(),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = Color.White.copy(alpha = 0.10f),
                        contentColor = TextPrimary
                    )
                ) {
                    Text("Play Raw Audio")
                }

                Button(
                    onClick = onPlayNormalized,
                    modifier = Modifier.fillMaxWidth(),
                    colors = ButtonDefaults.buttonColors(
                        containerColor = Accent,
                        contentColor = Bg
                    )
                ) {
                    Text(
                        text = "Play Normalized Audio",
                        fontWeight = FontWeight.Bold
                    )
                }

                TextButton(
                    onClick = onStop,
                    modifier = Modifier.fillMaxWidth(),
                    colors = ButtonDefaults.textButtonColors(
                        contentColor = TextMuted
                    )
                ) {
                    Text("Stop Audio")
                }
            }
        }
    }
}

@Composable
private fun ResultCard(
    title: String,
    body: String
) {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .border(1.dp, CardBorder, RoundedCornerShape(20.dp)),
        shape = RoundedCornerShape(20.dp),
        colors = CardDefaults.cardColors(
            containerColor = CardBg
        )
    ) {
        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            Text(
                text = title.uppercase(),
                color = AccentSoft,
                style = MaterialTheme.typography.labelLarge,
                fontWeight = FontWeight.Bold
            )

            Text(
                text = body,
                color = TextPrimary,
                style = MaterialTheme.typography.bodyLarge
            )
        }
    }
}

@Composable
private fun FooterNote() {
    Card(
        modifier = Modifier
            .fillMaxWidth()
            .border(1.dp, CardBorder, RoundedCornerShape(20.dp)),
        shape = RoundedCornerShape(20.dp),
        colors = CardDefaults.cardColors(
            containerColor = CardBg
        )
    ) {
        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(6.dp)
        ) {
            Text(
                text = "Speech synthesis",
                color = AccentSoft,
                style = MaterialTheme.typography.labelLarge,
                fontWeight = FontWeight.Bold
            )

            Text(
                text = "Powered by Sarvam AI Text-to-Speech. MapVoice adds normalization, abbreviation expansion, suffix splitting and pronunciation hints before generating speech.",
                color = TextMuted,
                style = MaterialTheme.typography.bodySmall
            )
        }
    }
}

private fun buildAbsoluteUrl(path: String): String {
    val base = com.mapvoice.android.BuildConfig.BASE_URL.removeSuffix("/")
    return if (path.startsWith("http")) path else "$base$path"
}