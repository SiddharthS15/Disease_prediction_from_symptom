from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import pandas as pd
import os

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, 
            template_folder=os.path.join(project_root, 'templates'),
            static_folder=os.path.join(project_root, 'static'))

# Load the trained model and data
try:
    models_path = os.path.join(project_root, 'models')
    model = joblib.load(os.path.join(models_path, 'disease_prediction_model.pkl'))
    symptoms_list = joblib.load(os.path.join(models_path, 'symptoms_list.pkl'))
    disease_descriptions = joblib.load(os.path.join(models_path, 'disease_descriptions.pkl'))
    disease_precautions = joblib.load(os.path.join(models_path, 'disease_precautions.pkl'))
    symptom_severity = joblib.load(os.path.join(models_path, 'symptom_severity.pkl'))
    print("Model and data loaded successfully!")
except FileNotFoundError as e:
    print(f"Error loading files: {e}")
    print("Please run the Jupyter notebook first to train the model.")

class DiseasePredictor:
    def __init__(self, model, symptoms_list, descriptions, precautions, severity):
        self.model = model
        self.symptoms_list = symptoms_list
        self.descriptions = descriptions
        self.precautions = precautions
        self.severity = severity
    
    def predict_disease(self, input_symptoms):
        """
        Predict disease based on input symptoms
        """
        # Create feature vector as pandas DataFrame to match training format
        import pandas as pd
        feature_dict = {symptom: 1 if symptom in input_symptoms else 0 for symptom in self.symptoms_list}
        feature_vector = pd.DataFrame([feature_dict])
        
        # Make prediction
        prediction = self.model.predict(feature_vector)[0]
        
        # Get prediction probabilities
        if hasattr(self.model, 'predict_proba'):
            probabilities = self.model.predict_proba(feature_vector)[0]
            confidence = max(probabilities)
            
            # Get top 3 predictions
            top_indices = np.argsort(probabilities)[-3:][::-1]
            top_diseases = self.model.classes_[top_indices]
            top_probabilities = probabilities[top_indices]
        else:
            confidence = 0.8  # Default confidence for models without predict_proba
            top_diseases = [prediction]
            top_probabilities = [confidence]
        
        return prediction, confidence, top_diseases, top_probabilities
    
    def get_disease_info(self, disease):
        """
        Get description and precautions for a disease
        """
        description = self.descriptions.get(disease, "Description not available.")
        precautions = self.precautions.get(disease, [])
        return description, precautions
    
    def calculate_severity_score(self, symptoms):
        """
        Calculate total severity score based on symptoms
        """
        total_score = 0
        for symptom in symptoms:
            # Clean symptom name (remove spaces and underscores)
            clean_symptom = symptom.strip().replace(' ', '_')
            score = self.severity.get(clean_symptom, 1)  # Default score of 1
            total_score += score
        return total_score

# Initialize predictor
try:
    predictor = DiseasePredictor(model, symptoms_list, disease_descriptions, 
                               disease_precautions, symptom_severity)
except NameError:
    predictor = None

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html', symptoms=symptoms_list if predictor else [])

@app.route('/predict', methods=['POST'])
def predict():
    """Predict disease based on selected symptoms"""
    if not predictor:
        return jsonify({'error': 'Model not loaded. Please train the model first.'})
    
    try:
        # Get selected symptoms from form
        selected_symptoms = request.json.get('symptoms', [])
        print(f"DEBUG: Received symptoms: {selected_symptoms}")
        
        if not selected_symptoms:
            return jsonify({'error': 'Please select at least one symptom.'})
        
        # Make prediction
        predicted_disease, confidence, top_diseases, top_probabilities = predictor.predict_disease(selected_symptoms)
        print(f"DEBUG: Predicted disease: {predicted_disease}, Confidence: {confidence}")
        
        # Get disease information
        description, precautions = predictor.get_disease_info(predicted_disease)
        
        # Calculate severity score
        severity_score = predictor.calculate_severity_score(selected_symptoms)
        
        # Prepare top predictions
        top_predictions = []
        for disease, prob in zip(top_diseases, top_probabilities):
            desc, prec = predictor.get_disease_info(disease)
            top_predictions.append({
                'disease': disease,
                'probability': round(prob * 100, 2),
                'description': desc,
                'precautions': prec
            })
        
        result = {
            'predicted_disease': predicted_disease,
            'confidence': round(confidence * 100, 2),
            'description': description,
            'precautions': precautions,
            'severity_score': severity_score,
            'selected_symptoms': selected_symptoms,
            'top_predictions': top_predictions
        }
        
        print(f"DEBUG: Returning result: {result}")
        return jsonify(result)
    
    except Exception as e:
        print(f"DEBUG: Error occurred: {str(e)}")
        return jsonify({'error': f'An error occurred: {str(e)}'})

@app.route('/symptoms')
def get_symptoms():
    """Get all available symptoms"""
    if not predictor:
        return jsonify({'error': 'Model not loaded.'})
    
    return jsonify({'symptoms': symptoms_list})

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/health')
def health_check():
    """Health check endpoint"""
    status = {
        'status': 'healthy',
        'model_loaded': predictor is not None,
        'total_symptoms': len(symptoms_list) if predictor else 0
    }
    return jsonify(status)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
