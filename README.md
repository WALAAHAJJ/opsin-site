# Opsin Site — Photography & Videography (Django)

Official website project for a photography/videography business:
- Portfolio gallery (albums + media)
- Reservation requests (admin-managed)

## Tech stack
- Python / Django
- PostgreSQL
- Admin back-office for content management

## Local setup (Windows)
1. Create and activate venv
2. Install dependencies:
   pip install -r requirements.txt
3. Create `.env` from `.env.example`
4. Apply migrations:
   python manage.py migrate
5. Run server:
   python manage.py runserver

## Environment variables
See `.env.example`.

## Git workflow
- `main`: stable
- `develop`: ongoing development
- `feature/*`: features merged via Pull Requests
