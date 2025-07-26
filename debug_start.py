#!/usr/bin/env python3
"""
Disease Prediction Flask App for Railway
"""

import sys
import os
import logging
from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the project root directory
project_root = os.getcwd()

# Create Flask app
app = Flask(__name__, 
            template_folder=os.path.join(project_root, 'templates'),
            static_folder=os.path.join(project_root, 'static'))

# Initialize variables
model = None
symptoms_list = []
disease_descriptions = {}
disease_precautions = {}
symptom_severity = {}
predictor = None

# Load the trained model and data with error handling
try:
    models_path = os.path.join(project_root, 'models')
    logger.info(f"Loading models from: {models_path}")
    
    # Try loading the model
    try:
        model = joblib.load(os.path.join(models_path, 'disease_prediction_model.pkl'))
        logger.info("Model loaded successfully!")
    except Exception as model_error:
        logger.warning(f"Model loading failed: {model_error}")
        logger.info("Attempting to retrain model with compatible version...")
        
        # Try to retrain the model
        try:
            from retrain_model import retrain_model
            if retrain_model():
                model = joblib.load(os.path.join(models_path, 'disease_prediction_model.pkl'))
                logger.info("Model retrained and loaded successfully!")
            else:
                raise Exception("Model retraining failed")
        except Exception as retrain_error:
            logger.error(f"Model retraining failed: {retrain_error}")
            model = None
    
    # Load other data files
    symptoms_list = joblib.load(os.path.join(models_path, 'symptoms_list.pkl'))
    disease_descriptions = joblib.load(os.path.join(models_path, 'disease_descriptions.pkl'))
    disease_precautions = joblib.load(os.path.join(models_path, 'disease_precautions.pkl'))
    symptom_severity = joblib.load(os.path.join(models_path, 'symptom_severity.pkl'))
    
    logger.info("All data files loaded successfully!")
    
    # Simple predictor class
    class DiseasePredictor:
        def __init__(self, model, symptoms_list, descriptions, precautions, severity):
            self.model = model
            self.symptoms_list = symptoms_list
            self.descriptions = descriptions
            self.precautions = precautions
            self.severity = severity
        
        def predict_disease(self, input_symptoms):
            try:
                # Create feature vector
                feature_dict = {symptom: 1 if symptom in input_symptoms else 0 for symptom in self.symptoms_list}
                feature_vector = pd.DataFrame([feature_dict])
                
                # Make prediction
                prediction = self.model.predict(feature_vector)[0]
                
                # Get confidence if possible
                confidence = 0.85  # Default confidence
                if hasattr(self.model, 'predict_proba'):
                    try:
                        probabilities = self.model.predict_proba(feature_vector)[0]
                        confidence = max(probabilities)
                    except:
                        pass
                
                return prediction, confidence, [prediction], [confidence]
            except Exception as e:
                logger.error(f"Prediction error: {e}")
                return "Unknown", 0.5, ["Unknown"], [0.5]
        
        def get_disease_info(self, disease):
            description = self.descriptions.get(disease, "Description not available.")
            precautions = self.precautions.get(disease, [])
            return description, precautions
        
        def calculate_severity_score(self, symptoms):
            total_score = 0
            for symptom in symptoms:
                clean_symptom = symptom.strip().replace(' ', '_')
                score = self.severity.get(clean_symptom, 1)
                total_score += score
            return total_score
    
    # Initialize predictor
    predictor = DiseasePredictor(model, symptoms_list, disease_descriptions, 
                               disease_precautions, symptom_severity)
    logger.info("Predictor initialized successfully!")
    
except Exception as e:
    logger.error(f"Error loading models: {e}")
    logger.error("App will start with limited functionality")

# Routes
@app.route('/')
def index():
    """Home page"""
    if predictor:
        return render_template('index.html', symptoms=symptoms_list)
    else:
        return "Disease Prediction System is starting up... Models not loaded yet."

@app.route('/predict', methods=['POST'])
def predict():
    """Predict disease based on symptoms"""
    if not predictor:
        return jsonify({
            'error': 'Prediction model not available',
            'message': 'Please try again later'
        }), 503
    
    try:
        data = request.get_json()
        symptoms = data.get('symptoms', [])
        
        if not symptoms:
            return jsonify({'error': 'No symptoms provided'}), 400
        
        # Make prediction
        disease, confidence, top_diseases, top_probabilities = predictor.predict_disease(symptoms)
        
        # Get disease info
        description, precautions = predictor.get_disease_info(disease)
        
        # Calculate severity
        severity_score = predictor.calculate_severity_score(symptoms)
        
        return jsonify({
            'disease': disease,
            'confidence': float(confidence),
            'description': description,
            'precautions': precautions,
            'severity_score': severity_score,
            'selected_symptoms': symptoms
        })
        
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({
            'error': 'Prediction failed',
            'message': str(e)
        }), 500

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': predictor is not None,
        'total_symptoms': len(symptoms_list),
        'service': 'disease-prediction'
    })

@app.route('/ping')
def ping():
    """Simple ping endpoint"""
    return 'pong'

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
