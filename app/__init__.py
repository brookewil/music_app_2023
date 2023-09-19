from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = 'swag'

from app import routes
