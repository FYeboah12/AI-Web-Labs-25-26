import random
from flask import Flask, render_template

app = Flask(__name__)
'''Addiction generator 🙂.
Create a page where the visitor can click on a link for a chance to win. 
There will be three routes in this site ( /home, /gamble, and /stats )
This link always goes to the same route:  /gamble (or equivalent)
Sometimes you win, sometimes you don’t. The win/lose decision is determined randomly by the server before the page is rendered. 
Make two templates (one for if you win, one for if you lose). Render the appropriate template
On the stats page you can see the tally of wins and losses
If a user visits /stats before gambling, display 0 wins and 0 losses instead of an error.
Wins and losses do not need to persist when the server restarts
'''
stats_dict = {"wins": 0, "losses": 0}

@app.route("/")
def idefeault():
    return "/home"

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/gamble")
def gamble():
    global stats_dict
    odds = random.randint(1,100)
    if odds <= 75:
        stats_dict["losses"] += 1
        return render_template("loss.html", num = odds)
    else:
        stats_dict["wins"] += 1
        return render_template("win.html", num = odds)
    
@app.route("/stats")
def stats():
    return render_template("stats.html", stats = stats_dict)

if __name__ == "__main__":
    app.run(debug=True)