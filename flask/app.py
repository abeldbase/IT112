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
        if color == "yellow":

            if number == "1":
                return f"Hola {request.form.get('user')} You are very lucky!! Happy today!"

            elif number == "2":
                return f"Hola {request.form.get('user')}You will become a reach person  soon!"

            elif number == "3":
                return f"Hola {request.form.get('user')}You will get a new job next year!"

            else:
                number == "4"
            return f"Hola {request.form.get('user')}You will visit Paris after 2 years!"

        if color == "red":
            if number == "1":
                return f"Hola {request.form.get('user')} You are beautiful"

            elif number == "2":
                return f"Hola {request.form.get('user')}You will become a actor soon!"

            elif number == "3":
                return f"Hola {request.form.get('user')}You will get a new babey  next year!"

            else:
                number == "4"
            return f"Hola {request.form.get('user')}You will visit Africa after 6 month!"

        if color == "blue":

            if number == "1":
                return f"Hola {request.form.get('user')}Keep calm  Happy today!"

            elif number == "2":
                return f"Hola {request.form.get('user')}You will become a runner soon!"

            elif number == "3":
                return f"Hola {request.form.get('user')}You will get a a new friend next year in Bejing !"

            else:
                number == "4"
            return f"Hola {request.form.get('user')} Tokyo will be your seconf home!"

        if color == "green":

            if number == "1":
                return f"Hola {request.form.get('user')} You are alive!"

            elif number == "2":
                return f"Hola {request.form.get('user')}You will be famouse !"

            elif number == "3":
                return f"Hola {request.form.get('user')}You will get exta job remotely next year!"

            else:
                number == "4"
            return f"Hola {request.form.get('user')}You will go to WH to meet POTUS!"

        return f"Hi {request.form.get('name')}. You have selected {request.form.get('color')} &  {request.form.get('number')}"
    return render_template('fortune_form.html')


if __name__ == "__main__":
    app.run()
