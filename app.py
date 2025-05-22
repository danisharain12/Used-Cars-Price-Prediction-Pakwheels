import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st
from pathlib import Path

# Load model and data
BASE_DIR = Path(__file__).resolve().parent
model_path = BASE_DIR / 'used_car_price_prediction.pkl'
with open(model_path, 'rb') as f:
    model = pk.load(f)

data_path = BASE_DIR / 'backup_clean.csv'
data = pd.read_csv(data_path)
data.drop(columns=['location', 'engine_capacity', 'last_updated', 'registered_in'], inplace=True)

cat_features = ['brand', 'model_name', 'province', 'fuel_type', 'transmission', 'color', 'assembly', 'body_type']
unique_categories = {feature: sorted(data[feature].dropna().unique().tolist()) for feature in cat_features}

st.markdown("""
    <div style="text-align: center;">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROchth92QH0mynUSxh5Qp6rCRjiFAl0BB-kg&s" width="100" />
        <h1 style='color: #0A6EBD;'>Pakwheels Used Car Price Predictor</h1>
        <hr style='border: 2px solid #0A6EBD; border-radius: 5px;' />
    </div>
""", unsafe_allow_html=True)

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

# Vehicle Specs Section
st.markdown("""
    <hr style='margin-top:30px; margin-bottom:10px; border: 1px dashed #ccc;' />
    <h3 style='color:#0A6EBD'>Vehicle Specifications</h3>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)
with col3:
    model_year = st.number_input('Model Year', min_value=1960, max_value=2025, value=2020, step=1)
with col4:
    car_age = st.number_input('Car Age (Years)', min_value=0, max_value=65, value=5, step=1)

col5, col6 = st.columns(2)
with col5:
    km_driven = st.number_input('Kilometers Driven (km)', min_value=1, max_value=1_000_000, value=50_000, step=100)
with col6:
    engine_power = st.number_input('Engine Power', min_value=4, max_value=6200, value=1300, step=50)

# DataFrame for prediction
df = pd.DataFrame({
    'brand': [selected_brand],
    'model_name': [selected_model],
    'province': [selected_province],
    'fuel_type': [selected_fuel_type],
    'transmission': [selected_transmission],
    'color': [selected_color],
    'assembly': [selected_assembly],
    'body_type': [selected_body_type],
    'model_year': [model_year],
    'km_driven': [km_driven],
    'engine_power': [engine_power],
    'car_age': [car_age]
})

# Prediction
st.markdown("<hr style='margin-top:30px; margin-bottom:10px;' />", unsafe_allow_html=True)

if st.button('Predict Car Price'):
    prediction = model.predict(df)[0]
    price_in_lakh = round(prediction / 100000, 2)
    price_in_crore = round(prediction / 10000000, 2)

    st.markdown(f"""
        <div style='background-color: #E8F8F5; padding: 30px; border-radius: 10px; border-left: 6px solid #0A6EBD;'>
            <h2 style='color: #0A6EBD;'>Estimated Car Price</h2>
            <h1 style='color: #117A65;'>{price_in_lakh} Lakh PKR</h1>
            <h4 style='color: #148F77;'>(~{price_in_crore} Crore PKR)</h4>
        </div>
    """, unsafe_allow_html=True)
