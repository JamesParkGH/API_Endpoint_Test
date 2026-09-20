# Membership Color API

A small FastAPI service that maps membership numbers to colors.

## Run locally

```bash
cd "/Users/jamesparkgh/Desktop/JamesCode/Zoom/API Playground/API_Endpoint_Test"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The endpoint is available at `http://localhost:8000/membership`.

## Membership lookup with GET

Use the `input` query parameter when the customer gives a membership number:

```text
GET /membership?input=1111  -> {"input":"1111","color":"red"}
GET /membership?input=2222  -> {"input":"2222","color":"blue"}
GET /membership?input=3333  -> {"input":"3333","color":"yellow"}
```

Unknown values return `"color":"unknown"`.

## JavaScript agent example

```javascript
async function main () {
  const membership = var_get("membership");

  const response = await req.get(
    `https://YOUR-TUNNEL-URL.loca.lt/membership?input=${encodeURIComponent(membership)}`
  );

  const result = response.data;
  log.info(`Membership ${result.input} maps to ${result.color}`);

  // Use result.color in the next routing decision.
}
```

If your platform exposes the response body directly rather than under `data`, use `response` instead of `response.data`.

## Create a public URL

Keep the API running in one Terminal:

```bash
python3 -m uvicorn app:app --host 0.0.0.0 --port 8000
```

In another Terminal, create a free temporary HTTPS tunnel:

```bash
npx localtunnel --port 8000
```

Use the URL it prints in the Zoom JavaScript. Both processes must remain running, and the tunnel URL may change when restarted.
