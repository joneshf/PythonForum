from flask import Flask, render_template, url_for
from flask.ext.login import LoginManager
from flask.ext.browserid import BrowserID
import time

app = Flask(__name__)
app.version = "0.1a"
# Secret key can change with each new version this forces all old logins to expire :)
app.config['SECRET_KEY'] = '\xad\xdb\xe9o\x84\x03S\xa93\xc2X\x0ejlq\xad\xcd1\xb0Ub'

# Import here so database it can reach the app object.
from database.login import get_user, get_user_by_id

# Set up the authentication realm
login_manager = LoginManager()
# Point it to the function that retrieves active users
login_manager.user_loader(get_user_by_id)
login_manager.init_app(app)

# Now the actual login system
browser_id = BrowserID()
browser_id.user_loader(get_user)
browser_id.init_app(app)

@app.route("/servertime")
def time_at_server():
    """Generic default testy route. Handy for debugging."""
    return time.asctime()

@app.route("/google980b6417f3302651.html")
def google_auth():
    return render_template("google980b6417f3302651.html")

@app.route("/persona/test")
def index():
    """Obsolete test for persona login."""
    return render_template("loginTest.html")

# Import application views here!
import views.board
import views.index
import views.favicon
import views.topic
import views.errors

# API views.
import views.personal_api
import views.public_api
import views.private_api

# All routes have now been registered.

# Setup logging
from custom_super_mega_non_blocking_logger import ThreadedTlsSMTPHandler
from config import email_password

ADMINS = ["jkbbwr@gmail.com"]
if not app.debug:
    import logging
    mail_handler = ThreadedTlsSMTPHandler(("smtp.gmail.com", 587), 'admin@pythonforum.org', ADMINS,
        'Error happened!', ('admin@pythonforum.com', email_password))
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)