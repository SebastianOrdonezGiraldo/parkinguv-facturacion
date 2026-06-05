from fastapi import FastAPI, HTTPException

from parkinguv.billing import calculate_fee

app = FastAPI(title="ParkingUV Billing API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/calculate")
def calculate(minutes: int, vip: bool = False):
    try:
        total = calculate_fee(minutes, vip=vip)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"minutes": minutes, "vip": vip, "total": total}
