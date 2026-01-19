# URL Shortener (Flask + SQLite)

## Features
- Shorten long URLs into a short link
- One-click copy button for the short link
- Saves every shortened URL to SQLite and shows it on **History** page
- Redirects `/<code>` to the original URL
- URL validation (syntax), with optional reachability check

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open the app at `http://127.0.0.1:5000/`.

## Optional: stronger URL verification
By default the app validates URL syntax only. To also check that the URL is reachable over the network:

```bash
$env:CHECK_URL_REACHABLE="1"
python app.py
```


