from fastapi import FastAPI
from app.routes.url_check import router as url_router

app = FastAPI(title="Phishing URL Detector by Shreya")

app.include_router(url_router)