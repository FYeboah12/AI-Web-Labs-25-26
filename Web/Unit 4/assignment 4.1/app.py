from flask import Flask, render_template, jsonify
app = Flask(__name__)
vote = 0
upvotes = 0
downvotes = 0
@app.route('/')
def hello_world():
    return render_template('vote.htm')

@app.route("/upvote")
def upvote():
    global vote
    global upvotes
    vote += 1
    upvotes += 1
    reddit  = {
        "total": vote,
        "upvotes": upvotes,
        "downvotes": downvotes
	}
    print(reddit)
    return jsonify(reddit)

@app.route("/downvote")
def downvote():
    global vote
    global downvotes
    vote -= 1
    downvotes += 1
    reddit  = {
        "total": vote,
        "upvotes": upvotes,
        "downvotes": downvotes
	}
    print(reddit)
    return jsonify(reddit)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)