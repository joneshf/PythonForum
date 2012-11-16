from .. import app
from ..database import boards
from flask import render_template

@app.route("/board/<board_id>/")
def category(board_id):
    board = boards.Board.objects(board_id=board_id).first()
    return render_template("board.html", board=board, topics=board.topics)
