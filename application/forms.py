from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.widgets import TextArea
from application.models import User

class SignUpForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        
        if existing_user_username:
            raise ValidationError(
                "Sorry, that username already exists."
            )


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Log In")


class RecipeForm(FlaskForm):
    name = StringField("Name")
    description = StringField("Description", widget=TextArea())
    diet = SelectField("Diet", choices=[
        ("meat_eater", "Meat Eater"), 
        ("vegetarian", "Vegetarian"), 
        ("vegan", "Vegan")
    ])
    cooking_time = IntegerField("Cooking Time (Minutes)")
    servings = IntegerField("Servings")
    ingredients = StringField("Ingredients", widget=TextArea())
    instructions = StringField("Instructions", widget=TextArea())
    submit = SubmitField("Submit")