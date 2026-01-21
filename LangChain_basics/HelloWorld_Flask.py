# a simple application sets up a web server that responds with "Hello, World!" when accessing the root URL using Flask.
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
    