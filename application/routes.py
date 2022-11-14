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
    all_recipes = Recipe.query.all()
    return render_template('profile.html', all_recipes=all_recipes)


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
@login_required
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
                cooking_time =form.cooking_time.data,
                ingredients = form.ingredients.data,
                instructions = form.instructions.data,
            )
            db.session.add(recipe)
            db.session.commit()

            return(redirect(url_for('index')))
            

    return render_template('add_recipe.html', form=form)


@app.route('/update_recipe/<int:recipe_id>', methods = ['GET', 'POST'])
@login_required
def update_recipe(recipe_id):
    recipe_to_update = Recipe.query.get(recipe_id)
    form = RecipeForm()
    
    if request.method == 'GET':
        form.name.data = recipe_to_update.name
        form.description.data = recipe_to_update.description
        form.servings.data = recipe_to_update.servings
        form.diet.data = recipe_to_update.diet
        form.cooking_time.data = recipe_to_update.cooking_time
        form.ingredients.data = recipe_to_update.ingredients
        form.instructions.data = recipe_to_update.instructions
        

    if recipe_to_update.author == current_user.username and request.method == 'POST':
        recipe_to_update.name = form.name.data
        recipe_to_update.author = current_user.username
        recipe_to_update.description = form.description.data
        recipe_to_update.servings = form.servings.data
        recipe_to_update.diet = form.diet.data
        recipe_to_update.cooking_time = form.cooking_time.data
        recipe_to_update.ingredients = form.ingredients.data
        recipe_to_update.instructions = form.instructions.data
        db.session.commit()

        return(redirect(url_for('index')))
    
    return render_template('update_recipe.html', recipe_to_update=recipe_to_update, form=form)


@app.route('/delete_recipe/<int:recipe_id>', methods = ['GET', 'POST'])
@login_required
def delete_recipe(recipe_id):
    recipe_to_delete = Recipe.query.get(recipe_id)
    if recipe_to_delete.author == current_user.username:

        db.session.delete(recipe_to_delete)
        db.session.commit()
    else:
        return(redirect(url_for('index')))


    return(redirect(url_for('index')))


@app.route('/view_recipe/<int:recipe_id>', methods = ['GET'])
def view_recipe(recipe_id):
    recipe_to_view = Recipe.query.get(recipe_id)

    return render_template('view_recipe.html', recipe_to_view=recipe_to_view)