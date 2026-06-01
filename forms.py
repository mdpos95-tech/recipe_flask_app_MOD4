from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=100)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")    

class RecipeForm(FlaskForm):
    title = StringField("Recipe Title", validators=[DataRequired(), Length(max=150)])
    category_id = SelectField("Category", coerce=int, validators=[DataRequired()])
    ingredients = TextAreaField("Ingredients", validators=[DataRequired()])
    instructions = TextAreaField("Instructions", validators=[DataRequired()])
    image_url = StringField("Image URL", validators=[Length(max=255)])
    submit = SubmitField("Submit Recipe")

class CommentForm(FlaskForm):
    message = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Post Comment")    

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")    