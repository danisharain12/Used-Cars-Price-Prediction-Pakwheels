# Car Price Prediction Web App

A **Machine Learning-powered Streamlit app** that predicts the prices of used cars based on real-time data scraped from [PakWheels](https://www.pakwheels.com/).  
This end-to-end project covers web scraping, data preprocessing, EDA, model building, evaluation, and deployment.

---

## 🔗 Live App

👉 [Try the App Here](https://danisharain12-used-cars-price-prediction-pakwheels-app-9mtcuv.streamlit.app/)

---

## 📂 Project Structure

├── backup_clean/ # Raw & cleaned dataset
├── Used_car_price_prediction_Pakwheels/ # EDA and model training notebooks
├── app/ # Streamlit app scripts
├── used_car_price_predictor/ # Saved ML models (Pickle)
├── requirements.txt
└── README.md

---

## 📌 Features

- Scraped **10,000+ car listings** from PakWheels using **BeautifulSoup**
- Performed **data cleaning** and **feature engineering** on real-world messy data
- Conducted **Exploratory Data Analysis (EDA)** to understand feature impact
- Trained and evaluated multiple ML models to predict car prices:
  - ✅ Random Forest Regressor
  - ⚠️ KNN Regressor
  - 🌳 Decision Tree Regressor
  - 📉 Linear, Ridge, and Lasso Regression
- Deployed a **Streamlit web app** for real-time price prediction

---

## 🧠 Model Performance Summary

| Model                   | Train R² | Test R² | RMSE    | Notes                             |
|------------------------|----------|---------|---------|-----------------------------------|
| Random Forest           | 0.97     | 0.857   | ~2.6M   | Best generalization               |
| KNN Regressor           | 0.9999   | 0.871   | —       | Overfitting observed              |
| Decision Tree           | 0.94     | 0.857   | —       | Interpretable but less stable     |
| Ridge/Lasso/Linear Reg. | 0.77–0.79| 0.77–0.79| —      | Poor fit for complex relationships|

---

## 🔍 Key Features Influencing Price

- Engine Power  
- KM Driven  
- Model Year / Car Age  
- Fuel Type  
- Transmission  
- Brand and Body Type  

---

## 🛠️ Tech Stack

- **Python**
- **BeautifulSoup** (Web Scraping)
- **pandas, NumPy, Matplotlib, Seaborn** (EDA)
- **scikit-learn** (Modeling)
- **Streamlit** (Deployment)

---
## Contat

- Danish Karim
- danisharain253@gmail.com
