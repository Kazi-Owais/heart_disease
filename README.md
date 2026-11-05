# ❤️ Heart Disease Prediction using Machine Learning

🔗 **Live Demo:** https://heart-disease-prediction-byowaiskazi.streamlit.app/

A Machine Learning project that predicts the likelihood of heart disease using patient health data. The project focuses on building an accurate and interpretable classification model using Logistic Regression and deploying it as an interactive web application with Streamlit.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death worldwide. Early prediction can help healthcare professionals identify high-risk patients and take preventive measures.

This project uses a Logistic Regression model trained on clinical patient data to classify whether a person is likely to have heart disease.

The complete workflow includes:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Data Preprocessing
* Model Training
* Model Evaluation
* Deployment using Streamlit

---

## 🎯 Problem Statement

Given a patient's medical attributes such as age, cholesterol level, chest pain type, and heart rate, predict whether the patient has heart disease.

**Target Variable:**

* 1 → Heart Disease Present
* 0 → No Heart Disease

---

## 📊 Dataset Features

The dataset includes the following medical attributes:

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Resting ECG
* Maximum Heart Rate
* Exercise-Induced Angina
* Oldpeak
* ST Slope

---

## 🤖 Machine Learning Model

### Logistic Regression

Logistic Regression was selected as the final model because it provides:

* Strong performance on classification tasks
* Fast training and prediction
* High interpretability
* Good generalization on unseen data

---

## 📈 Model Performance

| Metric   | Score   |
| -------- | ------- |
| Accuracy | **87%** |
| F1 Score | **85%** |

The model achieved strong classification performance, demonstrating its ability to effectively distinguish between patients with and without heart disease.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

---

## ⚙️ Project Workflow

### 1. Data Preprocessing

* Checked for missing values
* Handled categorical features
* Encoded categorical variables
* Prepared data for model training

### 2. Exploratory Data Analysis

* Analyzed feature distributions
* Identified patterns and correlations
* Visualized important health indicators

### 3. Model Training

* Split data into training and testing sets
* Trained a Logistic Regression classifier
* Evaluated performance using classification metrics

### 4. Deployment

* Saved the trained model
* Built an interactive Streamlit web application
* Enabled real-time predictions through a user-friendly interface

---

## 🚀 Running the Project Locally

Clone the repository:

```bash
git clone https://github.com/Kazi-Owais/heart_disease.git
cd heart_disease
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 🌟 Key Learnings

Through this project, I gained practical experience in:

* Data Cleaning and Preprocessing
* Feature Engineering
* Classification Algorithms
* Logistic Regression
* Model Evaluation
* Streamlit Deployment
* End-to-End Machine Learning Workflow

---

## 👨‍💻 Author

**Owais Kazi**

B.Sc. IT Student | Aspiring Data Scientist & Machine Learning Engineer

GitHub: https://github.com/Kazi-Owais

If you found this project helpful, consider giving it a ⭐ on GitHub.
