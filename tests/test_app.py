from fastapi.testclient import TestClient

from app.main import app
from app.safety import detect_crisis

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_index_serves_html():
    r = client.get("/")
    assert r.status_code == 200
    assert "Sukoon" in r.text


def test_chat_rejects_empty():
    assert client.post("/api/chat", json={"messages": []}).status_code == 422


def test_chat_rejects_assistant_last():
    r = client.post("/api/chat", json={"messages": [{"role": "assistant", "content": "hi"}]})
    assert r.status_code == 400


def test_crisis_detection():
    assert detect_crisis("I want to die")
    assert detect_crisis("khudkushi ka khayal aata hai")
    assert not detect_crisis("I had a stressful day at work")
