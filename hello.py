from flask import Flask
#MY FLASK APP
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
