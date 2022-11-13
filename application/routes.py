from application import app, db
from flask import render_template, url_for, redirect, request
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from application.forms import LoginForm, SignUpForm, RecipeForm
from application.models import User, Recipe


bcrypt = Bcrypt(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    all_recipes = Recipe.query.all()
    return render_template('index.html', all_recipes=all_recipes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('profile'))


    return render_template('login.html', form=form)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route('/add_recipe', methods = ['GET', 'POST'])
def add_recipe():
    form = RecipeForm()

    if request.method == 'POST':

        if form.validate_on_submit():

            recipe = Recipe(
                name = form.name.data,
                author = current_user.username,
                description = form.description.data,
                servings = form.servings.data,
                diet = form.diet.data,
                ingredients = form.ingredients.data,
                instructions = form.instructions.data,
            )
            db.session.add(recipe)
            db.session.commit()

            return(redirect(url_for('index')))
            

    return render_template('add_recipe.html', form=form)
