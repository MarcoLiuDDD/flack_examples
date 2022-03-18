# use flask to create a blog

# config.py
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  #Database configuration
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  
# models.py
from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(80), nullable=False)
  email = db/Column(db.String(120), nullable=False)
  
  def __repr__(self):

# app.py
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import DQLAlchemy
from config import Config 

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

@app/route('/')
def index():
  paragraphs = [
    'para 1',
    'para 2'
  ]
  return render_template('index.html', title='Home', data=paragraphs)

if __name__ == '__main__':
  
