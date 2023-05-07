#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#https://docs.djangoproject.com/en/4.2/intro/tutorial01/

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#changed the internal IP to port 8080
#py manage.py runserver 8080
#py manage.py runserver 0.0.0.0:8000