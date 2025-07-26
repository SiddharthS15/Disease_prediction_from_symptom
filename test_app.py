#!/usr/bin/env python3
"""
Test script to verify the Flask app can be imported and started
"""

import sys
import os

# Add the project directory to path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(project_dir, 'src'))

print("Testing Flask app import...")
try:
    from app import app, predictor
    print("✅ Flask app imported successfully")
    print(f"✅ Predictor loaded: {predictor is not None}")
    
    # Test a simple route
    with app.test_client() as client:
        response = client.get('/ping')
        print(f"✅ Ping test: {response.status_code} - {response.get_data(as_text=True)}")
        
        response = client.get('/health')
        print(f"✅ Health test: {response.status_code} - {response.get_json()}")
        
    print("✅ All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
