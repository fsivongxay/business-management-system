# Business Management System

A Django web application for managing business information and data.

## Features

- Add and manage business information
- View business listings
- Responsive web interface
- PostgreSQL database support
- Ready for production deployment

## Local Development

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`
5. Visit: http://127.0.0.1:8000/

## Deployment

This project is configured for deployment on Railway with:
- PostgreSQL database
- Gunicorn web server
- Whitenoise for static files
- Automatic migrations

**Last updated: August 10, 2025 - Ready for Railway deployment!**
