from fastapi.testclient import TestClient
from app.main import app

def test_read_main(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Tim's Glia API"}

def test_post_jumble(test_app):
    response = test_app.post("/jumble", json={"word": "test"})
    assert response.status_code == 200
    jumbled_word = response.json().get("jumbled_word")
    assert jumbled_word != "test"
    assert len(jumbled_word) == len("test")

def test_post_jumble_one_character(test_app):
    response = test_app.post("/jumble", json={"word": "a"})
    assert response.status_code == 200
    jumbled_word = response.json().get("jumbled_word")
    assert jumbled_word == "a"

def test_post_jumble_empty_string(test_app):
    response = test_app.post("/jumble", json={"word": ""})
    assert response.status_code == 200
    jumbled_word = response.json().get("jumbled_word")
    assert jumbled_word == ""

def test_audit_no_payload(test_app):
    response = test_app.get("/audit")
    assert response.status_code == 200
    assert response.json() == [{'endpoint': '/audit', 'payload': {}}]

def test_audit_with_payload(test_app):
    test_app.post("/jumble", json={"word": "test"})
    response = test_app.get("/audit")
    assert response.status_code == 200
    assert response.json() == [{'endpoint': '/jumble', 'payload': {"word": "test"}}, {'endpoint': '/audit', 'payload': {}}]

def test_audit_only_10_items(test_app):
    for x in range(15):
        test_app.get("/")
        test_app.get("/audit")
    response = test_app.get("/audit")
    assert response.status_code == 200
    assert len(response.json()) == 10
