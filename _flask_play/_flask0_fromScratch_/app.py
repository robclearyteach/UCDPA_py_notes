## install flask first
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")
	#project/templates/home.html

@app.route("/contact")
def tiddlywinks():
	return "<h1> Contact page displaying...</h1>"

if __name__ == '__main__':
	app.run(debug=True, port=8080)