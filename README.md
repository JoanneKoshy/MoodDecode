🧠 MoodDecode API
MoodDecode is a FastAPI-based NLP web API that uses Google's Gemini Pro to analyze user-inputted text for emotion detection, mental health crisis signals, and summarization.

🚀 Live Demo
Base URL:
https://mooddecode-1.onrender.com

📌 Endpoints
🔹 POST /analyze_mood
Description:
Analyzes the emotion expressed in a given sentence. Returns a single word emotion (like happy, sad, angry).

Input (JSON):

json
Copy
Edit
{
  "text": "I'm feeling really down today."
}
Output (JSON):

json
Copy
Edit
{
  "emotion": "sad"
}
🔹 POST /detect_crisis
Description:
Detects if the given text indicates a mental health crisis or suicidal statement.

Input (JSON):

json
Copy
Edit
{
  "text": "I can't take this anymore."
}
Output (JSON):

json
Copy
Edit
{
  "crisis_detected": true
}
🔹 POST /summarize
Description:
Summarizes a long text into 1–2 sentences using Gemini's summarization ability.

Input (JSON):

json
Copy
Edit
{
  "text": "Today was a really exhausting day. I had back-to-back classes and assignments due, but I managed to push through everything."
}
Output (JSON):

json
Copy
Edit
{
  "summary": "Despite a hectic schedule filled with classes and assignments, the speaker successfully managed their day."
}
🧠 Model/API Used
Google Generative AI API

Model: gemini-pro

Library: google.generativeai

API Calls: generate_content(prompt)

Note: Requires Google AI API Key

🛠️ Tech Stack
Framework: FastAPI

LLM: Gemini Pro

Deployment: Render

Language: Python 3.10

CORS: Enabled for all origins

📦 Requirements
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Your requirements.txt should include:

nginx
Copy
Edit
fastapi
uvicorn
python-dotenv
google-generativeai
📁 Environment Variables
Create a .env file in the root directory:

ini
Copy
Edit
GEMINI_API_KEY=your_google_api_key_here
🖥️ Hosting Platform
🌐 Hosted on Render

👩‍💻 Author
Name: Joanne Alice Thomas

GitHub: JoanneKoshy

Email: joannealicethomas@gmail.com

