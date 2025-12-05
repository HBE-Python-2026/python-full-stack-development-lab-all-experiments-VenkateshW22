# Experiment 10: REST API with Flask
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
tasks = [
    {"id": 1, "title": "Learn Python"},
    {"id": 2, "title": "Learn Flask"}
]
next_id = 3

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    # TODO: Return the 'tasks' list as JSON using jsonify
    pass

@app.route('/api/tasks', methods=['POST'])
def create_task():
    global next_id
    # Validation (Given)
    if not request.json or not 'title' in request.json:
        return jsonify({"error": "Bad Request"}), 400

    # TODO: Get 'title' from request.json
    # TODO: Create a new task dictionary with 'id' (next_id) and 'title'
    # TODO: Append new task to 'tasks' list
    # TODO: Increment next_id
    # TODO: Return the new task as JSON with status code 201
    pass

if __name__ == '__main__':
    app.run(debug=True)