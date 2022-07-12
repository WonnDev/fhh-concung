from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main/main-product.html')
@app.route("/find")
def find():
    return render_template('main/find.html')
@app.route("/login")
def login():
    return render_template('main/login.html')
