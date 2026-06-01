import os
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import db, User, Category, Recipe, Comment, Favorite, ContactMessage
from forms import RegisterForm, LoginForm, RecipeForm, CommentForm, ContactForm

load_dotenv()


app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "temporary_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password_hash == form.password.data:
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        flash("Invalid email or password.", "danger")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been successfully logged out.", "success")
    return redirect(url_for("recipes"))

@app.route("/recipes")
def recipes():
    all_recipes = Recipe.query.all()
    return render_template("recipes.html", recipes=all_recipes) 

@app.route("/recipe/<int:recipe_id>", methods=["GET", "POST"])
@login_required
def recipe_detail(recipe_id):
    form = CommentForm()
    recipe = Recipe.query.get_or_404(recipe_id)
    if form.validate_on_submit():
        comment = Comment(
            message=form.message.data,
            user_id=current_user.id,
            recipe_id=recipe.id
        )
        db.session.add(comment)
        db.session.commit()
        flash("Comment posted successfully!", "success")
        return redirect(url_for("recipe_detail", recipe_id=recipe.id))
    return render_template("recipe_detail.html", recipe=recipe, form=form)

@app.route("/favorite/<int:recipe_id>", methods=["POST"])
@login_required
def favorite_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    existing_favorite = Favorite.query.filter_by(user_id=current_user.id, recipe_id=recipe.id).first()
    if existing_favorite:
        flash("You have already favorited this recipe.", "info")
        return redirect(url_for("recipe_detail", recipe_id=recipe.id))
    else:
        favorite = Favorite(
            user_id=current_user.id,
            recipe_id=recipe.id
        )
        db.session.add(favorite)
    db.session.commit()
    flash("Recipe added to favorites!", "success")
    return redirect(url_for("recipe_detail", recipe_id=recipe.id))

@app.route("/remove-favorite/<int:recipe_id>", methods=["POST"])
@login_required
def remove_favorite(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    favorite = Favorite.query.filter_by(user_id=current_user.id, recipe_id=recipe.id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        flash("Recipe removed from favorites.", "success")
    return redirect(url_for("recipe_detail", recipe_id=recipe.id))

@app.route("/favorites")
@login_required
def favorites():
    favorite_recipes = Recipe.query.join(Favorite).filter(Favorite.user_id == current_user.id).all()
    return render_template("favorites.html", favorites=favorite_recipes)

@app.route("/delete-recipe/<int:recipe_id>")
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user != current_user:
        flash("You do not have permission to delete this recipe.", "danger")
        return redirect(url_for("recipe_detail", recipe_id=recipe.id))
    Comment.query.filter_by(recipe_id=recipe.id).delete()
    Favorite.query.filter_by(recipe_id=recipe.id).delete()
    db.session.delete(recipe)
    db.session.commit()
    flash("Recipe deleted successfully!", "success")
    return redirect(url_for("recipes"))

@app.route("/add-recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    form = RecipeForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]

    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            image_url=form.image_url.data,
            user_id=current_user.id,
            category_id=form.category_id.data
        )
        db.session.add(recipe)
        db.session.commit()
        flash("Recipe added successfully!", "success")
        return redirect(url_for("recipes"))
    return render_template("add_recipe.html", form=form)

@app.route("/edit-recipe/<int:recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.user != current_user:
        flash("You do not have permission to edit this recipe.", "danger")
        return redirect(url_for("recipe_detail", recipe_id=recipe.id))
    form = RecipeForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.ingredients = form.ingredients.data
        recipe.instructions = form.instructions.data
        recipe.image_url = form.image_url.data
        recipe.category_id = form.category_id.data
        db.session.commit()
        flash("Recipe updated successfully!", "success")
        return redirect(url_for("recipe_detail", recipe_id=recipe.id))
    if request.method == "GET":
        form.title.data = recipe.title
        form.ingredients.data = recipe.ingredients
        form.instructions.data = recipe.instructions
        form.image_url.data = recipe.image_url
        form.category_id.data = recipe.category_id
    return render_template("edit_recipe.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)