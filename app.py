from flask import Flask, Response
from cli import generate_toml

app = Flask(__name__)
app.config.from_object("config.BaseConfig")

@app.route("/")
def index():
    content = generate_toml()

    # Supposed to be application/toml, but would rather it render in browser
    # instead of downloading file.
    # See: https://github.com/toml-lang/toml/issues/465#issuecomment-364506403
    return Response(content, mimetype="text/toml")

if __name__ == "__main__":
    app.run()
