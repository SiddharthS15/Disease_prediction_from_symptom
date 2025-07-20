"""
Quick Model Training Script
This script trains the disease prediction model directly from command line.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import warnings
warnings.filterwarnings('ignore')

def main():
    print("=" * 60)
    print("Disease Prediction Model Training")
    print("=" * 60)
    
    # Load datasets
    print("Loading datasets...")
    df = pd.read_csv('../data/dataset.csv')
    description_df = pd.read_csv('../data/symptom_Description.csv')
    precaution_df = pd.read_csv('../data/symptom_precaution.csv')
    severity_df = pd.read_csv('../data/Symptom-severity.csv')
    
    print(f"✓ Training data: {len(df)} samples, {df['Disease'].nunique()} diseases")
    print(f"✓ Disease descriptions: {len(description_df)} diseases")
    print(f"✓ Precautions: {len(precaution_df)} diseases")
    print(f"✓ Symptom severity: {len(severity_df)} symptoms")
    
    # Get all unique symptoms
    print("\nExtracting symptoms...")
    symptoms = []
    for i in range(1, 18):
        col_name = f'Symptom_{i}'
        if col_name in df.columns:
            symptoms.extend(df[col_name].dropna().str.strip().unique())
    
    symptoms = list(set([s for s in symptoms if s and s.strip()]))
    symptoms.sort()
    print(f"✓ Found {len(symptoms)} unique symptoms")
    
    # Create binary encoding for symptoms
    print("\nCreating feature matrix...")
    feature_matrix = pd.DataFrame(0, index=df.index, columns=symptoms)
    
    for idx, row in df.iterrows():
        for i in range(1, 18):
            col_name = f'Symptom_{i}'
            if col_name in df.columns and pd.notna(row[col_name]):
                symptom = row[col_name].strip()
                if symptom in symptoms:
                    feature_matrix.loc[idx, symptom] = 1
    
    X = feature_matrix
    y = df['Disease']
    
    print(f"✓ Feature matrix: {X.shape}")
    
    # Split the data
    print("\nSplitting data...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print(f"✓ Training set: {X_train.shape[0]} samples")
    print(f"✓ Test set: {X_test.shape[0]} samples")
    
    # Train multiple models
    print("\nTraining models...")
    models = {
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
        'SVM': SVC(kernel='rbf', random_state=42, probability=True),
        'Naive Bayes': GaussianNB()
    }
    
    model_scores = {}
    trained_models = {}
    
    for name, model in models.items():
        print(f"\nTraining {name}...")
        
        # Train the model
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        
        # Cross-validation score
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)
        
        model_scores[name] = {
            'accuracy': accuracy,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std()
        }
        
        trained_models[name] = model
        
        print(f"  ✓ Test Accuracy: {accuracy:.4f}")
        print(f"  ✓ CV Score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
    
    # Select the best model
    print("\nModel Performance Comparison:")
    for name, scores in model_scores.items():
        print(f"  {name}: {scores['accuracy']:.4f} accuracy, {scores['cv_mean']:.4f} CV")
    
    best_model_name = max(model_scores.items(), key=lambda x: x[1]['accuracy'])[0]
    best_model = trained_models[best_model_name]
    
    print(f"\n🏆 Best Model: {best_model_name}")
    print(f"   Accuracy: {model_scores[best_model_name]['accuracy']:.4f}")
    
    # Save the best model and necessary data
    print("\nSaving model and data...")
    
    # Save the trained model
    joblib.dump(best_model, '../models/disease_prediction_model.pkl')
    print("✓ Saved: ../models/disease_prediction_model.pkl")
    
    # Save the symptom list
    joblib.dump(symptoms, '../models/symptoms_list.pkl')
    print("✓ Saved: ../models/symptoms_list.pkl")
    
    # Save disease descriptions and precautions as dictionaries
    description_dict = dict(zip(description_df['Disease'], description_df['Description']))
    joblib.dump(description_dict, '../models/disease_descriptions.pkl')
    print("✓ Saved: ../models/disease_descriptions.pkl")
    
    # Create precaution dictionary
    precaution_dict = {}
    for _, row in precaution_df.iterrows():
        precautions = []
        for i in range(1, 5):
            col_name = f'Precaution_{i}'
            if col_name in precaution_df.columns and pd.notna(row[col_name]):
                precautions.append(row[col_name])
        precaution_dict[row['Disease']] = precautions
    
    joblib.dump(precaution_dict, '../models/disease_precautions.pkl')
    print("✓ Saved: ../models/disease_precautions.pkl")
    
    # Save severity dictionary
    severity_dict = dict(zip(severity_df['Symptom'], severity_df['weight']))
    joblib.dump(severity_dict, '../models/symptom_severity.pkl')
    print("✓ Saved: ../models/symptom_severity.pkl")
    
    # Test the model
    print("\nTesting model with sample symptoms...")
    test_symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions']
    feature_vector = [1 if symptom in test_symptoms else 0 for symptom in symptoms]
    feature_vector = np.array(feature_vector).reshape(1, -1)
    
    prediction = best_model.predict(feature_vector)[0]
    confidence = best_model.predict_proba(feature_vector).max()
    
    print(f"  Test symptoms: {test_symptoms}")
    print(f"  Predicted disease: {prediction}")
    print(f"  Confidence: {confidence:.4f}")
    
    print("\n" + "=" * 60)
    print("✅ Model training completed successfully!")
    print("✅ All files saved and ready for use!")
    print("\nNext step: Run the Flask app with 'python app.py'")
    print("=" * 60)

if __name__ == "__main__":
    main()
