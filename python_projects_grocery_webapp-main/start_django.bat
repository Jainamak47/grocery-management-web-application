@echo off
echo ========================================
echo Grocery Store Django Server
echo ========================================
echo.
echo Starting Django development server...
echo Server will be available at: http://127.0.0.1:8000
echo.
echo Press CTRL+C to stop the server
echo ========================================
echo.

cd grocery_django
python manage.py runserver 8000
