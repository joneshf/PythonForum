from .. import app
from ..database.forum import Forum
from flask import render_template, flash

@app.route("/")
def index():
    flash("The forum is still in pre-alpha and missing lots of content. More content will be added over the next few days. Be patient")
    categories = Forum.objects.first().categories
    return render_template("index.html", categories=categories)
