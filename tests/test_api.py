def test_register_user(client):
    response = client.post(
        "/api/v1/auth/register",
        json={
            "email": "testuser@example.com",
            "password": "securepassword123",
            "full_name": "Test User",
            "phone_number": "770000000",
            "role": "merchant_owner",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "testuser@example.com"
    assert "id" in data


def test_login_user(client):
    response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "testuser@example.com",
            "password": "securepassword123",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_create_merchant_and_transaction(client):
    # 1. Login to get token
    login_res = client.post(
        "/api/v1/auth/login",
        json={"email": "testuser@example.com", "password": "securepassword123"},
    )
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Create merchant
    merchant_res = client.post(
        "/api/v1/merchants/",
        headers=headers,
        json={"business_name": "Test Store", "tax_id": "12345", "currency": "XOF"},
    )
    assert merchant_res.status_code == 201
    merchant_id = merchant_res.json()["id"]

    # 3. Create transaction
    tx_res = client.post(
        "/api/v1/transactions",
        headers=headers,
        json={
            "merchant_id": merchant_id,
            "amount": 5000,
            "currency": "XOF",
            "provider": "wave",
        },
    )
    assert tx_res.status_code == 201
    tx_data = tx_res.json()
    assert tx_data["status"] == "pending"

    # 4. Trigger payment webhook
    webhook_res = client.post(
        "/api/v1/webhooks/payment-callback",
        json={
            "transaction_id": tx_data["id"],
            "provider_tx_id": "WAVE_TEST_123",
            "status": "completed",
        },
    )
    assert webhook_res.status_code == 200
    assert webhook_res.json()["status"] == "completed"