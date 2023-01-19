from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return "<p>This is my Application!</p>"


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/fortune', methods=['GET', 'POST'])
def fortune():
    if request.method == 'POST':
        return f"Hi {request.form.get('name')}. You have selected {request.form.get('color')} &  {request.form.get('number')}"
    return render_template('fortune_form.html')


if __name__ == "__main__":
    app.run()
