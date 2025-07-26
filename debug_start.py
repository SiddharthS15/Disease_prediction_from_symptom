#!/usr/bin/env python3
"""
Minimal Flask app for Railway deployment
"""

import sys
import os
import logging
from flask import Flask, jsonify

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create minimal Flask app that always works
app = Flask(__name__)

@app.route('/')
def home():
    return "Disease Prediction System is running!"

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'disease-prediction',
        'port': os.environ.get('PORT', '5000')
    })

if __name__ == '__main__':
    # Get port from Railway
    port = int(os.environ.get('PORT', 5000))
    logger.info(f"Starting Flask app on port {port}")
    
    # Start the app
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False,
        threaded=True
    )
