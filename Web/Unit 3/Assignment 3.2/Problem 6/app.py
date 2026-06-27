from datetime import datetime
from math import inf

from flask import Flask, render_template, request

app = Flask(__name__)
global visits_list
visits_list = []
@app.route("/")
def index():
    return "Go to /home or /log"


@app.route("/home")
def home():
    return render_template("index.html")
"""You are now the NSA.
Create a server with two routes /home and /log. Visits to the /log page should display a list of previous visits to the site. Specifically, a visit to /log should 
Record the current time (e.g., datetime.now()).
Calculate how many seconds have passed since the last visit.
Save (append) the visit info in a list of dictionaries, where each dictionary stores:
IP address of the visitor (request.remote_addr)
Browser / User-Agent (request.headers.get("User-Agent"))
Visit time (formatted string)
Pass the ‘log’ list to the template 
The template should loop over the log entries and display them in a table or list.
"""

@app.route("/log")
def log():
    current_time = datetime.now()
    info = {"ip": request.remote_addr, "browser": request.headers.get("User-Agent"),"current_time": current_time.strftime("%Y-%m-%d %H:%M:%S")}
    visits_list.append(info)
    return render_template("log.html", info_list = visits_list)
    

if __name__ == "__main__":
    app.run(debug=True)
