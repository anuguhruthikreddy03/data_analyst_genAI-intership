from __future__ import annotations

from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for

from src.db import db
from src.models import ShortURL
from src.utils import generate_code, is_valid_url, normalize_url

web = Blueprint("web", __name__)


@web.get("/")
def home():
    return render_template("home.html")


@web.post("/shorten")
def shorten():
    original_raw = request.form.get("url", "")
    original_url = normalize_url(original_raw)

    valid, err = is_valid_url(
        original_url, check_reachable=bool(current_app.config.get("CHECK_URL_REACHABLE"))
    )
    if not valid:
        flash(err or "Invalid URL.", "danger")
        return render_template("home.html", original_url=original_raw), 400

    # Reuse existing short URL for same original URL (basic user convenience)
    existing = (
        ShortURL.query.filter_by(original_url=original_url)
        .order_by(ShortURL.id.desc())
        .first()
    )
    if existing:
        short_url = url_for("web.redirect_code", code=existing.short_code, _external=True)
        return render_template(
            "home.html",
            original_url=original_url,
            short_url=short_url,
        )

    # Create new short code, retry on collisions
    code = generate_code()
    for _ in range(10):
        if not ShortURL.query.filter_by(short_code=code).first():
            break
        code = generate_code()
    else:
        flash("Couldn't generate a unique short code. Please try again.", "danger")
        return redirect(url_for("web.home")), 500

    row = ShortURL(original_url=original_url, short_code=code)
    db.session.add(row)
    db.session.commit()

    short_url = url_for("web.redirect_code", code=code, _external=True)
    flash("Short URL created and saved to history.", "success")
    return render_template(
        "home.html",
        original_url=original_url,
        short_url=short_url,
    )


@web.get("/history")
def history():
    rows = ShortURL.query.order_by(ShortURL.created_at.desc()).all()
    return render_template("history.html", rows=rows)


@web.get("/<code>")
def redirect_code(code: str):
    row = ShortURL.query.filter_by(short_code=code).first()
    if not row:
        flash("Short URL not found.", "warning")
        return redirect(url_for("web.home")), 404
    return redirect(row.original_url)


