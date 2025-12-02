# AI-Based-App-or-Game-Code-Generator-n8n

This project is an AI-driven Python application/game code generator built using n8n workflow automation and Google Gemini.
Users can send instructions via a webhook, and the system automatically returns fully executable Python code that builds either a web app (Streamlit), desktop app (Tkinter), or game (Pygame) depending on the request.

🚀 Key Features

🔗 Webhook API endpoint to receive dynamic user requests

🤖 AI Agent using Google Gemini to generate structured executable Python code

🎮 Automatically supports Streamlit / Tkinter / Pygame

🕹 Game restart (R key) and quit (Q key) built-in functionality for generated games

🛡 Ensures safe environment by preventing unsafe imports and external API calls

⚙️ Runs without modification — ready-to-execute output

🧪 How to Use

1.Import the provided .json workflow file into n8n

2.Configure Google Gemini API Key

3.Activate the workflow

4.Copy the webhook URL generated

5.Send a POST request with JSON

6.Get AI-generated responses in real-time


💡 Possible Use Cases

1.AI-powered code generation tools

2.Game or app builders

3.Developer assistants

4.Automation and workflow learning projects

