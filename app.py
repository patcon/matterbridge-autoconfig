from flask import Flask

app = Flask(__name__)

@app.route("/")
def generate():
    return "Helo world!"
