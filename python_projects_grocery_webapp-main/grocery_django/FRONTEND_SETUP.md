# Frontend Configuration for Django Backend

## Update API URLs

To connect the existing frontend to the Django backend, update the port from 5000 to 8000 in:

**File: `ui/js/custom/common.js`**

Change:
```javascript
var productListApiUrl = 'http://127.0.0.1:5000/getProducts';
var uomListApiUrl = 'http://127.0.0.1:5000/getUOM';
var productSaveApiUrl = 'http://127.0.0.1:5000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:5000/deleteProduct';
var orderListApiUrl = 'http://127.0.0.1:5000/getAllOrders';
var orderSaveApiUrl = 'http://127.0.0.1:5000/insertOrder';
```

To:
```javascript
var productListApiUrl = 'http://127.0.0.1:8000/getProducts';
var uomListApiUrl = 'http://127.0.0.1:8000/getUOM';
var productSaveApiUrl = 'http://127.0.0.1:8000/insertProduct';
var productDeleteApiUrl = 'http://127.0.0.1:8000/deleteProduct';
var orderListApiUrl = 'http://127.0.0.1:8000/getAllOrders';
var orderSaveApiUrl = 'http://127.0.0.1:8000/insertOrder';
```

## Serve Static Files

Option 1: Open HTML files directly in browser (simple for development)
Option 2: Serve through Django static files (recommended for production)

### Option 2 Setup:
1. Copy the `ui` folder to `grocery_django/store/static/`
2. Update `settings.py`:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'store/static']
```
3. Access at: `http://127.0.0.1:8000/static/index.html`
