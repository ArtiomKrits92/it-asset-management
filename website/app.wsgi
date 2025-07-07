import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, "/home/ubuntu/it_asset_app")

from app import application  # import your Flask app's WSGI callable
