from app.core.security import hash_password, verify_password
from fastapi.testclient import TestClient

from app.main import app

# Test app health check functionality

client = TestClient(app)

def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy"
    }

# Test password hashing and verification functionality

def test_password_hash_is_different_from_password():
    password = "MySecurePassword123!"

    hashed_password = hash_password(password)

    assert hashed_password != password


def test_password_verification_succeeds():
    password = "MySecurePassword123!"

    hashed_password = hash_password(password)

    assert verify_password(
        password,
        hashed_password,
    )


def test_password_verification_fails():
    password = "MySecurePassword123!"
    wrong_password = "WrongPassword123!"

    hashed_password = hash_password(password)

    assert not verify_password(
        wrong_password,
        hashed_password,
    )