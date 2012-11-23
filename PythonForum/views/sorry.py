from .. import app
from flask import render_template

@app.route("/sorry")
def sorry():
    return render_template("sorry.html")