## Advanced URL Shortener – Flask App

This is a simple URL shortener web application for advanced users, built with **Flask**, **Flask‑Login**, **SQLAlchemy**, **SQLite**, and **Bootstrap**.

### Features

- **User accounts**
  - Signup with unique username (must be **5–9 characters**).
  - Login and logout with session management.
- **URL shortening**
  - Enter a long URL and generate a short code.
  - Short URLs redirect to the original URL.
  - URLs are **saved per user**.
- **History**
  - After login, a **dashboard** shows:
    - A form to shorten new URLs.
    - The **latest** shortened URL with a **Copy** button.
    - A table of all previously shortened URLs for that user.

### Project Structure

- `app.py` – Flask application factory, configuration, and startup.
- `models.py` – SQLAlchemy models (`User`, `ShortURL`).
- `routes.py` – All routes (signup, login, dashboard, shorten, redirect, etc.).
- `templates/` – HTML templates using Bootstrap:
  - `base.html`, `home.html`, `signup.html`, `login.html`, `dashboard.html`
- `requirements.txt` – Python dependencies.

### Setup & Run (Windows / PowerShell)

1. **Create and activate a virtual environment (recommended)**

   ```powershell
   cd C:\Users\anugu\Downloads\adv_flask_url_app
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. **Install dependencies**

   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the application**

   ```powershell
   python app.py
   ```

4. **Open in browser**

   Go to `http://127.0.0.1:5000/`

### Usage Flow

- **Home page** (`/`)
  - Choose **Login** or **Signup**.
- **Signup** (`/signup`)
  - Enter username (5–9 characters) and password.
  - If username already exists, you see:  
    **“This username already exists. Please choose another.”**
  - If username length is invalid, you see:  
    **“Username must be between 5 to 9 characters long”**
  - After successful signup, you are redirected to the **login** page.
- **Login** (`/login`)
  - Enter your username and password.
  - On success, you are taken to the **URL shortener dashboard**.
- **Dashboard** (`/dashboard`)
  - Enter a **long URL** and click **Shorten**.
  - The latest shortened URL appears in a text field with a **Copy** button.
  - Below, a table lists **all your previous URLs** with their shortened versions and timestamps.
- **Short URL redirect** (`/<short_code>`)
  - Visiting the short URL redirects you to the original URL.

### Notes

- Database: **SQLite** file `url_shortener.db` in the project directory.
- To start fresh, you can delete `url_shortener.db` (will be re-created on next run).


