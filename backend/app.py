from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origin='http://localhost:3000/')  # Enable CORS for all routes

@app.route('/')
def hello_world():
    return jsonify(
        {
            "names": [
                "name1",
                "name2",
                "name3"
            ]
        }
    )

if __name__ == '__main__':
    app.run(debug=True)
