from __future__ import annotations

import re
import secrets
from urllib.parse import urlparse

import requests
import validators


_CODE_ALPHABET_RE = re.compile(r"^[A-Za-z0-9_-]+$")


def normalize_url(raw: str) -> str:
    """
    Normalize user input:
    - trims whitespace
    - if scheme missing, defaults to https://
    """
    raw = (raw or "").strip()
    if not raw:
        return raw
    parsed = urlparse(raw)
    if parsed.scheme:
        return raw
    return f"https://{raw}"


def is_valid_url(url: str, *, check_reachable: bool) -> tuple[bool, str | None]:
    """
    Returns (is_valid, error_message).
    """
    url = (url or "").strip()
    if not url:
        return False, "Please enter a URL."

    # Basic syntactic validation
    if not validators.url(url):
        return False, "That doesn't look like a valid URL."

    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return False, "Only http:// and https:// URLs are supported."
    if not parsed.netloc:
        return False, "URL must include a valid host."

    if check_reachable:
        ok, msg = _is_reachable(url)
        if not ok:
            return False, msg

    return True, None


def _is_reachable(url: str) -> tuple[bool, str | None]:
    """
    Best-effort reachability check with short timeouts.
    """
    try:
        # Prefer HEAD; fall back to GET for servers that block HEAD.
        r = requests.head(url, allow_redirects=True, timeout=3)
        if r.status_code >= 400:
            r = requests.get(url, allow_redirects=True, timeout=3)
        if r.status_code >= 400:
            return False, f"URL responded with status {r.status_code}."
        return True, None
    except requests.RequestException:
        return False, "Couldn't reach that URL (network/host error)."


def generate_code(length: int = 7) -> str:
    """
    Generates a short, URL-safe code.
    """
    # token_urlsafe(n) produces ~ 1.3n chars; trim to requested length
    code = secrets.token_urlsafe(6)[:length]
    # Ensure strictly url-safe charset we expect (defensive)
    if not _CODE_ALPHABET_RE.match(code):
        code = re.sub(r"[^A-Za-z0-9_-]", "", code)
    return code[:length] if len(code) >= length else (code + "0" * (length - len(code)))


