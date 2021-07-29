# import module
from flask import Flask, render_template, redirect, request, jsonify

# Create an instance of Flask
app = Flask(__name__)

# Create route / index.html must stay outside of templates folder in same path as app.py
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index1") # Can change "/index1" to the "top left" tab name  
def index1(): # Can change index1 to descriptive route name
    return render_template("index1.html") # Can change "index1.html" to the renamed HTML title

@app.route("/index2")
def index2():
    return render_template("index2.html")

@app.route("/index3")
def index3():
    return render_template("index3.html")

@app.route("/index4")
def index4():
    return render_template("index4.html")

if __name__ == "__main__":
    app.run(debug=True)
