#!/usr/bin/env python3
"""
Disease Prediction System Launcher
Run this script to start the Flask web application.
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
    
    if __name__ == '__main__':
        logger.info("Starting Disease Prediction System...")
        
        # Get port from environment variable (Railway sets this)
        port = int(os.environ.get('PORT', 5000))
        host = os.environ.get('HOST', '0.0.0.0')
        
        logger.info(f"Binding to host: {host}, port: {port}")
        
        # For local development
        if os.environ.get('RAILWAY_ENVIRONMENT') is None:
            logger.info("Running in development mode")
            logger.info("Open your browser and go to: http://localhost:5000")
            app.run(debug=True, host=host, port=port)
        else:
            # For production (Railway)
            logger.info("Running in production mode on Railway")
            app.run(debug=False, host=host, port=port, threaded=True)
            
except Exception as e:
    logger.error(f"Failed to start application: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
