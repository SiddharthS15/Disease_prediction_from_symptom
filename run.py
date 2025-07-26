#!/usr/bin/env python3
"""
Disease Prediction System Launcher
Run this script to start the Flask web application.
"""

import sys
import os
import logging
import time

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("Starting Disease Prediction System initialization...")

# Change to the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)
logger.info(f"Working directory: {project_dir}")

# Add src directory to Python path
sys.path.insert(0, os.path.join(project_dir, 'src'))
logger.info(f"Added to Python path: {os.path.join(project_dir, 'src')}")

# Check if required directories exist
models_dir = os.path.join(project_dir, 'models')
data_dir = os.path.join(project_dir, 'data')
src_dir = os.path.join(project_dir, 'src')

logger.info(f"Models directory exists: {os.path.exists(models_dir)}")
logger.info(f"Data directory exists: {os.path.exists(data_dir)}")
logger.info(f"Src directory exists: {os.path.exists(src_dir)}")

if os.path.exists(models_dir):
    logger.info(f"Models directory contents: {os.listdir(models_dir)}")

try:
    logger.info("Importing Flask app...")
    # Import the Flask app
    from app import app
    
    # WSGI application for gunicorn
    application = app
    
    logger.info("Flask app imported successfully!")
    
    if __name__ == '__main__':
        logger.info("Starting Flask server...")
        
        # Get port from environment variable (Railway sets this)
        port = int(os.environ.get('PORT', 5000))
        host = os.environ.get('HOST', '0.0.0.0')
        
        logger.info(f"Server will bind to host: {host}, port: {port}")
        
        # Check if running on Railway
        is_railway = os.environ.get('RAILWAY_ENVIRONMENT') is not None
        logger.info(f"Running on Railway: {is_railway}")
        
        if not is_railway:
            # For local development
            logger.info("Running in development mode")
            logger.info("Open your browser and go to: http://localhost:5000")
            app.run(debug=True, host=host, port=port)
        else:
            # For production (Railway)
            logger.info("Running in production mode on Railway")
            logger.info("Starting Flask server with threading enabled...")
            app.run(debug=False, host=host, port=port, threaded=True, use_reloader=False)
            
except Exception as e:
    logger.error(f"Failed to start application: {e}")
    import traceback
    logger.error(traceback.format_exc())
    sys.exit(1)
