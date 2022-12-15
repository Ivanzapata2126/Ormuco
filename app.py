from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
import requests
app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/logging",methods=['POST'])
def logging():
    email = request.form['email']
    password = request.form['password']
    if(logged(email,password)):
        return redirect("/home")
    else:
        return redirect("/login")

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/create')
def create():
    return render_template('createInstance.html')

if __name__ == '__main__':
    app.run()