
from flask import Flask, flash, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request


app = Flask(__name__)


# data is a Python dict
data = {"it112": 25, "it121": 18}


@app.get('/api/courses')
def courses():
    # send HTTP response with content-type: application/json
    return jsonify(data)


app.run(host='0.0.0.0', port=81)


# create a 'student' class that maps to a db table


@property
def serialized(self):
    """Return object data in easily serializable format"""
    return {
        'id': self.id,
        'name': self.name,
        'city': self.city
    }


@app.route('/api/students')
def api_students():
    # return db query results as a JSON list
    return jsonify([student.serialized for student in Student.query.all()])


@app.post('/api/course')
def add_course():
    # normally we would validate the submission before adding to our list
    data.update(request.get_json())
    return '', 204


@app.post('/api/student')
def add_student():
    # normally we would validate the submission before adding to our list
    data = request.get_json()
    try:
        student = Student(name=data['name'], city=data['city'])
        db.session.add(student)
        db.session.commit()
        return jsonify({"status": "success"})
    except Exception:
        return app.response_class(response={"status": "failure"},
                                  status=500,
                                  mimetype='application/json')


# set URI for the database to be used
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'

# associate a SQLAlchemy object with the Flask app
db = SQLAlchemy(app)

# create a 'student' class that maps to a db table


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    major = db.Column(db.String(50))

    def __repr__(self):
        return '<Student %r>' % self.name. email. major


# create / use the database
with app.app_context():
    db.create_all()


# student1 = Student(name='Neil deGrasse Tyson',email='neil@harvard.edu', major='astrophysics')
# student2 = Student(name='Nikole Hannah Jones', email='nikole@howard.edu', major='journalism')
# student3 = Student(name='Abel Sharon Dale', email='abel@howard.edu', major='PSIR')
# db.session.add(student1)
# db.session.add(student2)
# db.session.add(student3)
# db.session.commit()
# students = Student.query.all()
# student = Student.query.filter_by(id=2).first()
# students = Student.query.all()
# student = Student.query.filter_by(id=2).first()


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
# Create a Flask route to show a list of all items in your database


@app.route('/show_all')
def show_all():
    return render_template('show_all.html', students=Student.query.all())


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['email'] or not request.form['email']:
            flash('Please enter all the fields', 'error')
        else:
            student = student(request.form['name'], request.form['major'],
                              request.form['major'], request.form['major'])

            db.session.add(student)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html', student=Student.query.filter_by(id=2).first())


@app.get('/api/courses')
def courses():
    # send HTTP response with content-type: application/json
    return jsonify(data)


app.run(host='0.0.0.0', port=81)


if __name__ == "__main__":
    app.run()
