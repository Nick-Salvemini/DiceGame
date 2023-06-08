from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text
from models import db, connect_db, User, Match
import authentication

app = Flask(__name__)

app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///dice_game'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'jH5Q6?zm9|zZ^Q-'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()

# HOMEPAGE TO LOGIN
# **************************************************


# HOMEPAGE ONCE LOGGED IN
# **************************************************


# PAGE FOR PLAYING COMPUTER OPPONENT
# **************************************************


# PAGE FOR PLAYING HUMAN OPPONENT
# **************************************************
