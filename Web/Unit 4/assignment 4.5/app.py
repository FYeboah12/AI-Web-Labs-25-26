import re

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def default():
    return "404 not found in the system 404 new era era"

@app.route("/<exclude>")
def getExcludedWords(exclude):
    #this is the words to pass through the gray
    word_list = open("enable1.txt").read().splitlines()
    pattern = r"^[^" + exclude + r"]{5}$"
    words = [word for word in word_list if re.match(pattern, word.strip())]
    return words

@app.route("/getwords/<guess>")
def wordle(guess):
    pairs = [(guess[i], guess[i + 1]) for i in range(0, len(guess), 2)]
    return jsonify(pairs)

# 8 is green
# 7 is yellow
# 0 is gray
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
