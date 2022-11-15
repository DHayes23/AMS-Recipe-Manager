from flask import url_for
from flask_testing import TestCase
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from application import app, db
from application.models import User, Recipe
import os


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///',
            SECRET_KEY = os.environ.get("TEST_DB_SECRET_KEY"),
            DEBUG = True,
            WTF_CSRF_ENABLED = False
        )
        return app

    def setUp(self):
        # Create table schema
        db.create_all()

        # Create test recipe

        test_user = User(
            username="Test Username: John Doe",
            password = "TestPassword"
            )

        test_recipe = Recipe(
            name="Test Name: Eggs and Bacon",
            author = "Test Username: John Doe", 
            description = "Test Description: A combination of Eggs and Bacon.",
            cooking_time = 15,
            servings = 2,
            diet = 'Test Diet: Meat Eater',
            ingredients = 'Test Ingredients: Eggs, Bacon',
            instructions = 'Test Instructions: Cook the Eggs. Cook the Bacon. Serve.'
            )

        # save sample data to database
        db.session.add(test_user)
        db.session.add(test_recipe)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestRoutes(TestBase):

    # Tests all non-authenticated routes for correct response
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_login_get(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_get(self):
        response = self.client.get(url_for('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_recipe_get(self):
        response = self.client.get(url_for('view_recipe', recipe_id=1))
        self.assertEqual(response.status_code, 200)
    