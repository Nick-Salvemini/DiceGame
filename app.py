from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text
# from models import db, connect_db
import authentication
# import pyrebase

app = Flask(__name__)

app.app_context().push()

# config = {
#     'apiKey': "AIzaSyBA9qS60QyXhrdYXsyk8MLan4pNgnPfMjo",
#     'authDomain': "dicegame-a8c5b.firebaseapp.com",
#     'projectId': "dicegame-a8c5b",
#     'storageBucket': "dicegame-a8c5b.appspot.com",
#     'messagingSenderId': "17795767024",
#     'appId': "1:17795767024:web:d1da35cf106eef5b640035",
#     'measurementId': "G-MS3VJ2HC6R",
#     'databaseURL': ''
# }

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///XXXXXXXXXXXXXXXXXX'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chickens'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

# connect_db(app)

# HOMEPAGE TO LOGIN
# **************************************************



# HOMEPAGE ONCE LOGGED IN
# **************************************************



# PAGE FOR PLAYING COMPUTER OPPONENT
# **************************************************



# PAGE FOR PLAYING HUMAN OPPONENT
# **************************************************
