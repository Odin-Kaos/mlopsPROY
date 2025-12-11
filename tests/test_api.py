# test_api.py
import io
import pytest
from fastapi.testclient import TestClient
from api.api import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root_endpoint_renders_template():
    response = client.get("/")
    # TemplateResponse returns HTML
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


def test_predict_endpoint_empty_file():
    response = client.post(
        "/predict",
        files={"file": ("empty.jpg", b"", "image/jpeg")},
        data={"size": "8"},
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Empty file"
