from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from config import config
from flask_caching import Cache


db = SQLAlchemy()
ma = Marshmallow()
SECRET_KEY = 'SOME_KEY'
cache = Cache(config={'CACHE_TYPE': 'simple'})


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)
    cache.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
