def is_dangerous(text: str) -> bool:
    dangerous_keywords = [
        "suicide","kill myself","end my life","hurt myself",
        "self-harm","cut myself","want to die","can't live"
    ]
    text_lower = text.lower()
    return any(k in text_lower for k in dangerous_keywords)
