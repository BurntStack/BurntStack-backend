# BurntStack — Backend

Secure REST API for the BurntStack Technologies website, built with Django & Django REST Framework.

## Tech Stack

- **Python 3.12** · **Django 5.1** · **Django REST Framework**
- **SimpleJWT** — JWT authentication
- **PostgreSQL** (Supabase) in production · SQLite fallback for local dev
- **Celery + Redis** — background tasks (optional; runs eagerly without a broker)
- **WhiteNoise** — static files · **Gunicorn** — WSGI server
- **django-cors-headers**, **django-filter**, throttling, secure headers

## Getting Started

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows
pip install -r requirements.txt
copy .env.example .env            # then edit values

python manage.py migrate
python manage.py seed             # demo content
python manage.py createsuperuser
python manage.py runserver        # http://127.0.0.1:8000
```

- API root: `http://127.0.0.1:8000/api/`
- Admin: `http://127.0.0.1:8000/admin/`

## Connecting to Supabase PostgreSQL

The project **burntstack** (`ref: xqpnpfnozukidxzeoweg`, region `ap-south-1`) is already
identified. To switch from SQLite to Supabase Postgres, add your database password to
`DATABASE_URL` in `.env` and uncomment it:

```
DATABASE_URL=postgresql://postgres.xqpnpfnozukidxzeoweg:YOUR_DB_PASSWORD@aws-0-ap-south-1.pooler.supabase.com:5432/postgres
```

Then run `python manage.py migrate` again to create the tables in Supabase.
(The password is the one set when the Supabase project was created — it is **not** the
`sbp_...` access token. You can reset it in the Supabase dashboard → Project Settings → Database.)

## API Endpoints

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/api/health/` | — | Liveness probe |
| POST | `/api/auth/token/` | — | Obtain JWT access + refresh |
| POST | `/api/auth/token/refresh/` | — | Refresh access token |
| POST | `/api/contact/` | — | Submit contact form (rate-limited 5/min) |
| POST | `/api/newsletter/` | — | Subscribe to newsletter |
| GET | `/api/blog/` · `/api/blog/{slug}/` | — | Published posts (search, filter) |
| GET | `/api/blog/categories/` | — | Blog categories |
| GET | `/api/careers/` | — | Active job openings |
| POST | `/api/careers/applications/` | — | Apply (multipart, résumé upload) |
| GET | `/api/projects/` · `/api/projects/{slug}/` | — | Portfolio projects |
| GET | `/api/testimonials/` | — | Active testimonials |
| GET | `/api/faqs/` | — | Active FAQs |

Public read endpoints are open; writes to content (blog, projects, etc.) require a JWT.
Public form submissions (contact, newsletter, applications) are open but rate-limited.

## Project Structure

```
backend/
  config/           # settings, urls, wsgi/asgi, celery
  apps/
    core/           # base model, health/root views, `seed` command
    contact/        # contact form (+ Celery email notification)
    newsletter/     # subscriptions
    blog/           # categories + posts
    careers/        # job openings + applications (résumé upload)
    projects/       # portfolio
    testimonials/   # testimonials
    faqs/           # FAQs
  requirements.txt
  .env.example
```

## Background Tasks (Celery)

Without `REDIS_URL`/`CELERY_BROKER_URL` set, tasks run **synchronously** (eager mode) so the
app works out of the box. To run a real worker:

```bash
# set REDIS_URL in .env first
celery -A config worker -l info
```

## Production

- Set `DEBUG=False`, a strong `SECRET_KEY`, and real `ALLOWED_HOSTS` / `CORS_ALLOWED_ORIGINS`.
- Security headers (HSTS, secure cookies, SSL redirect) switch on automatically when `DEBUG=False`.
- Serve with Gunicorn behind Nginx: `gunicorn config.wsgi --bind 0.0.0.0:8000`.
- Run `python manage.py collectstatic` (WhiteNoise serves the compressed output).
- Configure S3 or Cloudinary for media (`MEDIA`) storage.
