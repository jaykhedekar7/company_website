from flask import Flask, render_template, url_for, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime
import random
import os
import math


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SESSION_COOKIE_SECURE=True
SESSION_COOKIE_NAME='codingthon-website'

if (params["local_server"]):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)