from flask import Flask

from server.extensions import db, migrate

import server.models


def create_app(config="server.config"):
    """Create Flask Application

    Args:
        config (str, optional): Application configuration. Defaults to 'server.config'.

    Returns:
        flask.Flask: Flask application
    """
    app = Flask(__name__)
    app.config.from_object(config)

    load_extensions(app)
    return app


def load_extensions(app):
    """Initialized Flask extensions

    Args:
        app (flask.Flask): Flask Application
    """
    db.init_app(app)
    migrate.init_app(app, db)
