from flask import Flask
from random import randint
from flask import render_template


app = Flask(__name__)




@app.get("/")
def home():
    return "<h1>Hello, World!<h1>"


@app.get("/random/")
def random():
    return str(randint(1,  1000))


@app.get("/about/")
def about():
    return "<h1>Hello, World!<h1>"