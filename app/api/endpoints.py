from fastapi import FastAPI, HTTPException
from app.core.calculator import calculate


app = FastAPI()


@app.get("/health")
def health_check():
    return {"STATUS": "OK"}


@app.get("/calculate")
def calculate_endpoint(a: int, b: int, op: str = '+'):
    try:
        result = calculate(a, b, op)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
