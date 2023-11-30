from flask import Flask

app = Flask(__name__)

from flask import redirect, url_for, render_template

@app.route("/contact")
def contact():
    return render_template("index.html")

@app.route("/")
def index():
    return redirect(url_for("contact"))