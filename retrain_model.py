#!/usr/bin/env python3
"""
Model compatibility fixer for Railway deployment
"""

import joblib
import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def retrain_model():
    """Retrain the model with current scikit-learn version"""
    try:
        project_root = os.getcwd()
        data_path = os.path.join(project_root, 'data')
        models_path = os.path.join(project_root, 'models')
        
        # Load dataset
        df = pd.read_csv(os.path.join(data_path, 'dataset.csv'))
        logger.info(f"Loaded dataset with {len(df)} samples")
        
        # Prepare features and target
        feature_cols = [col for col in df.columns if col != 'Disease']
        X = df[feature_cols]
        y = df['Disease']
        
        logger.info(f"Features: {len(feature_cols)}, Classes: {len(y.unique())}")
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train a simple, compatible model
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=2
        )
        
        logger.info("Training model...")
        model.fit(X_train, y_train)
        
        # Test accuracy
        accuracy = model.score(X_test, y_test)
        logger.info(f"Model accuracy: {accuracy:.3f}")
        
        # Save the retrained model
        joblib.dump(model, os.path.join(models_path, 'disease_prediction_model.pkl'))
        logger.info("Model saved successfully!")
        
        return True
        
    except Exception as e:
        logger.error(f"Model retraining failed: {e}")
        return False

if __name__ == '__main__':
    retrain_model()
