from flask import Flask
from tapsearch.indexer import Database, InvertedIndex
import os
app= Flask(__name__)
app.config['SECRET_KEY'] = 'youwontguess'
basedir = os.path.abspath(os.path.dirname(__file__))
app.static_folder = 'static'
from tapsearch.routes import admin
app.register_blueprint(admin)