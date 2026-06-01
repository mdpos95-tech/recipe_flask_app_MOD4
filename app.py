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

if __name__ == "__main__":
    app.run(debug=True)