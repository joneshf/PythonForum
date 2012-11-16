import os

from flask import send_from_directory
from .. import app

@app.route('/favicon.ico')
def favicon():
    """Return the favicon.ico for the forum. I didn't write this."""
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')