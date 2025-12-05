import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../exp08')))
from app import app, db, Entry

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' # Use RAM DB
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_add_guest(client):
    # Simulate submitting the form
    client.post('/', data={'guest_name': 'Tester'})

    # Check if saved to DB
    with app.app_context():
        entry = Entry.query.filter_by(guest_name='Tester').first()
        assert entry is not None, "Guest was not saved to database"