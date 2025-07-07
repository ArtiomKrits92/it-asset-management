import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/var/www/it-asset-management")

from app import app as application  # import your Flask app's WSGI callable
