from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root_endpoint():

    return {"status": "success", "message": "HNG Stage 1 API"}

@app.get("/me")
def me_endpoint():

    return {
        "email": "asanteedith699@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/asanteedith/hng-stage-1"
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
