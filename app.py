from flask import Flask, request
app = Flask(__name__)

@app.route('/welcome')
def home():
    return "Welcome "



@app.route("/welcome/home")
def home2():
    return "Welcome home"

@app.route("/welcome/back")
def home3():
    return "Welcome back"
