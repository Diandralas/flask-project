from flask import Flask, render_template  #import library
app = Flask(__name__) #start the app

@app.route('/hello')    #create a new route
def hello():
    return "Hello World!"

@app.route('/index') 
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)   #exec the app
