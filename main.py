from flask import Flask
from faker import Faker
import requests
import random
import string


app = Flask(__name__)


def generate_users(num):
    fake = Faker()
    tmp_str = ""
    for _ in range(num):
        tmp_str += fake.first_name() + " " + fake.email() + "<br/>"
    return tmp_str


def password_generate(len):
    tmp_str = "".join(random.choice(string.printable) for _ in range(len))
    return tmp_str


def num_of_astro():
    tmp_json_req = requests.get("http://api.open-notify.org/astros.json").json()
    tmp_str = str(tmp_json_req["number"])
    return tmp_str


@app.route("/users/generate")
@app.route("/users/generate/<int:num>")
def users(num=20):
    return generate_users(num)


@app.route("/password/generate")
@app.route("/password/generate/<int:len>")
def password(len=8):
    return password_generate(len)


@app.route("/astro")
def astro():
    return num_of_astro()
