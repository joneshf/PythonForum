from .. import app
from flask import render_template
from ..database.threads import Thread

@app.route("/topic/<topic_uuid>/")
def topic(topic_uuid):
    thread = Thread.objects(topic_uuid=topic_uuid).first()
    return render_template("posts.html", topic=thread)
