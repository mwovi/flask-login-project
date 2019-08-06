from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY']='21192fcf622691fdcc2a64868add4b3f'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///razo.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from flaskblog import routes