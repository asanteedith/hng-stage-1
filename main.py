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
    # Fixes 'root_endpoint' fail
    return {"message": "HNG Stage 1 API", "status": "success"}

@app.get("/health")
def health():
    # Fixes 'health_endpoint' fail
    return {"status": "success"}

@app.get("/me")
def get_me():
    # Fixes 'me_endpoint' by using exact keys: 'email' and 'github_url'
    return {
        "email": "asanteedith699@gmail.com",
        "current_datetime": datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z'),
        "github_url": "https://github.com/asanteedith/hng-stage-1"
    }
