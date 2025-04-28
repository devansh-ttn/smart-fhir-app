from fastapi import FastAPI, Header, HTTPException
import httpx

app = FastAPI()
FHIR_BASE_URL = "https://fhir-server/baseR4/"

@app.get("/{resource}")
async def proxy(resource: str, authorization: str = Header(...)):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{FHIR_BASE_URL}{resource}",
            headers={"Authorization": authorization}
        )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code)
    return response.json()