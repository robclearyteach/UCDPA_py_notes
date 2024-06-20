## install flask first
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html")


@app.route("/greet")			
@app.route("/greet/<a_name>") 	
def greet(a_name="Anonymous"):				
	return f"<h2> Hiya, how are you: {a_name}</h2>"


#/digit-sum/1234
@app.route("/digit-sum/<int:number>") 	
def age(number=0):			
	sum = 0
	while( digit := number%10 ):
		sum += digit
		number = number // 10
		
	return render_template("home.html", digit_sum=sum)




if __name__ == '__main__':
	app.run(debug=True, port=8080)