import streamlit as st
import pandas as pd
import joblib

model = joblib.load('spare_part_prediction_model.pkl')
st.divider()
st.header('Enter the Months of Failure Counts')
col1 , col2 = st.columns(2)

with col1:
    st.subheader('Equipment Failures')
    pump = st.number_input('Pump Failure', 0,20,0,1)
    motor = st.number_input('Motor Failure', 0,20,0,1)
    compressor = st.number_input('Compressor Failure', 0,20,0,1)
    
with col2:
    st.subheader('More Equipment')
    conveyor = st.number_input('Conveyor Failure', 0,20,0,1)
    boiler = st.number_input('Boiler Failure', 0,20,0,1)
    cooling = st.number_input('Cooling Fan Failure', 0,20,0,1)

st.divider()

st.header('Predict Next Month Stock')
if st.button("📦 Predict Next Part", type="primary", use_container_width=True):
    
    input_data = pd.DataFrame({
        'Month': [1],                   
        'Pump_Failures': [pump],
        'Motor_Failures': [motor],
        'Compressor_Failures': [compressor],
        'Conveyor_Failures': [conveyor],
        'Boiler_Failures': [boiler],
        'Cooling_Failures': [cooling]
    })
    
    # Model se prediction lo
    predicted = model.predict(input_data)[0]
    
   
    st.divider()
    st.header("🎯 Prediction Result")
    st.success(f"## Next Month Stock: {predicted}")
    
   
    st.info(f"💡 **Recommendation:** Order {predicted} in advance to avoid downtime.")
    
    # Input summary table
    st.subheader("📋 This Month's Failure Summary")
    summary = pd.DataFrame({
        'Equipment': ['Pump', 'Motor', 'Compressor', 'Conveyor', 'Boiler', 'Cooling Fan'],
        'Failures': [pump, motor, compressor, conveyor, boiler, cooling]
    })
    st.table(summary)

st.divider()
st.caption("Built by Irfan")
