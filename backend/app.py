from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    obj = {'numbers': [1, 2, 3, 4]}
    return obj

if __name__ == '__main__':
    app.run(debug=True)