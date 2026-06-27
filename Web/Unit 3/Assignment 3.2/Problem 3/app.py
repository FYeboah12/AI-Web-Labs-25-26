from flask import Flask, render_template

app = Flask(__name__)
"""This can be tame. I guess. It also doesn’t have to be. Keep it school appropriate.
Create a site with a dogs page, and a cats page. (Or equivalent.) Static Folder Example
The dogs page should have a picture of a dog
The cats page should have a picture of a cat
You can navigate back and forth between the dogs page and the cats page; every page should be linked in a way that allows navigation to continue
The images should be saved in either ./static/ or an appropriate subfolder (i.e. ./static/images or equivalent)"""

@app.route("/")
def index():
    return "Look at /panda or /elephant :)"

@app.route("/panda")
def panda():
    return render_template("panda.htm")


@app.route("/elephant")
def elephant():
    return render_template("elephant.htm")


if __name__ == "__main__":
    app.run(debug=True)
