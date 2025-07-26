#!/usr/bin/env python3
"""
Debug startup script for Railway deployment
"""

import sys
import os
import logging

# Setup logging with more detail
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

logger.info("=== RAILWAY DEPLOYMENT DEBUG START ===")
logger.info(f"Python version: {sys.version}")
logger.info(f"Current working directory: {os.getcwd()}")
logger.info(f"Python path: {sys.path}")

# Environment variables
logger.info("Environment variables:")
for key, value in os.environ.items():
    if key.startswith(('PORT', 'HOST', 'RAILWAY', 'NIXPACKS')):
        logger.info(f"  {key} = {value}")

# Check file structure
project_dir = os.getcwd()
logger.info(f"Project directory contents: {os.listdir(project_dir)}")

if os.path.exists('models'):
    logger.info(f"Models directory contents: {os.listdir('models')}")
else:
    logger.error("Models directory not found!")

if os.path.exists('src'):
    logger.info(f"Src directory contents: {os.listdir('src')}")
else:
    logger.error("Src directory not found!")

# Test imports
logger.info("Testing imports...")
try:
    sys.path.insert(0, os.path.join(project_dir, 'src'))
    import app
    logger.info("✅ App module imported successfully")
    
    flask_app = app.app
    logger.info("✅ Flask app object retrieved")
    
    # Test basic functionality
    with flask_app.test_client() as client:
        response = client.get('/ping')
        logger.info(f"✅ Ping test: {response.status_code}")
        
except Exception as e:
    logger.error(f"❌ Import error: {e}")
    import traceback
    logger.error(traceback.format_exc())

logger.info("=== RAILWAY DEPLOYMENT DEBUG END ===")

# Now start the actual app
if __name__ == '__main__':
    try:
        from run import *
    except Exception as e:
        logger.error(f"Failed to start main app: {e}")
        sys.exit(1)
