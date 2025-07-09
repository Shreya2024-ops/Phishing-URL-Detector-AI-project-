from gemini_api import generate_images

def explain_risk(url: str, is_phishing: bool) -> str:
    if is_phishing:
        prompt = f"Explain why this URL might be a phishing link: {url}"
    else:
        prompt = f"This URL seems safe: {url}. Give a short explanation."

    return generate_images(prompt)