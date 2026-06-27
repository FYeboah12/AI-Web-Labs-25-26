from operator import le
import re

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def wordle():
    return render_template("index.htm")


@app.route("/returnWords/<exclude>/<yellow>/<green>")
def getExcludedWords(exclude,yellow,green):
    # gray is fine, just exclude
    lettersGiven = exclude + yellow + green
    word_list = open("enable1.txt").read().splitlines()
    pattern = r"^[^" + exclude + r"]{5}$"
    words = [word for word in word_list if re.match(pattern, word.strip())]
    if yellow != "404":
        index_yellows = [(int(yellow[i]), yellow[i + 1]) for i in range(0, len(yellow), 2)]
        for y in index_yellows:
            words = [word for word in words if y[1] in word and word[y[0]] != y[1] and lettersGiven.count(y[1]) == word.count(y[1])]
    if green != "404":
        index_greens = [(int(green[i]), green[i + 1]) for i in range(0, len(green), 2)]
        for g in index_greens:
            words = [word for word in words if word[g[0]] == g[1] and lettersGiven.count(g[1]) == word.count(g[1])]

    # words = [word for g in index_greens for word in words if word[g[0]] == g[1]]
    # words = [word for y in index_yellows for word in words if y[1] in word and word[y[0]] != y[1]]

    return words


@app.route("/getwords/<guess>")
def guessWord(guess):
    # guess = [{h:yellow},{e:green},{l:gray},{l:gray},{o:yellow}]
    #check for multiple letters, use enumerate!
    guess = guess[1:-1]
    guess = guess.split(",")
    print(guess)
    yellows = [(ind,y[2]) for ind,y in enumerate(guess) if "yellow" in y]
    excludes = [x for x in guess if "gray" in x]
    excludes = [e[2] for e in excludes]
    greens = [(ind, g[2]) for ind,g in enumerate(guess) if "green" in g]
    #[exclude],[yellows],[greens]
    return jsonify((yellows,excludes,greens))


# 8 is green
# 7 is yellow
# 0 is gray
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
