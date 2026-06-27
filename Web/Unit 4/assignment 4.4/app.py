from flask import Flask
import re
app = Flask(__name__)

@app.route("/")
def default():
    return "404 not found in the system 404 new era era"

@app.route("/<exclude>")
def wordle(exclude):
    # regex pattern: /^(?![a])\w{5}$/gm
    #list comp to exclude letters found in var exclude
    # pattern =  r"^\w(?![" + exclude + r"]){5}$"
    word_list = open("enable1.txt").read().splitlines()
    pattern = r"^[^" + exclude + r"]{5}$"
    words = [word for word in word_list if re.match(pattern, word.strip())]
    return words

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)