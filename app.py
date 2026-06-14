import streamlit as st
import pickle
import numpy as np

# 1. Load the pre-trained AI model configuration parameters
with open('fraud_detector_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# 2. Set up the dynamic web page interface title headers
st.set_page_config(page_title="AI Credit Card Fraud Detector", layout="centered")
st.title("🛡️ AI Credit Card Fraud Detection System")
st.write("Enter the transaction details below to evaluate if the transaction is Safe or Fraudulent.")

st.divider()

# 3. Create interactive numerical entry grid data input vectors
st.subheader("📊 Transaction Features")
st.write("Provide values for key anonymized transaction features:")

# Partitioning presentation layers via structural rendering columns
col1, col2 = st.columns(2)

with col1:
    v1 = st.number_input("Feature V1", value=0.0)
    v2 = st.number_input("Feature V2", value=0.0)
    v3 = st.number_input("Feature V3", value=0.0)
    v4 = st.number_input("Feature V4", value=0.0)
    v14 = st.number_input("Critical Feature V14", value=0.0)

with col2:
    v17 = st.number_input("Critical Feature V17", value=0.0)
    v12 = st.number_input("Feature V12", value=0.0)
    v10 = st.number_input("Feature V10", value=0.0)
    time = st.number_input("Transaction Time (Seconds)", value=0.0)
    amount = st.number_input("Transaction Amount ($)", value=10.0)

st.divider()

# 4. Deployment validation trigger engine evaluation routine
if st.button("🚀 Run Fraud Diagnostics", type="primary"):
    # Initializing data vectors mapping back to original dimensional formats
    input_features = np.zeros(30)
    input_features[0] = time
    input_features[1] = v1
    input_features[2] = v2
    input_features[3] = v3
    input_features[4] = v4
    input_features[10] = v10
    input_features[12] = v12
    input_features[14] = v14
    input_features[17] = v17
    input_features[29] = amount
    
    # Executing predictive algorithms using structured array parsing shapes
    prediction = model.predict(input_features.reshape(1, -1))
    
    # Conditional output dashboard metrics evaluation logs rendering block
    if prediction[0] == 1:
        st.error("🚨 WARNING: High Risk of Fraud Detected! Immediate investigation recommended.")
    else:
        st.success("🟢 SUCCESS: Transaction evaluated as Low Risk (Safe).")