import streamlit as st
import pickle
import numpy as np

# Load the model
filename = "model.sav"
with open(filename, 'rb') as file:
    classifier = pickle.load(file)


# Streamlit app
st.title("Purchase Prediction App")
st.write("Welcome to the Purchase Prediction App! This app predicts whether a customer will purchase an item based on their age and estimated salary.")


# User input for age
age = st.number_input("Enter Age", min_value=0, max_value=120, value=34)


# User input for estimated salary
estimated_salary = st.number_input("Enter Estimated Salary", min_value=0, value=765580)

# Button to make prediction
if st.button("Predict"):

    prediction = classifier.predict([[age, estimated_salary]])
    
    # Display prediction result
    st.subheader("Prediction Result:")
    if prediction == 1:
        st.success("Item will be purchased")
    else:
        st.error("Item will not be purchased")
