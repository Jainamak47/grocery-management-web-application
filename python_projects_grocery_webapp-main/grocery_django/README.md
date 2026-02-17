# Grocery Store Management System - Django Version

This is the Django migration of the Flask-based grocery store management application.

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Database
Update the database credentials in `grocery_store/settings.py` if needed:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grocery_store',
        'USER': 'root',
        'PASSWORD': '0000',  # Change this
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 3. Run Migrations (Optional - if creating new database)
```bash
python manage.py makemigrations
python manage.py migrate
```

Note: If you're using the existing MySQL database from the Flask app, skip migrations as the tables already exist.

### 4. Run the Server
```bash
python manage.py runserver 8000
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

All endpoints remain the same as the Flask version:
- GET `/getProducts` - Get all products
- POST `/insertProduct` - Add new product
- POST `/deleteProduct` - Delete product
- GET `/getAllOrders` - Get all orders
- POST `/insertOrder` - Create new order

## Frontend

The frontend HTML/CSS/JS files remain in the `../ui/` folder. Update the API base URL in the JavaScript files from port 5000 to 8000.

## Key Differences from Flask

1. **Framework**: Django instead of Flask
2. **ORM**: Django ORM instead of raw SQL queries
3. **Port**: Default port 8000 instead of 5000
4. **Structure**: Django MVT pattern (Models, Views, Templates)
5. **Admin Panel**: Built-in admin interface at `/admin/`
