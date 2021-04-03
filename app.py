from faker import Faker
from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


fake = Faker()


app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<User %r>" % self.name


db.create_all()
db.session.commit()


@app.route("/")
def home():
    return "Welcome Home!"


@app.route("/users/all")
def users_all():
    users = User.query.all()
    tmp_users = [dict(id=user.user_id, name=user.name, email=user.email) for user in users]
    return jsonify(tmp_users)


@app.route("/users/gen")
def users_gen():
    usr = User(name=fake.name(), email=fake.email())
    db.session.add(usr)
    db.session.commit()
    return redirect(url_for("users_all"))


@app.route("/users/delete-all")
def users_del_all():
    User.query.delete()
    db.session.commit()
    return redirect(url_for("users_all"))


@app.route("/users/count")
def users_count():
    tmp_int = User.query.count()
    return jsonify({"count": tmp_int})


@app.route("/users/add", methods=["GET", "POST"])
def users_add():
    if request.method == "GET":
        return render_template("user_add.html")
    else:
        name = request.form["user_name"]
        email = request.form["email"]
    usr = User(name=name, email=email)
    db.session.add(usr)
    db.session.commit()
    return redirect(url_for("users_all"))
