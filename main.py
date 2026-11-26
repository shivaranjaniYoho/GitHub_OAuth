
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = FastAPI()

CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

REDIRECT_URI = "http://localhost:8000/callback"


@app.get("/")
def home():
    return {"message": "GitHub OAuth Login Application"}


@app.get("/login")
def login():
    github_url = (
        "https://github.com/login/oauth/authorize"
        f"?client_id={CLIENT_ID}"
        "&scope=read:user user:email"
    )
    return RedirectResponse(github_url)


@app.get("/callback")
def callback(code: str):
    token_url = "https://github.com/login/oauth/access_token"

    response = requests.post(
        token_url,
        data={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "code": code,
        },
        headers={"Accept": "application/json"}
    )

    token_data = response.json()

    access_token = token_data.get("access_token")

    if not access_token:
        return {"error": "Unable to get access token", "details": token_data}

    return {"message": "GitHub Login Successful!", "access_token": access_token}
