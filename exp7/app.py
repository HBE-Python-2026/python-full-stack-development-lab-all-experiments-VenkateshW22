# Experiment 7: Introduction to Flask
# TODO: NOTE: (Students must create templates/profile.html themselves)
from flask import Flask, render_template

app = Flask(__name__)

# 1. Home Route
@app.route('/')
def home():
    # TODO: Return the string "Welcome to the Home Page!"
    pass

# 2. Dynamic Route
# TODO: Create a route '/profile/<username>'
def profile(username):
    # TODO: Render the template 'profile.html' and pass 'username' as the 'name' variable
    pass

if __name__ == '__main__':
    app.run(debug=True)