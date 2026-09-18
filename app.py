import os
from typing import Optional

from fastapi import FastAPI, Header, HTTPException, Query
from pydantic import BaseModel

app = FastAPI(title="Membership Color API", version="1.0.0")

MEMBERSHIP_COLORS = {
    "1111": "red",
    "2222": "blue",
    "3333": "yellow",
}


class MembershipResponse(BaseModel):
    input: str
    color: str


def check_api_key(api_key: Optional[str]) -> None:
    expected_api_key = os.getenv("ROUTING_API_KEY")
    if expected_api_key and api_key != expected_api_key:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/membership", response_model=MembershipResponse)
@app.get("/route", response_model=MembershipResponse)
def membership_route(
    input_value: str = Query(..., alias="input"),
    x_api_key: Optional[str] = Header(default=None),
) -> MembershipResponse:
    check_api_key(x_api_key)

    normalized_input = input_value.strip()
    return MembershipResponse(
        input=normalized_input,
        color=MEMBERSHIP_COLORS.get(normalized_input, "unknown"),
    )
