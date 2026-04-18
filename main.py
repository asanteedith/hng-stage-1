from fastapi import FastAPI

app = FastAPI()

@app.get("/me")
def read_me():
    return {
        "email": "asanteedith699@gmail.com",
        "current_datetime": "2026-04-18T00:41:28Z", 
        "github_url": "https://github.com/asanteedith/hng-stage-1"
    }
