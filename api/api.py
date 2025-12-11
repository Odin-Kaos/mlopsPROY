# lab1/api/api.py
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pathlib import Path

import torch
from torchvision.io import decode_image

from Lab1.mylib.model import predict, rescale

app = FastAPI(title="MLOps Lab1 API")

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/predict")
async def predict_class(
    file: UploadFile = File(...),
    size: str | None = Form(None),
):
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Empty file")

    image = decode_image(torch.ByteTensor(list(content)))
    size = int(size)
    if size > 0:
        image = rescale(image, int(size))
    predicted = predict(image)

    return JSONResponse(
        {
            "predicted_class": predicted,
            "processed_size": {"width": size, "height": size},
        }
    )


@app.get("/health")
def health():
    return {"status": "ok"}
