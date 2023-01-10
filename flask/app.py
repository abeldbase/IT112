from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "<p>This is my Application!</p>"


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()
