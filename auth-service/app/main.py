from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import httpx

app = FastAPI()

# Environment variables (configure in docker-compose)
CLIENT_ID = "your-client-id"
REDIRECT_URI = "http://localhost:8000/callback"
FHIR_AUTH_URL = "https://fhir-server/auth"
FHIR_TOKEN_URL = "https://fhir-server/token"

@app.get("/login")
async def login():
    return RedirectResponse(
        f"{FHIR_AUTH_URL}?response_type=code&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}&scope=patient/*.read"
    )

@app.get("/callback")
async def callback(code: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            FHIR_TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "code": code,
                "client_id": CLIENT_ID,
                "redirect_uri": REDIRECT_URI
            }
        )
    return response.json()