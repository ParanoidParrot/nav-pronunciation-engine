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
                max-width: 760px;
                margin: 40px auto;
                padding: 0 16px;
                line-height: 1.5;
            }
            textarea, input, button {
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
            code {
                white-space: pre-wrap;
                word-break: break-word;
            }
        </style>
    </head>
    <body>
        <h1>MapVoice Demo</h1>
        <p>Paste a navigation instruction and see the normalized output.</p>

        <label for="instruction">Navigation instruction</label>
        <textarea id="instruction" rows="4">Turn left onto NH 44 after 500m near Hosakerehalli</textarea>

        <button onclick="normalizeText()">Normalize</button>

        <div class="card">
            <h3>Normalized Output</h3>
            <code id="result">Waiting...</code>
        </div>

        <script>
            async function normalizeText() {
                const instruction = document.getElementById("instruction").value;
                const resultBox = document.getElementById("result");
                resultBox.textContent = "Loading...";

                try {
                    const response = await fetch("/normalize", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({ instruction })
                    });

                    const data = await response.json();
                    resultBox.textContent = data.normalized || JSON.stringify(data, null, 2);
                } catch (err) {
                    resultBox.textContent = "Error: " + err.message;
                }
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html)