# Call Routing API

A small FastAPI service for routing a call from a variable collected by a JavaScript call-routing agent.

## Run locally

```bash
cd "/Users/jamesparkgh/Desktop/JamesCode/Zoom/API Playground"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The endpoint is available at `http://localhost:8000/route` and interactive API documentation is at `http://localhost:8000/docs`.

## Membership lookup with GET

Use the `input` query parameter when the customer gives a membership number:

```text
GET /membership?input=1111  -> {"input":"1111","color":"red"}
GET /membership?input=2222  -> {"input":"2222","color":"blue"}
GET /membership?input=3333  -> {"input":"3333","color":"yellow"}
```

`GET /route?input=1111` is also supported. Unknown values return `"color":"unknown"`.

## JavaScript agent example

```javascript
async function main () {
  const membership = var_get("membership");

  const response = await req.get(
    `https://YOUR-PUBLIC-DOMAIN.com/membership?input=${encodeURIComponent(membership)}`
  );

  const result = response.data;
  log.info(`Membership ${result.input} maps to ${result.color}`);

  // Use result.color in the next routing decision.
}
```

If your platform exposes the response body directly rather than under `data`, use `response` instead of `response.data`.

To require an API key, set `ROUTING_API_KEY`. Then send it as the `X-API-Key` header from the agent.

## Deploy for Zoom Virtual Agent

1. Push this folder to a GitHub repository.
2. In Render, create a new Blueprint and select that repository. The included `render.yaml` creates the service.
3. Render will provide a public URL such as `https://call-routing-api.onrender.com`.
4. Replace `https://YOUR-PUBLIC-DOMAIN.com` in the JavaScript with that Render URL.

Zoom cannot reach `localhost`; the Zoom request must use the deployed HTTPS URL.
