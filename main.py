from fastapi import FastAPI, Request
import requests

app = FastAPI()

MODASH_API_KEY = "UaxcWljkGvMdnvCLzrar2kR7s2guLm3a"

@app.post("/modash")
async def query_modash(request: Request):
    body = await request.json()
    query = body.get("query", "")

    response = requests.get(
        "https://api.modash.io/v1/creators/search",
        headers={"Authorization": f"Bearer {MODASH_API_KEY}"},
        params={"search": query, "limit": 5}
    )

    data = response.json()
    return {"influencers": data}
