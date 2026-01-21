from urllib.parse import urlparse

from flask import (
    render_template,
    redirect,
    url_for,
    flash,
    request,
)
from flask_login import login_user, login_required, logout_user, current_user

from app import db
from models import User, ShortURL


def is_valid_username(username: str) -> bool:
    return 5 <= len(username) <= 9


def normalize_url(url: str) -> str:
    if not url:
        return url
    parsed = urlparse(url)
    if not parsed.scheme:
        url = "https://" + url
    return url


@login_required
def dashboard():
    user_urls = (
        ShortURL.query.filter_by(user_id=current_user.id)
        .order_by(ShortURL.created_at.desc())
        .all()
    )
    return render_template("dashboard.html", user=current_user, urls=user_urls)


def home():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return render_template("home.html")


def signup():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if not is_valid_username(username):
            flash("Username must be between 5 to 9 characters long", "danger")
            return render_template("signup.html", username=username)

        existing = User.query.filter_by(username=username).first()
        if existing:
            flash("This username already exists. Please choose another.", "danger")
            return render_template("signup.html", username=username)

        if not password:
            flash("Password is required.", "danger")
            return render_template("signup.html", username=username)

        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash("Signup successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")


def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Logged in successfully.", "success")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("dashboard"))

        flash("Invalid username or password.", "danger")

    return render_template("login.html")


@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))


@login_required
def shorten():
    original_url = request.form.get("original_url", "").strip()
    if not original_url:
        flash("Please enter a URL to shorten.", "danger")
        return redirect(url_for("dashboard"))

    normalized = normalize_url(original_url)
    short = ShortURL.create_unique(normalized, current_user.id)
    flash("URL shortened successfully!", "success")
    return redirect(url_for("dashboard", new_id=short.id))


def redirect_short(code):
    short = ShortURL.query.filter_by(short_code=code).first_or_404()
    return redirect(short.original_url)


def register_routes(app):
    app.add_url_rule("/", "home", home, methods=["GET"])
    app.add_url_rule("/signup", "signup", signup, methods=["GET", "POST"])
    app.add_url_rule("/login", "login", login, methods=["GET", "POST"])
    app.add_url_rule("/logout", "logout", logout, methods=["GET"])
    app.add_url_rule("/dashboard", "dashboard", dashboard, methods=["GET"])
    app.add_url_rule("/shorten", "shorten", shorten, methods=["POST"])
    app.add_url_rule("/<string:code>", "redirect_short", redirect_short, methods=["GET"])


