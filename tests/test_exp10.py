import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../exp10')))
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks(client):
    rv = client.get('/api/tasks')
    assert rv.status_code == 200
    assert b"id" in rv.data

def test_create_task(client):
    new_task = {'title': 'Autograding Task'}
    rv = client.post('/api/tasks', json=new_task)
    assert rv.status_code == 201
    assert b"Autograding Task" in rv.data