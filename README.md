# 🧠 Disease Prediction from Symptoms

A web-based machine learning project that predicts diseases based on user-selected symptoms. Built with Python, Flask, and a trained ML model, the application provides predictions, precautions, and detailed information about diseases.

---

## � Table of Contents

- [📸 Screenshots](#-screenshots)
  - [🏠 Home Page](#-home-page)
  - [🤒 Symptoms Selection](#-symptoms-selection)
  - [🧪 Disease Prediction Output](#-disease-prediction-output)
  - [💊 Precaution Suggestions](#-precaution-suggestions)
  - [⚙️ Tech Stack Overview](#️-tech-stack-overview)
- [🚀 Features](#-features)
- [🧰 Tech Stack](#-tech-stack)
- [🖥️ How to Run on Your PC](#️-how-to-run-on-your-pc)
  - [📋 Prerequisites](#-prerequisites)
  - [📂 Project Setup](#-project-setup)
    - [Method 1: Download ZIP (Easier)](#method-1-download-zip-easier)
    - [Method 2: Clone with Git](#method-2-clone-with-git)
  - [🔧 Installation Steps](#-installation-steps)
  - [🚀 Running the Application](#-running-the-application)
  - [📱 Using the Application](#-using-the-application)
  - [🔧 Troubleshooting](#-troubleshooting)
- [📁 Project Structure](#-project-structure)
- [🎯 Features Overview](#-features-overview)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Developer](#-developer)
- [🙏 Acknowledgments](#-acknowledgments)

---

## �📸 Screenshots

### 🏠 Home Page
![Home](screenshots/home.png)

### 🤒 Symptoms Selection
![Symptoms](screenshots/symptoms.png)

### 🧪 Disease Prediction Output
![Prediction](screenshots/prediction.png)

### 💊 Precaution Suggestions
![Precautions](screenshots/precuation.png)

### ⚙️ Tech Stack Overview
![Tech Stack](screenshots/tech%20stack.png)

---

## 🚀 Features

- Predicts disease based on selected symptoms.
- Shows disease description and severity.
- Provides precautions to follow.
- User-friendly interface built with HTML/CSS/JS and Flask.

---

## 🧰 Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn
- **Data Handling**: Pandas, NumPy
- **Model Persistence**: Pickle (`.pkl`)

---

## 🖥️ How to Run on Your PC

### 📋 Prerequisites

Before running this project, make sure you have the following installed on your computer:

1. **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
2. **Git** (optional) - [Download Git](https://git-scm.com/downloads/)

### 📂 Project Setup

#### Method 1: Download ZIP (Easier)
1. Click the green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract the ZIP file to your desired location
4. Open Command Prompt/Terminal and navigate to the extracted folder

#### Method 2: Clone with Git
```bash
git clone https://github.com/SiddharthS15/Disease_prediction_from_symptom.git
cd Disease_prediction_from_symptom
```

### 🔧 Installation Steps

1. **Open Command Prompt/Terminal** in the project directory

2. **Create a Virtual Environment** (Recommended)
   ```bash
   # For Windows
   python -m venv disease_prediction_env
   disease_prediction_env\Scripts\activate
   
   # For macOS/Linux
   python3 -m venv disease_prediction_env
   source disease_prediction_env/bin/activate
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   pip list
   ```

### 🚀 Running the Application

1. **Start the Flask Server**
   ```bash
   python run.py
   ```

2. **Access the Application**
   - Open your web browser
   - Go to: `http://localhost:5000` or `http://127.0.0.1:5000`
   - The application should load successfully!

3. **Stop the Server**
   - Press `Ctrl + C` in the terminal to stop the server

### 📱 Using the Application

1. **Home Page**: Navigate through the modern, responsive interface
2. **Select Symptoms**: Choose symptoms from the comprehensive list
3. **Get Prediction**: Click "Predict Disease" to get results
4. **View Results**: See disease prediction, description, and precautions
5. **Dark Mode**: Toggle between light and dark themes using the theme button
6. **Help**: Click the help button for usage instructions

### 🔧 Troubleshooting

#### Common Issues and Solutions:

**Problem**: `ModuleNotFoundError`
```bash
# Solution: Install missing packages
pip install flask pandas numpy scikit-learn
```

**Problem**: `Port already in use`
```bash
# Solution: Use a different port
python run.py --port 5001
```

**Problem**: Models not loading
- Ensure all `.pkl` files are in the `models/` directory
- Check if the CSV files are in the `data/` directory

**Problem**: Python not recognized
- Add Python to your system PATH
- Use `python3` instead of `python` on macOS/Linux

### 📁 Project Structure
```
Disease_prediction_from_symptom/
├── data/                     # Dataset files
│   ├── dataset.csv
│   ├── symptom_Description.csv
│   ├── symptom_precaution.csv
│   └── Symptom-severity.csv
├── models/                   # Trained ML models
│   ├── disease_prediction_model.pkl
│   ├── symptoms_list.pkl
│   ├── disease_descriptions.pkl
│   ├── disease_precautions.pkl
│   └── symptom_severity.pkl
├── src/                      # Source code
│   ├── app.py               # Flask application
│   └── train_model.py       # Model training script
├── static/                   # Static files
│   ├── css/style.css        # Styling
│   └── js/script.js         # JavaScript
├── templates/               # HTML templates
│   ├── base.html
│   ├── index.html
│   └── about.html
├── requirements.txt         # Dependencies
├── run.py                  # Application entry point
└── README.md               # This file
```

### 🎯 Features Overview

- **🔮 Disease Prediction**: AI-powered disease prediction from symptoms
- **📊 Severity Assessment**: Understanding disease severity levels
- **💡 Smart Recommendations**: Personalized precautions and advice
- **🌙 Dark Mode**: Modern UI with light/dark theme toggle
- **📱 Responsive Design**: Works on desktop, tablet, and mobile
- **⚡ Fast Performance**: Optimized for quick predictions
- **🔒 Privacy Focused**: No data stored, completely local processing

### 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

### 👨‍💻 Developer

**Siddharth S** - [GitHub Profile](https://github.com/SiddharthS15)

### 🙏 Acknowledgments

- Machine Learning algorithms for disease prediction
- Flask framework for web development
- Bootstrap for responsive UI components
- Medical datasets for training the model

---

⭐ **Star this repository if you found it helpful!** ⭐
