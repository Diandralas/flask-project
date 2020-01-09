from flask import Flask, render_template, redirect, request, url_for  #import library
app = Flask(__name__) #start the app

@app.route('/hello')    #create a new route
def hello():
    return "Hello World!"

@app.route('/index') 
def index():
    return render_template("index.html")

@app.route('/login', methods= ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        return redirect (url_for('index', name = user))
    else:
        user = request.args.get('user')
        return redirect (url_for('index', name = user))


if __name__ == "__main__":
    app.run(debug=True)   #exec the app
