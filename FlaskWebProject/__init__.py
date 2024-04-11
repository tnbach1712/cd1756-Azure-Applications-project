"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:!6Den10kytu@@192.168.49.1/bachtnsqlserver01?driver=ODBC+Driver+17+for+SQL+Server'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# TODO: Add any logging levels and handlers with app.logger
# logging.basicConfig(filename='app.log', level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views