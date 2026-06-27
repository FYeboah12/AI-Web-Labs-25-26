from flask import Flask, render_template

app = Flask(__name__)
"""This can be tame. I guess. It also doesn’t have to be. Keep it school appropriate.
Create a site with a dogs page, and a cats page. (Or equivalent.) Static Folder Example
The dogs page should have a picture of a dog
The cats page should have a picture of a cat
You can navigate back and forth between the dogs page and the cats page; every page should be linked in a way that allows navigation to continue
The images should be saved in either ./static/ or an appropriate subfolder (i.e. ./static/images or equivalent)"""

song_list = [
    "TWICE: Talk That Talk",
    "BTS: Anpanman",
    "NewJeans: OMG",
    "BlackPink: As If It's Your Last",
    "Aespa: Drama",
    "Ive: Attitude"
]
@app.route("/")
def index():
    return render_template("list.html", tier_list = song_list)
if __name__ == "__main__":
    app.run(debug=True)