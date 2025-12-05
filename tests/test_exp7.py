import pytest
from exp7_app import app # Import student's Flask app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    # Test Homepage [cite: 546]
    rv = client.get('/')
    assert b"Welcome" in rv.data

def test_dynamic_profile(client):
    # Test Dynamic Route [cite: 547]
    rv = client.get('/profile/Alice')
    assert b"Hello, Alice" in rv.data