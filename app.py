import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / 'used_car_price_prediction.pkl'

with open(model_path, 'rb') as f:
    model = pk.load(f)

data_path = BASE_DIR / 'backup_clean.csv'
data = pd.read_csv(data_path)

data.drop(columns=['location', 'engine_capacity', 'last_updated', 'registered_in'], inplace=True)

cat_features = ['brand', 'model_name', 'province', 'fuel_type', 'transmission', 'color', 'assembly', 'body_type']
unique_categories = {feature: sorted(data[feature].dropna().unique().tolist()) for feature in cat_features}

st.markdown("<h1 style='text-align: center; color: #0A6EBD;'>Pakwheels Used Car Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("### Select Car Features")

col1, col2 = st.columns(2)

with col1:
    selected_brand = st.selectbox('Brand', unique_categories['brand'])
    selected_province = st.selectbox('Province', unique_categories['province'])
    selected_fuel_type = st.selectbox('Fuel Type', unique_categories['fuel_type'])
    selected_color = st.selectbox('Color', unique_categories['color'])

with col2:
    selected_model = st.selectbox('Model Name', unique_categories['model_name'])
    selected_transmission = st.selectbox('Transmission', unique_categories['transmission'])
    selected_assembly = st.selectbox('Assembly Type', unique_categories['assembly'])
    selected_body_type = st.selectbox('Body Type', unique_categories['body_type'])

# Numerical Inputs
st.markdown("### Vehicle Specifications")

col3, col4 = st.columns(2)

with col3:
    model_year = st.slider('Model Year', 1960, 2025, 2020)

with col4:
    car_age = st.slider('Car Age', 0, 65, 5, step=1)

col5, col6 = st.columns(2)

with col5:
    km_driven = st.slider('Kilometers Driven', 1, 1000000, 50000, step=1)

with col6:
    engine_power = st.slider('Engine Power', 4, 6200, 1300, step=1)

df = pd.DataFrame({'brand': [selected_brand],'model_name': [selected_model],'province': [selected_province],'fuel_type': [selected_fuel_type],
                   'transmission': [selected_transmission],'color': [selected_color],'assembly': [selected_assembly],'body_type': [selected_body_type],'model_year': [model_year],
                   'km_driven': [km_driven],'engine_power': [engine_power],'car_age': [car_age]})

st.markdown("---")
if st.button('Predict Car Price'):
    prediction = model.predict(df)[0]
    price_in_lakh = round(prediction / 100000, 2)
    price_in_crore = round(prediction / 10000000, 2)

    st.markdown(f"""
    <div style='background-color: #D1F2EB; padding: 20px; border-radius: 10px;'>
        <h2 style='color: #117864;'>Estimated Car Price:</h2>
        <h1 style='color: #0B5345;'>{price_in_lakh} Lakh</h1>
        <h4 style='color: #148F77;'>(~{price_in_crore} Crore)</h4>
    </div>
    """, unsafe_allow_html=True)
