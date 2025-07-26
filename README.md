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
- [🚀 Deploy on Railway](#-deploy-on-railway)
  - [📋 Prerequisites for Deployment](#-prerequisites-for-deployment)
  - [🔧 Deployment Steps](#-deployment-steps)
  - [⚙️ Environment Configuration](#️-environment-configuration)
  - [🌐 Accessing Your Deployed App](#-accessing-your-deployed-app)
  - [🔧 Troubleshooting Deployment](#-troubleshooting-deployment)
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

---

## 🚀 Deploy on Railway

Deploy your Disease Prediction System to the cloud with Railway for free! Railway provides an easy way to deploy web applications with automatic builds and deployments.

### 📋 Prerequisites for Deployment

1. **GitHub Account** - Your code needs to be on GitHub
2. **Railway Account** - Sign up at [railway.app](https://railway.app) (free)
3. **Pushed Repository** - Your code should be pushed to GitHub

### 🔧 Deployment Steps

#### Step 1: Prepare Your Repository
```bash
# Make sure all files are committed and pushed to GitHub
git add .
git commit -m "Prepare for Railway deployment"
git push origin main
```

#### Step 2: Deploy on Railway
1. **Go to Railway** - Visit [railway.app](https://railway.app)
2. **Sign In** - Use your GitHub account to sign in
3. **Create New Project** - Click "New Project"
4. **Deploy from GitHub** - Select "Deploy from GitHub repo"
5. **Choose Repository** - Select your `Disease_prediction_from_symptom` repository
6. **Deploy** - Railway will automatically detect and deploy your Flask app

#### Step 3: Automatic Configuration
Railway automatically detects:
- ✅ Python application
- ✅ Flask framework
- ✅ Dependencies from `requirements.txt`
- ✅ Start command from `Procfile`

### ⚙️ Environment Configuration

Railway automatically handles:
- **Port Configuration** - Uses `PORT` environment variable
- **Build Process** - Installs dependencies automatically
- **Start Command** - Uses `python run.py` from Procfile
- **Health Checks** - Monitors application health

### 🌐 Accessing Your Deployed App

1. **Build Process** - Wait for Railway to build (2-5 minutes)
2. **Get URL** - Railway provides a unique URL like `your-app-name.railway.app`
3. **Test Application** - Your disease prediction system is now live!

#### Example Deployed URLs:
```
https://disease-prediction-production.railway.app
https://your-app-name.railway.app
```

### 🔧 Troubleshooting Deployment

#### Common Issues and Solutions:

**Problem**: `ModuleNotFoundError: No module named 'distutils'` or Python 3.12 compatibility issues
```bash
# Solution: Use Python 3.11 (specified in runtime.txt and .python-version)
# Railway will automatically use the correct Python version
# Updated requirements.txt with compatible package versions
```

**Problem**: Build fails due to memory limits
```bash
# Solution: Reduce dependencies or use Railway Pro
# Removed unnecessary packages like jupyter and ipykernel from requirements.txt
```

**Problem**: Package version conflicts
```bash
# Solution: Updated all packages to compatible versions
# Flask 3.0.0, scikit-learn 1.4.0, pandas 2.1.4, etc.
```

**Problem**: App doesn't start
- Check Railway logs in the dashboard
- Ensure `Procfile` exists with correct start command
- Verify all required files are in the repository

**Problem**: Models not loading
- Ensure all `.pkl` files are committed to the repository
- Check file paths are relative, not absolute
- Verify `models/` and `data/` directories are included

**Problem**: Port binding issues
- Railway automatically sets the `PORT` environment variable
- The updated `run.py` handles this automatically

#### Checking Deployment Logs:
1. Go to Railway dashboard
2. Select your project
3. Click on "Deployments"
4. View build and runtime logs

### 📊 Deployment Features

- **🔄 Automatic Deployments** - Updates when you push to GitHub
- **📈 Usage Monitoring** - Track app performance and usage
- **🔧 Environment Variables** - Configure settings without code changes
- **📱 Custom Domains** - Add your own domain (Pro plan)
- **⚡ Fast CDN** - Global content delivery network
- **🔒 HTTPS** - Automatic SSL certificates

### 💰 Railway Pricing

- **Starter Plan** - Free ($0/month)
  - 512MB RAM
  - 1GB disk
  - Shared CPU
  - Perfect for this project!

- **Pro Plan** - $5/month
  - More resources
  - Custom domains
  - Priority support

### 🎯 Post-Deployment Tips

1. **Test All Features** - Verify symptom selection and prediction work
2. **Check Performance** - Monitor response times
3. **Update Repository** - Push updates to auto-deploy
4. **Monitor Usage** - Use Railway dashboard for insights
5. **Share Your App** - Your disease prediction system is now accessible worldwide!

### 🔗 Useful Railway Commands

```bash
# Install Railway CLI (optional)
npm install -g @railway/cli

# Login to Railway
railway login

# Deploy from command line
railway up

# Check deployment status
railway status

# View logs
railway logs
```

---

## 🤝 Contributing

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
