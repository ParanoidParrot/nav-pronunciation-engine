from fastapi.responses import HTMLResponse


def get_demo_html() -> HTMLResponse:
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MapVoice Demo</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 860px;
                margin: 40px auto;
                padding: 0 16px;
                line-height: 1.5;
            }
            textarea, button {
                width: 100%;
                box-sizing: border-box;
                margin-top: 8px;
                margin-bottom: 16px;
                padding: 10px;
                font-size: 16px;
            }
            button {
                cursor: pointer;
            }
            .card {
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 16px;
                margin-top: 20px;
            }
            .section-title {
                margin-top: 0;
            }
            code {
                white-space: pre-wrap;
                word-break: break-word;
            }
            audio {
                width: 100%;
                margin-top: 8px;
            }
        </style>
    </head>
    <body>
        <h1>MapVoice Demo</h1>
        <p>Paste a navigation instruction and compare raw vs normalized TTS output.</p>

        <label for="instruction">Navigation instruction</label>
        <textarea id="instruction" rows="4">Turn left onto NH 44 after 500m near Hosakerehalli</textarea>

        <button onclick="compareAudio()">Normalize + Generate Audio</button>

        <div class="card">
            <h3 class="section-title">Normalized Output</h3>
            <code id="normalizedText">Waiting...</code>
        </div>

        <div class="card">
            <h3 class="section-title">Raw Audio</h3>
            <p><strong>Original text:</strong></p>
            <code id="originalText">Waiting...</code>
            <audio id="rawAudio" controls></audio>
        </div>

        <div class="card">
            <h3 class="section-title">Normalized Audio</h3>
            <p><strong>Normalized text:</strong></p>
            <code id="normalizedTextAudio">Waiting...</code>
            <audio id="normalizedAudio" controls></audio>
        </div>

        <script>
            async function compareAudio() {
                const instruction = document.getElementById("instruction").value;
                const normalizedText = document.getElementById("normalizedText");
                const originalText = document.getElementById("originalText");
                const normalizedTextAudio = document.getElementById("normalizedTextAudio");
                const rawAudio = document.getElementById("rawAudio");
                const normalizedAudio = document.getElementById("normalizedAudio");

                normalizedText.textContent = "Loading...";
                originalText.textContent = "Loading...";
                normalizedTextAudio.textContent = "Loading...";
                rawAudio.removeAttribute("src");
                normalizedAudio.removeAttribute("src");

                try {
                    const response = await fetch("/demo/compare", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ instruction })
                    });

                    const data = await response.json();

                    normalizedText.textContent = data.normalized_text;
                    originalText.textContent = data.original_text;
                    normalizedTextAudio.textContent = data.normalized_text;

                    rawAudio.src = data.original_audio_url;
                    normalizedAudio.src = data.normalized_audio_url;

                    rawAudio.load();
                    normalizedAudio.load();
                } catch (err) {
                    normalizedText.textContent = "Error: " + err.message;
                    originalText.textContent = "Error";
                    normalizedTextAudio.textContent = "Error";
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)