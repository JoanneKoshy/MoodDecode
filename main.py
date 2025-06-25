from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI(title="MoodDecode with Gemini")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up Gemini model with chat
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

class TextInput(BaseModel):
    text: str

@app.post("/analyze_mood")
async def analyze_mood(input: TextInput):
    try:
        prompt = f"What is the emotion in this sentence? Reply with one word like happy, sad, angry, etc.\nSentence: {input.text}"
        chat = model.start_chat()
        response = chat.send_message(prompt)
        mood = response.text.strip()
        return {"emotion": mood.lower()}
    except Exception as e:
        return {"error": str(e)}

@app.post("/detect_crisis")
async def detect_crisis(input: TextInput):
    try:
        prompt = f"Is this a mental health crisis? Respond only with true or false.\nText: {input.text}"
        chat = model.start_chat()
        response = chat.send_message(prompt)
        result = response.text.strip().lower()
        return {"crisis_detected": result == "true"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/summarize")
async def summarize(input: TextInput):
    try:
        prompt = f"Summarize the following text in 1–2 sentences:\n\n{input.text}"
        chat = model.start_chat()
        response = chat.send_message(prompt)
        summary = response.text.strip()
        return {"summary": summary}
    except Exception as e:
        return {"error": str(e)}
