from flask import Flask, render_template
"""One page has a secret message. The users must navigate the pages to find it!
Create a simple Flask app with: 
At least three different routes: /home, /about, and /contact.
Each route should have its own template with a hardcoded short message (e.g., “Welcome to the home page!”, “This is the about page”, “Here’s how to reach us”).
Within each page, add links that let you navigate between all three pages.
Use <a href="{{ url_for('route_name') }}"> 
Verify that clicking the links actually changes the URL and loads the correct template.
"""

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/about")
def abt():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.htm")

@app.route("/secret")
def secret():
    return render_template("secret.html")


if __name__ == "__main__":
    app.run(debug=True)