from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "<p>This is my Application!</p>"


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        return "show fortune"
    return render_template('fortune.html')


if __name__ == "__main__":
    app.run()
