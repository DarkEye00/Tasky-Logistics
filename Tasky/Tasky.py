from flask import Flask, request, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

app.secret_key = "T45ky"

@app.route('/')
def index():
    
    return render_template("index.html")
@app.route("/About_Us/")
def about():

    return render_template("about.html")
@app.route('/Transporters/')
def transport():

    return render_template("transporters.html")
@app.route('/Cargo/')
def cargo():

    return render_template("cargo.html")


if __name__ == ("__main__"):
    freezer.freeze()
