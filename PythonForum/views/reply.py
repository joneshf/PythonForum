from .. import app
import time
from flask.ext.login import current_user, login_required
import shortuuid
from ..database.boards import Board
from ..database.threads import Thread
from ..database.posts import Post
from flask import render_template, request, redirect, url_for

@app.route("/success/<topic_uuid>")
def success(topic_uuid):
    return render_template("success.html", topic_uuid=topic_uuid)

@app.route("/reply/<topic_id>", methods=["POST","GET"])
@login_required
def reply(topic_id):
    if request.method == "POST":
        body = request.form.get("reply", False)
        if body:
            topic = Thread.objects(topic_uuid=topic_id)
            post = Post(author=current_user.user_in_db,content=body)
            post.save()
            topic.posts.append(post)
            return redirect(url_for("success", topic_uuid=topic_id))
        return redirect(url_for("failure", topic_uuid=topic_id))
    else:
        # First validate to see its a valid topic_id, if its not then 404 that son of a bitch.
        valid = Thread.objects(topic_uuid=topic_id) != []
        if not valid:
            return render_template("404.html")
        return render_template("reply.html")

@app.route("/new_topic/<board_name>", methods=["POST","GET"])
@login_required
def new_topic(board_name):
    if request.method == "GET":
        return render_template("new_topic.html")
    else:
        # get the board
        board = Board.objects(name=board_name).first()
        # Get the title and body from the POST
        title = request.form.get("title")
        body = request.form.get("reply")

        uuid = shortuuid.uuid()
        # Get the database reference'd author
        author = current_user.user_in_db

        date = time.asctime()

        # Construct and save the thread
        thread = Thread(title=title, author=author, topic_uuid=uuid, date=date)
        thread.save()
        # Construct and save the post.
        first_post = Post(author=author, content=body)
        first_post.save()

        thread.posts.append(first_post)
        board.topics.insert(0, thread)
        # Update collections !
        board.save()
        thread.save()

        return redirect(url_for("success", topic_uuid=uuid))