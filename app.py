import os
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import db, Recipe, ContactMessage
from forms import RecipeForm, ContactForm

load_dotenv()


app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "temporary_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/recipes")
def recipes():
    all_recipes = Recipe.query.all()
    return render_template("recipes.html", recipes=all_recipes) 

@app.route("/recipe/<int:recipe_id>")
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return render_template("recipe_detail.html", recipe=recipe)

@app.route("/add-recipe", methods=["GET", "POST"])
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(
            title=form.title.data,
            category=form.category.data,
            ingredients=form.ingredients.data,
            instructions=form.instructions.data,
            image_url=form.image_url.data
        )
        db.session.add(recipe)
        db.session.commit()
        flash("Recipe added successfully!", "success")
        return redirect(url_for("recipes"))
    return render_template("add_recipe.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)