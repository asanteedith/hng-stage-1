from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    # Exactly as required by instructions
    return {"message": "API is running"}

@app.get("/health")
def health():
    # Exactly as required by instructions
    return {"message": "healthy"}

@app.get("/me")
def get_me():
    # Exactly as required by instructions: includes name and uses 'github' key
    return {
        "name": "Edith Asante",
        "email": "asanteedith699@gmail.com",
        "github": "https://github.com/asanteedith",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    }
