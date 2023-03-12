#step-1
from flask import Flask,request
 #step-2
app=Flask(__name__)
@app.route('/')
def home_page():
    return " Welcome to home page "
@app.route('/search')
def search_page():
    return " welcome to search page "

@app.route('/findme')
def findme_page():
    return "   Apurva Jain : https://www.linkedin.com/in/apurva-jain04 "

@app.route('/upper')
def upper_case():
    a=request.args.get('a')
    return a.upper()

@app.route('/add')
def add_sum():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)+int(b))

@app.route('/div')
def div_sum():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)/int(b))

@app.route('/sub')
def add_sub():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)-int(b))

@app.route('/multi')
def add_multi():
    a=request.args.get('a')
    b=request.args.get('b')
    return str(int(a)*int(b))
#step=4
if __name__=='__main__':
    app.run(debug=True)    