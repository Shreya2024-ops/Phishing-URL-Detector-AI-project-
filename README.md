# Phishing URL Detector 🔐

An AI-powered tool to detect phishing URLs using FastAPI and Gemini Pro API.

## Features
- Detects if a URL is phishing using keyword analysis
- Gemini AI provides an explanation of risk
- REST API with `/check-url` endpoint

## How to Run
1. Clone repo
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Add `.env` file with your `GEMINI_API_KEY`
4. Run server:
   ```
   uvicorn app.main:app --reload
   ```

## Built by: Kumari Shreya 💻