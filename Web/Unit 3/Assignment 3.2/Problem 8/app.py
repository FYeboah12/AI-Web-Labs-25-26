from datetime import datetime
from math import inf
import random

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
""" /ask, /yes, /no, /maybe"""


@app.route("/")
def index():
    return redirect(url_for("ask"))

@app.route("/ask")
def ask():
    answers = ["yes","no","maybe"]
    random_answer = random.randint(0,2)
    return redirect(url_for(answers[random_answer]))

@app.route("/yes")
def yes():
    return render_template("index.htm", answer="yes")

@app.route("/no")
def no():
    return render_template("index.htm", answer="no") 

@app.route("/maybe")
def maybe():
    return render_template("index.htm", answer="maybe")

if __name__ == "__main__":
    app.run(debug=True)
