from flask import Flask
import os

from extensions import db, login_manager


def create_app():
    app = Flask(__name__)

    # Basic configuration
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///url_shortener.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    # Import and register routes
    with app.app_context():
        from models import User, ShortURL  # noqa: F401
        from routes import register_routes

        register_routes(app)

    return app


if __name__ == "__main__":
    application = create_app()
    with application.app_context():
        db.create_all()
    application.run(debug=True)


