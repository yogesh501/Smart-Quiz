"""
WSGI entry point for production deployments (Render, PythonAnywhere, etc.)
"""
from app import app

# For WSGI servers that look for 'application'
application = app

if __name__ == "__main__":
    app.run()
