from flask import url_for
from flask_testing import TestCase
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from application import app, db
from application.models import User, Recipe
import os


bcrypt = Bcrypt(app)


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///',
            SECRET_KEY = os.environ.get("TEST_DB_SECRET_KEY"),
            DEBUG = True,
            WTF_CSRF_ENABLED = False,
            # LOGIN_DISABLED = True
        )
        return app

    def setUp(self):
        # Create table schema
        db.create_all()

        # Create test recipe
        test_user = User(
            username="TestUsername",
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

# Test Template Response Codes

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

# Test Signup Redirect

    def test_signup_post(self):
        with self.client:
            response = self.client.post(url_for('signup'),
            data={'username': 'TestUsername2', 'password': 'TestUsername2'},
            follow_redirects=True)
            assert response.request.path=='/login'
            assert User.query.filter_by(username="TestUsername2").first().id == 2


    # Test Login Redirect
    # def test_login_post(self):
    #         with self.client:
    #             new_password = pw_hash = bcrypt.generate_password_hash('TestPassword').decode('utf-8') 
    #             response = self.client.post(url_for('login'),
    #             data={'username': 'TestUsername', 'password': new_password},
    #             follow_redirects=True)
    #             assert response.request.path=='/profile'