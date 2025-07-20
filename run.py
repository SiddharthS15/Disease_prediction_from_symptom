#!/usr/bin/env python3
"""
Disease Prediction System Launcher
Run this script to start the Flask web application.
"""

import sys
import os

# Change to the project directory
project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)

# Add src directory to Python path
sys.path.insert(0, os.path.join(project_dir, 'src'))

# Import and run the Flask app
from app import app

if __name__ == '__main__':
    print("Starting Disease Prediction System...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
