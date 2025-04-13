from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = '29cecf8afd6176f06bb3f55472d490d1'
if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt (app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "faça longin para poder acessar ou crie uma conta"
login_manager.login_message_category = "alert-info"
from comunidadeimpressionadora import routes

'''
login_view é a página que ele vai redirecionar quando o login maneger exigir aquele login, coloca o 
nome da função que vai se redirecionar 

pip install email_validator, flask, flask-login LoginManager, flask-bcrypt Bcrypt, flask_sqlalchemy SQLAlchemy
 '''

