import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/roll/<num_sides>")
def roll_sides(num_sides):
    try:
        sides = int(num_sides)
        result = [random.randint(1, sides)]
        return render_template("roll.htm", val=result, sides = sides, dice = 1)
    except ValueError:
        return "error with input", 400
    
@app.route("/roll/<num_sides>/<num_dice>")
def roll_multi_die(num_sides,num_dice):
    try:
        sides = int(num_sides)
        dice = int(num_dice)
        result = [random.randint(1, sides) for _ in range(dice)]
        return render_template("roll.htm", val=result, sides=sides, dice=dice)
    except ValueError:
        return "error with input", 400

if __name__ == "__main__":
    app.run(debug=True)
