import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model/model.pkl", "rb"))

# Page config
st.set_page_config(page_title="House Price Predictor", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏠 House Price Predictor</h1>", unsafe_allow_html=True)
st.write("### Enter property details below:")

# Input layout (2 columns)
col1, col2 = st.columns(2)

with col1:
    size = st.number_input("📏 Size (sq ft)", min_value=100, step=50)
    bedrooms = st.number_input("🛏 Bedrooms", min_value=1, step=1)

with col2:
    bathrooms = st.number_input("🚿 Bathrooms", min_value=1, step=1)
    age = st.number_input("🏚 Age (years)", min_value=0, step=1)

# Location
location = st.selectbox("📍 Location", ["Jaipur", "Delhi", "Mumbai"])

# Button
if st.button("💰 Predict Price"):
    data = {
        "size": size,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "age": age,
        "location_Delhi": 1 if location == "Delhi" else 0,
        "location_Jaipur": 1 if location == "Jaipur" else 0,
        "location_Mumbai": 1 if location == "Mumbai" else 0
    }

    df = pd.DataFrame([data])
    price = model.predict(df)

    st.success(f"🏷 Estimated Price: ₹ {int(price[0]):,}")