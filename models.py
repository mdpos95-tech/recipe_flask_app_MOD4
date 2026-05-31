from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)



    class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)