from fastapi import FastAPI
from datetime import datetime, timezone
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    # Strict match for root_endpoint
    return {"message": "HNG Stage 1 API", "status": "success"}

@app.get("/health")
def health():
    # Strict match for health_endpoint
    return {"status": "success"}

@app.get("/me")
def get_me():
    # Strict match for me_endpoint keys
    return {
        "email": "asanteedith699@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'),
        "github_url": "https://github.com/asanteedith/hng-stage-1"
    }
