import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

def generate_images(prompt: str, layout: str = "default") -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API Error: {e}"