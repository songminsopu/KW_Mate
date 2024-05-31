from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.secret_key = "super secret key"  # Bc it's just a demo
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # api route 등록
    from .api import auth, match, block
    app.register_blueprint(auth.bp)
    app.register_blueprint(match.bp)
    app.register_blueprint(block.bp)

    return app