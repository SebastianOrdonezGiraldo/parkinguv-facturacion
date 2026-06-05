from fastapi import FastAPI, HTTPException

from parkinguv.billing import calculate_fee

app = FastAPI(title="ParkingUV Billing API")


@app.get("/")
def root():
    return {
        "name": "ParkingUV Billing API",
        "status": "ok",
        "docs": "/docs",
        "health": "/health",
        "calculate": "/calculate",
    }


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
