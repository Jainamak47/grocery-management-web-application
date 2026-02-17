# Flask to Django Migration Guide

## Overview
This guide helps you migrate from the Flask backend to Django backend for the Grocery Store Management System.

## What Changed

### Backend Framework
- **Before**: Flask (backend/server.py)
- **After**: Django (grocery_django/)

### Project Structure
```
grocery_django/
├── manage.py                 # Django management script
├── grocery_store/            # Project settings
│   ├── settings.py          # Configuration
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI config
├── store/                    # Main app
│   ├── models.py            # Database models (ORM)
│   ├── views.py             # API endpoints
│   └── urls.py              # App URL routing
└── requirements.txt          # Dependencies
```

### Key Differences

| Aspect | Flask | Django |
|--------|-------|--------|
| Port | 5000 | 8000 |
| Database | Raw SQL queries | Django ORM |
| Routing | @app.route decorators | urls.py patterns |
| Models | Manual SQL tables | Django Models |
| Admin | None | Built-in admin panel |

## Migration Steps

### 1. Install Django Dependencies
```bash
cd grocery_django
pip install -r requirements.txt
```

Required packages:
- Django >= 5.0
- mysqlclient >= 2.2.0

### 2. Configure Database
Edit `grocery_store/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grocery_store',
        'USER': 'root',           # Your MySQL username
        'PASSWORD': '0000',       # Your MySQL password
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 3. Update Frontend API URLs
Replace in `ui/js/custom/common.js`:
- Change all `http://127.0.0.1:5000/` to `http://127.0.0.1:8000/`

Or use the provided `common_django.js` file.

### 4. Start Django Server
```bash
# Option 1: Using the batch script
start_django.bat

# Option 2: Manual command
cd grocery_django
python manage.py runserver 8000
```

### 5. Test the Application
1. Open `ui/index.html` in your browser
2. Test all features:
   - View products
   - Add/delete products
   - Create orders
   - View orders

## API Endpoints (Unchanged)

All API endpoints remain the same:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /getProducts | Get all products |
| POST | /insertProduct | Add new product |
| POST | /deleteProduct | Delete product |
| GET | /getAllOrders | Get all orders |
| POST | /insertOrder | Create new order |

## Benefits of Django

1. **ORM**: No more raw SQL queries
2. **Admin Panel**: Built-in admin interface at `/admin/`
3. **Security**: Better CSRF protection and security features
4. **Scalability**: Better structure for large applications
5. **Documentation**: Extensive Django documentation
6. **Community**: Large Django community and ecosystem

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Database Connection Error
- Verify MySQL is running
- Check credentials in settings.py
- Ensure database 'grocery_store' exists

### Module Not Found
```bash
pip install -r requirements.txt
```

## Rollback to Flask

If you need to go back to Flask:
1. Stop Django server
2. Start Flask server: `python backend/server.py`
3. Change frontend URLs back to port 5000

## Next Steps

1. **Add Admin User** (optional):
```bash
python manage.py createsuperuser
```
Access admin at: http://127.0.0.1:8000/admin/

2. **Add UOM Endpoint**: Implement the missing getUOM endpoint in views.py

3. **Add Invoice Generation**: Port the invoice_generator.py to Django

4. **Deploy**: Consider using Gunicorn + Nginx for production
