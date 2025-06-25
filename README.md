# MoodDecode API 🧠

A FastAPI service powered by Google's Gemini Pro that analyzes text for emotions, detects mental health crises, and provides summaries.

## Features
- Emotion detection from text (`/analyze_mood`)
- Mental health crisis detection (`/detect_crisis`)
- Text summarization (`/summarize`)

## API Reference
View the working:  
[https://mooddecode-1.onrender.com/docs](https://mooddecode-1.onrender.com/docs)

## Tech Stack
- **Framework**: FastAPI
- **AI Model**: Gemini Pro
- **Deployment**: Render
- **Language**: Python 3.10

## Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install fastapi uvicorn python-dotenv google-generativeai
