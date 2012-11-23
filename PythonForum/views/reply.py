from .. import app
from flask import render_template


@app.route("/reply", methods=["POST","GET"])
def reply():
    return render_template("reply.html")