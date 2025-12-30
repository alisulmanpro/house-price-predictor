import joblib
import streamlit as st
import numpy as np

# Load model
model = joblib.load('model.joblib')

# Reserve a spot at the top
result_placeholder = st.empty()  # This will show the result at the top

# Title
st.title('House Price Prediction')
st.write("Enter house details below to predict its price.")

# Input fields
bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=20, value=None, placeholder='e.g. 3')
bathrooms = st.number_input("Number of Bathrooms", min_value=0.0, max_value=10.0, value=None, step=0.25, placeholder='e.g. 2.00')
sqft_living = st.number_input("Living Area (sqft)", min_value=100, max_value=20000, value=None, placeholder='e.g. 2000')
floors = st.number_input("Number of Floors", min_value=1.0, max_value=5.0, value=None, step=0.5, placeholder='e.g. 1.0')
grade = st.number_input("House Grade (1-13)", min_value=1, max_value=13, value=None, placeholder='e.g. 7')

if st.button('Predict Price'):
    # Prepare input array
    input_features = np.array([[bedrooms, bathrooms, sqft_living, floors, grade]])
    # Make prediction
    pred_price = model.predict(input_features)
    # Display the result at the top with custom stylingx
    result_placeholder.markdown(
        f"<h4 style='background-color: {"#28a745" if pred_price[0] < 500000 else "#CF6679"}; padding: 10px; border-radius: 10px; text-align:center;'>Predicted House Price: ${pred_price[0]:,.2f}</h4>",
        unsafe_allow_html=True
    )
