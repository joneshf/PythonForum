from .. import app
from flask import render_template


@app.errorhandler(401)
def page_not_found(e):
    return render_template("401.html"), 401


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404