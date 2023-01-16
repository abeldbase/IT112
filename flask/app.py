from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "<p>This is my Application!</p>"


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/fortune")
def fortune():
    return render_template("fortune.html")


@app.route('/data/', methods=['POST'])
def data():
    if method == 'POST':
        fortune_data = fortune
        return render_template('data.html', fortune_data=fortune_data)


if __name__ == "__main__":
    app.run()
