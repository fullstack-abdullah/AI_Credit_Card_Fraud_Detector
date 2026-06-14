# 🛡️ AI Credit Card Fraud Detection System

An end-to-end Machine Learning web application that detects fraudulent credit card transactions in real-time with **90% sensitivity (Recall)** using Advanced Imbalance Data Handling (SMOTE) and Logistic Regression.

## 🚀 Live Demo
Experience the live interactive web application here:
🔗 **[Live AI Fraud Detector App](https://aicreditcardfrauddetector-f6uanke5upkend3ver5vfg.streamlit.app/)**

---

## 📊 Project Overview & Business Impact
Credit card fraud costs financial institutions billions annually. Traditional models often fail because fraud cases are extremely rare (less than 0.2% of total data). 

This project solves the **Class Imbalance Problem** using synthetic data generation to train a highly defensive AI engine capable of spotting hidden fraudulent patterns before they cause financial damage.

### Key Milestones Achieved:
* **Exploratory Data Analysis (EDA):** Analyzed highly skewed anonymized PCA features ($V1$ to $V28$).
* **Handling Extreme Imbalance:** Leveraged **SMOTE (Synthetic Minority Over-sampling Technique)** to artificially boost fraud samples for optimal training.
* **Performance Boost:** Raised the Fraud Catch Rate (Recall) from **71% up to a highly secure 90%**.
* **Production Deployment:** Developed a clean user-friendly grid UI using Streamlit and deployed it for public access.

---

## 🛠️ Tech Stack & Libraries Used
* **Language:** Python
* **Machine Learning:** Scikit-Learn
* **Imbalance Handling:** Imbalanced-Learn (SMOTE)
* **Web Framework:** Streamlit
* **Arrays & Matrices:** NumPy & Pandas
* **Model Serialization:** Pickle

---

## 💾 How to Run Locally

1. Clone this repository:
```bash
   git clone [https://github.com/fullstack-abdullah/AI_Credit_Card_Fraud_Detector.git](https://github.com/fullstack-abdullah/AI_Credit_Card_Fraud_Detector.git)
