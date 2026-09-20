from fastapi import FastAPI, Query

app = FastAPI(title="Membership Color API", version="1.0.0")

MEMBERSHIP_COLORS = {"1111": "red", "2222": "blue", "3333": "yellow", "4444": "green"}


@app.get("/membership")
def membership_route(
    input_value: str = Query(..., alias="input"),
) -> dict[str, str]:
    normalized_input = input_value.strip()
    return {
        "input": normalized_input,
        "color": MEMBERSHIP_COLORS.get(normalized_input, "unknown"),
    }
