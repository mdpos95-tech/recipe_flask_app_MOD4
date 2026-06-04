from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegisterForm(FlaskForm): #Form used to register a new user account.
    username = StringField("Username", validators=[DataRequired(), Length(min=3, max=100)]) #Username must be between 3 and 100 characters.
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")]) #Password confirmation must match the original password.
    submit = SubmitField("Register")

class LoginForm(FlaskForm): #Form used for user authentication and login.
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")    

class RecipeForm(FlaskForm): #Form used to create and submit a new recipe.
    title = StringField("Recipe Title", validators=[DataRequired(), Length(max=150)])
    category_id = SelectField("Category", coerce=int, validators=[DataRequired()]) #Category is selected from categories stored in the database.
    ingredients = TextAreaField("Ingredients", validators=[DataRequired()])
    instructions = TextAreaField("Instructions", validators=[DataRequired()])
    image_url = StringField("Image URL", validators=[Length(max=255)]) #Optional image URL for displaying recipe image.
    submit = SubmitField("Submit Recipe")

class CommentForm(FlaskForm): #Form used to allow users to post comments on recipes.
    message = TextAreaField("Comment", validators=[DataRequired()])
    submit = SubmitField("Post Comment")    

class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=100)])
    email = StringField("Email", validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send Message")    