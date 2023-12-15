# Przy pierwszym uruchomieniu:  flask --app app shell
# A następnie:
# >>> db.create_all()
# >>> exit()
#
# Dalej uruchamiamy: flask --app app run
import sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class create_tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tagname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.tag


def get_tag(session):
    return session.query(create_tag).all()


def create_tag(name, session):
    user = create_tag(username=name)
    session.add(user)
    session.commit()


@app.route('/')
def hello():
    return render_template('form.html', data=get_users(db.session),
                           tytul="Użytkownicy", no_error=True)


@app.route('/add')
def add_tag():
    args = request.args
    create_tag(args["name"], db.session)

    return render_template('form.html', data=get_tag(db.session),
                           tytul="Dodano użytkownika")
