from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RecipeForm(FlaskForm):
    title = StringField("Recipe Title", validators=[DataRequired(), Length(max=150)])
    category = StringField("Category", validators=[DataRequired(), Length(max=80)])
    ingredients = TextAreaField("Ingredients", validators=[DataRequired()])
    instructions = TextAreaField("Instructions", validators=[DataRequired()])
    image_url = StringField("Image URL", validators=[Length(max=255)])
    submit = SubmitField("Submit Recipe")

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")    