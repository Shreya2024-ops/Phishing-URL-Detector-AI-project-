from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.threat_check import check_phishing
from app.services.ai_explain import explain_risk

router = APIRouter()

class URLInput(BaseModel):
    url: str

@router.post("/check-url")
def check_url(data: URLInput):
    url = data.url

    try:
        is_phishing = check_phishing(url)
        explanation = explain_risk(url, is_phishing)

        return {
            "url": url,
            "is_phishing": is_phishing,
            "explanation": explanation
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))