from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import os



app = Flask(__name__)

if os.path.exists("env.py"):
    import env

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get("RECIPEASE_DB_SECRET_KEY")

db = SQLAlchemy(app)

from application import routes
from application import models
from application import forms
