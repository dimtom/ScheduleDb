import flask

app = flask.Flask(__name__)


@app.route("/")
def handler_main():
    return "<p>Hello, world!</p>"


@app.route("/help")
def handler_help():
    return "<p>This is help page</p>"


@app.route("/login")
def handler_login():
    return "<p>This is login page</p>"


@app.route("/logout")
def handler_logout():
    return "<p>This is logout page</p>"
