from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(150), nullable=False)
category = db.Column(db.String(50), nullable=False)
ingredients = db.Column(db.Text, nullable=False)
instructions = db.Column(db.Text, nullable=False)
image_url = db.Column(db.String(255), nullable=True)
created_at = db.Column(db.DateTime, default=datetime.utcnow)


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)