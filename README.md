# Business Management System

A Django web application for managing business information and contacts.

## Features

- **Business Listings**: View all businesses in a clean, organized list
- **Add New Business**: Add new businesses with contact information
- **Business Details**: Store name, address, phone, email, website, and description

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Visit `http://127.0.0.1:8000/`

## Deployment on Railway

This project is configured for easy deployment on Railway.

### Steps to Deploy:

1. **Create a Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with your GitHub account

2. **Connect Your Repository**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Add Database**
   - In your Railway project, click "New"
   - Select "Database" → "PostgreSQL"
   - Railway will automatically set the `DATABASE_URL` environment variable

4. **Deploy**
   - Railway will automatically detect it's a Django app
   - It will install dependencies from `requirements.txt`
   - Run migrations and start the server

5. **Access Your App**
   - Railway will provide a URL like `https://your-app-name.railway.app`
   - Your app will be live!

## Environment Variables

Railway automatically sets:
- `DATABASE_URL`: PostgreSQL connection string
- `PORT`: Port number for the application

## Project Structure

```
myproject/
├── businessdata/          # Main app
│   ├── models.py         # Business model
│   ├── views.py          # View functions
│   ├── forms.py          # Business form
│   ├── urls.py           # App URLs
│   └── templates/        # HTML templates
├── myproject/            # Project settings
│   ├── settings.py       # Django settings
│   └── urls.py           # Main URLs
├── requirements.txt      # Python dependencies
├── railway.json          # Railway configuration
└── nixpacks.toml         # Build configuration
```

## Technologies Used

- **Django 5.2.4**: Web framework
- **PostgreSQL**: Database (production)
- **SQLite**: Database (development)
- **Gunicorn**: WSGI server (production)
- **Whitenoise**: Static file serving
- **Railway**: Deployment platform
