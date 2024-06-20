## install flask first
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)
app.secret_key = "put a real secret key here"

@app.route("/")
@app.route("/<a_name>")
def home(a_name=None):
	return render_template("index.html", name=a_name)



@app.route("/greet")			
@app.route("/greet/<a_name>") 	
def greet(a_name="Anonymous"):
	print( a_name, url_for('greet') )			
	return redirect( url_for("home") )

@app.route("/contact")				
def contact():				
	return render_template("contact.html")



if __name__ == '__main__':
	app.run(debug=True, port=8080)



"""
@app.route("/")
@app.route("/home")
def home(a_name=None):
	current_user = session.get('user_name') #return None if no user
	if current_user:
		return render_template("home.html", name=current_user)
	else:
		return render_template("home.html")


@app.route("/greet")			
@app.route("/greet/<a_name>") 	
def greet(a_name="Anonymous"):
	session['user_name'] = a_name				
	return redirect(f"/home")
"""