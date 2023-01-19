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
        color = request.form.get('color')
        number = request.form.get('number')
        if color == 'Yellow':

            if number == 1:
                return f"Hola {request.form.get('user')} You are very lucky!! Happy today!"

            elif number == 2:
                return f"Hola {request.form.get('user')} You will become a reach person  soon!"
            elif number == 3:
                return f"Hola {request.form.get('user')}You will get a new job next year!"

            elif number == 4:
                return f"Hola {request.form.get('user')}You will visit Paris after 2 years!"
            else:
                print("Numbers - 1, 2, 3, 4 are the only numbers allowed!")
        return f"Hi {request.form.get('name')}. You have selected {request.form.get('color')} &  {request.form.get('number')}"
    return render_template('fortune_form.html')


if __name__ == "__main__":
    app.run()
