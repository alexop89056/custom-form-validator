from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

from app.routes.base import base_bp
app.register_blueprint(base_bp)