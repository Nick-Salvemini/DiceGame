from flask import Flask, request, redirect, render_template, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text
from models import db, connect_db

app = Flask(__name__)

app.app_context().push()
  
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///XXXXXXXXXXXXXXXXXX'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'chickens'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)
