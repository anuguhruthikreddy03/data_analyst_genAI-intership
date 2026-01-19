import os

from flask import Flask

from src.db import db
from src.routes import web


def create_app() -> Flask:
    app = Flask(__name__, static_folder="static", template_folder="templates")

    # Basic config
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///url_shortener.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # URL verification behavior
    # - If True, the app will attempt a HEAD/GET with a small timeout to ensure the URL is reachable.
    # - If False, it validates only URL syntax (scheme/host).
    app.config["CHECK_URL_REACHABLE"] = os.environ.get("CHECK_URL_REACHABLE", "0") == "1"

    db.init_app(app)
    app.register_blueprint(web)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

