from application import db, app
from application.routes import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    author = db.Column(db.String, nullable=False)
    description = db.Column(db.String(180), nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    diet = db.Column(db.String(30), nullable=False)
    ingredients = db.Column(db.String(500), nullable=False)
    instructions = db.Column(db.String(1000), nullable=False)
    