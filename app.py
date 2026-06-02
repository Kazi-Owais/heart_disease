import streamlit as st
import joblib
import pandas as pd

model = joblib.load('lr_heart.pkl')
scaler = joblib.load('heart_scaler.pkl')
columns = joblib.load('heart_columns.pkl')

st.subheader('❤️ Heart Disease Prediction')
st.markdown('Enter Your Details')
age = st.slider('Age',18,100,25)
sex = st.selectbox('Sex',['Male','Female'])
chest_pain = st.selectbox('ChestPain Type',['ATA','NAP','TA'])
resting_bp = st.number_input('Resting Blood Pressure',80,200,120)
cholesterol  = st.number_input('Cholesterol Level',100,600,200)
fasting_bs = st.selectbox('Fasting Blood Sugar',[1,0])
resting_ecg = st.selectbox('Fasting Blood Sugar',['Normal','ST','LVH'])
max_hr = st.slider('Max Heart Rate',60,220,125)
exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }


    input_df = pd.DataFrame([raw_input])


    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[columns]


    scaled_input = scaler.transform(input_df)


    prediction = model.predict(scaled_input)[0]


    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")