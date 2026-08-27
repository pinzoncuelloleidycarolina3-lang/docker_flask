from app import app as flask_app


def test_ejemplo_basico():
    assert 1 + 1 == 2  # nosec B101


def test_home_status():
    client = flask_app.test_client()
    response = client.get('/')
    assert response.status_code == 200  # nosec B101