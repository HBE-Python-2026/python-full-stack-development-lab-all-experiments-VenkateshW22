# Experiment 8: Flask with SQLite
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///guestbook.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 1. Define Model
class Entry(db.Model):
    # TODO: Define 'id' column (Integer, Primary Key)
    # TODO: Define 'guest_name' column (String, Not Null)
    pass

# 2. Main Route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # TODO: Get 'guest_name' from request.form
        # TODO: Create a new Entry object
        # TODO: Add to db session and commit
        # TODO: Redirect back to 'index'
        pass

    # GET request
    # TODO: Query all entries from the database
    # TODO: Render 'index.html' and pass the entries
    return "Render Template Here"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)