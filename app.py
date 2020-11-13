from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
@app.route("/math/add")
def add1():
#add A and B

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = add(a,b)
    return str(total)

@app.route("/sub")
@app.route("/math/sub")
def sub1():
#add A and B

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = sub(a,b)
    return str(total)

@app.route("/mult")
@app.route("/math/mult")
def mult1():
#add A and B

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = mult(a,b)
    return str(total)

@app.route("/div")
@app.route("/math/div")
def div1():
#add A and B

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = div(a,b)
    return str(total)


