from flask import Flask, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def main():
    return jsonify({ "message": "api flask"}), 200

if __name__ == '__main__':
    app.run()