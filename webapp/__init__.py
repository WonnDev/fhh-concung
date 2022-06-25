from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home/index.html')

@app.route("/product")
def product():
    return render_template('main/main-product.html')