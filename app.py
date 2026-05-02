import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline,CustomData

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻")
st.title("💻 Laptop Price Intelligence Engine")

col1, col2 = st.columns(2)
with col1:
    brand = st.selectbox("Brand", ["ASUS", "HP", "MOTOROLA", "Lenovo", "MICROSOFT", "Acer", "DELL", "MSI", "Samsung", "Apple"])
    ram = st.selectbox("RAM (GB)", [4, 8, 16, 24, 32, 64])
    storage = st.selectbox("Storage (GB)", [128, 256, 512, 1024, 2048])
    os = st.selectbox("Operating System", ["Windows 11", "Windows 10", "DOS"])

with col2:
    processor = st.selectbox("Processor", ["Intel Core i5", "Intel Core Ultra", "Snapdragon X", "AMD Ryzen 5", "Intel Core i3", "Intel Core i7", "AMD Ryzen 7", "AMD Ryzen 3", "Intel Core i9"])
    graphics = st.selectbox("Graphics", ["Integrated", "6 GB Graphics", "4 GB Graphics", "8 GB Graphics", "2 GB Graphics", "AMD Radeon"])
    original_price = st.number_input("Original Price (₹)", min_value=10000, max_value=500000, value=80000)
    discount_pct = st.number_input("Discount %", min_value=0.0, max_value=95.0, value=10.0)



st.write("Enter laptop specs to predict the fair market price")

if st.button("Predict Price 🔍"):
    data = CustomData(
        brand=brand,
        ram=ram,
        storage=storage,
        original_price=original_price,
        discount_price=discount_pct,
        processor=processor,
        graphics=graphics,
        os=os
    )
    
    df = data.get_data_as_dataframe()
    
    pipeline = PredictPipeline()
    result = pipeline.predict(df)
    
    st.success(f"💰 Predicted Price: ₹{result[0]:,.0f}")