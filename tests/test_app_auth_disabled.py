from flask import url_for
from flask_testing import TestCase
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from application import app, db
from application.models import User, Recipe
import os


class TestBase(TestCase):

    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI = 'sqlite:///',
            SECRET_KEY = os.environ.get("TEST_DB_SECRET_KEY"),
            DEBUG = True,
            WTF_CSRF_ENABLED = False,
            LOGIN_DISABLED = True
        )
        return app

    def setUp(self):
        # Create table schema
        db.create_all()

        # Create test recipe
        bcrypt=Bcrypt(app)
        test_user = User(
            username="TestUsername",
            password = "TestPassword"
            )

        test_recipe = Recipe(
            name="Test Name: Eggs and Bacon",
            author = "Anonymous", 
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

    def test_profile_get(self):
        response = self.client.get(url_for('profile'))
        self.assertEqual(response.status_code, 200)

    def test_add_recipe_get(self):
        response = self.client.get(url_for('add_recipe', recipe_id=1))
        self.assertEqual(response.status_code, 200)

    def test_update_recipe_get(self):
        response = self.client.get(url_for('update_recipe', recipe_id=1))
        self.assertEqual(response.status_code, 200)


# Test Recipe Creation Functionality

class TestAddRecipe(TestBase):

    def test_add_recipe(self):
        response = self.client.post(
            url_for('add_recipe'),
            data = dict(

                name="Test Name: Sandwich",
                author="Jane Doe", 
                description = "Test Description: A basic sandwich.",
                cooking_time = 5,
                servings = 1,
                diet = 'Test Diet: Vegetarian',
                ingredients = 'Test Ingredients: Bread, Lettuce',
                instructions = 'Test Instructions: Make the sandwich. Serve.'),
                follow_redirects=True
        )

        assert Recipe.query.filter_by(name="Test Name: Sandwich").first().id == 2


# Test Recipe Deletion Functionality


class TestDeleteRecipe(TestBase):

    def test_delete_recipe(self):

        existing_recipe = Recipe.query.filter_by(id=1).first()
        assert existing_recipe.name=='Test Name: Eggs and Bacon'
        response = self.client.post(
            url_for('delete_recipe', recipe_id=1))
        assert len(Recipe.query.all()) == 0


# Test Recipe Update Functionality

class TestUpdateRecipe(TestBase):

    def test_update_recipe(self):
        
        existing_recipe = Recipe.query.filter_by(id=1).first()
        assert existing_recipe.name=='Test Name: Eggs and Bacon'
        response = self.client.post(
            url_for('update_recipe', recipe_id=1),
            data = dict(

                name="Test Name: Sandwich",
                author="Jane Doe", 
                description = "Test Description: A basic sandwich.",
                cooking_time = 5,
                servings = 1,
                diet = 'Test Diet: Vegetarian',
                ingredients = 'Test Ingredients: Bread, Lettuce',
                instructions = 'Test Instructions: Make the sandwich. Serve.'),
                follow_redirects=True
        )

        assert Recipe.query.filter_by(name="Test Name: Sandwich").first().id == 1