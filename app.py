import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"


if __name__ == "__main__":
    if os.environ['SUPERSET_ENV'] == 'production':
        app.run(host='0.0.0.0', port=80)
    else:
        app.run(host='0.0.0.0', port=80, debug=True)
