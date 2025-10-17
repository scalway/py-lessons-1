from flask import Flask, render_template, redirect, url_for
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import secrets
import os
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)

STUDENTS_FILE = 'students.json'

def load_students():
    if not os.path.exists(STUDENTS_FILE):
        return []

    with open(STUDENTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_students(students) -> None:
    with open(STUDENTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

class StudentForm(FlaskForm):
    first_name = StringField('imie', validators=[DataRequired()])
    last_name = StringField('nazwisko', validators=[DataRequired()])
    class_name = StringField('klasa', validators=[DataRequired()])

    submit = SubmitField('Dodaj')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='lista uczniow', students=load_students())

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = StudentForm()
    if form.validate_on_submit():
        students = load_students()



        ids = [s['id'] for s in students]    # refaktoryzaca . cmd+ alt + v
        max_id = max(ids, default=0) + 1
        new_student = {
            'id': max_id,
            'first_name': form.first_name.data,
            'class_name': form.class_name.data,
            'last_name': form.last_name.data,
        }

        students.append(new_student)
        save_students(students)

        return redirect(url_for('index'))
    else:
        return render_template('add_student.html',title='dodaj ucznia', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    students = load_students()
    rest_students = [s for s in students if s['id'] != id]
    save_students(rest_students)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)