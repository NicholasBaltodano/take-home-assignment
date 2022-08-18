from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    _rl = response.url
    url = _rl.split("/")[2]

    print(url)
    assert response.status_code == 200
    assert response.json() == {"Welcome to the Monte Carlo Interview Challenge! Please head over to {url}docs for API documentation"}

def test_good_metric():
    response = client.get("/metric/BTCUSD")
    assert response.status_code == 200

def test_good_metric_lower():
    response = client.get("/metric/btcusd")
    assert response.status_code == 200

def test_bad_metric():
    response = client.get("/metric/bxxxxxxd")
    assert response.status_code == 422