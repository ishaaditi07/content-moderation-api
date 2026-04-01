from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Content Moderation API")

# Input schema
class TextInput(BaseModel):
    text: str

# Basic word list (you can expand later)
bad_words = ["idiot", "stupid", "hate", "dumb", "fool"]

# Home route
@app.get("/")
def home():
    return {"message": "AI Content Moderation API is running"}

# Profanity detection
@app.post("/profanity")
def profanity(input: TextInput):
    text = input.text.lower()
    result = any(word in text for word in bad_words)
    return {"profanity": result}

# Toxicity detection
@app.post("/toxicity")
def toxicity(input: TextInput):
    text = input.text.lower()
    
    if "hate" in text or "kill" in text:
        return {"toxicity": "toxic"}
    else:
        return {"toxicity": "clean"}

# Safety check
@app.post("/safe")
def safe(input: TextInput):
    text = input.text.lower()
    is_bad = any(word in text for word in bad_words)
    
    return {"safe": not is_bad}

# Combined moderation endpoint (BEST ONE)
@app.post("/moderate")
def moderate(input: TextInput):
    text = input.text.lower()

    is_profane = any(word in text for word in bad_words)
    is_toxic = "hate" in text or "kill" in text

    return {
        "safe": not (is_profane or is_toxic),
        "profanity": is_profane,
        "toxicity": is_toxic,
        "message": "Unsafe content detected" if (is_profane or is_toxic) else "Content is safe"
    }