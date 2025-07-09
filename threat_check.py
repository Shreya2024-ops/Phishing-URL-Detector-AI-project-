def check_phishing(url: str) -> bool:
    suspicious_keywords = ["login", "verify", "update", "secure", "bank", "account", "paypal"]
    for word in suspicious_keywords:
        if word in url.lower():
            return True
    return False