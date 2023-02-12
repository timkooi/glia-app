import pytest
from starlette.testclient import TestClient
from app.main import app, reset_audit_queue

@pytest.fixture()
def test_app():
    client = TestClient(app)
    reset_audit_queue()
    yield client