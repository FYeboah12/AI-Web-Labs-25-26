import re

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route('/')
def root_page():
    return render_template('index.htm')

@app.route('/get_schedule_from_ion/<date>')
def get_schedule_from_ion(date):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
        return jsonify({"error": "Invalid date format"}), 400
    url = f"https://ion.tjhsst.edu/api/schedule/{date}?format=json"
    response = requests.get(url)
    #turn this from json into not json
    return response.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)