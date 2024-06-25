from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET"]) 
def index_get():
    if request.args:
        name_submitted = request.args.get("name")
        return render_template('index.html', name=name_submitted, render="GET")
    else:
        return render_template('index.html')
    
@app.route('/', methods=["POST"]) 
def index_post():
    name_posted = request.form.get("name")
    return render_template("index.html", name=name_posted, render="POST")
    
if __name__ == '__main__':
    app.run(debug=True, port=8080)
