from flask import Flask, render_template

app = Flask(__name__)
x = {
    "count": 110,
    "next": "https://ion.tjhsst.edu/api/schedule?page=5",
    "previous": "https://ion.tjhsst.edu/api/schedule?page=3",
    "results": [
        {
            "url": "https://ion.tjhsst.edu/api/schedule/2026-04-16",
            "date": "2026-04-16",
            "day_type": {
                "name": "Blue Day",
                "special": False,
                "blocks": [
                    {"order": 1, "name": "Period 1", "start": "8:40", "end": "10:15"},
                    {"order": 2, "name": "Period 2", "start": "10:25", "end": "12:00"},
                    {"order": 3, "name": "Lunch", "start": "12:00", "end": "12:40"},
                    {"order": 4, "name": "Period 3", "start": "12:40", "end": "14:15"},
                    {"order": 5, "name": "Period 4", "start": "14:25", "end": "16:00"},
                ],
            },
        }
    ],
}

@app.route("/")
def scheudule():
    return render_template("index.htm", schedule=x)


if __name__ == "__main__":
    app.run(debug=True)
