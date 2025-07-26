#!/usr/bin/env python3
"""
WSGI entry point for Railway deployment
"""

import sys
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Change to the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)

# Add src directory to Python path
sys.path.insert(0, os.path.join(project_dir, 'src'))

try:
    # Import the Flask app
    from app import app
    
    # WSGI application for gunicorn
    application = app
    
    logger.info("WSGI application initialized successfully")
    
except Exception as e:
    logger.error(f"Failed to initialize WSGI application: {e}")
    import traceback
    traceback.print_exc()
    raise

if __name__ == '__main__':
    # For testing the WSGI app locally
    application.run(debug=False, host='0.0.0.0', port=5000)
