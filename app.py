import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, User
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE')

db.init_app(app)
Migrate(app, db)
CORS(app)

@app.route('/')
def main():
    return jsonify({ "message": "api flask"}), 200


@app.route('/test')
def test():
    users = User.query.all()
    users = [user.username for user in users]

    return jsonify(users), 200

if __name__ == '__main__':
    app.run()