import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_migrate import Migrate
from models import db, Recipe, ContactMessage

load_dotenv()

app = Flask(__name__)