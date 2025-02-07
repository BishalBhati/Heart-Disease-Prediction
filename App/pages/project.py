import streamlit as st
import pickle

st.subheader("Input your details to check for heart disease risk :")

input1, input2, input3 , input4 = st.columns(4)

with input1:
    age = int(st.number_input("Enter age"))

    gender = st.selectbox("Enter gender", ("Male", "Female"), index=None)

    chestpain = st.selectbox("Enter chestpain type", ("asymptomatic", "atypical angina", "non-anginal pain", "typical angina"), index=None)

with input2:
    cholestrol = int(st.number_input("Enter cholestrol value"))

    fbs = st.selectbox("Enter fasting blood sugar", (0,1), index=None)

    restecg = st.selectbox("Enter resting ecg value", (0,1,2), index=None)

with input3:
    eia = st.selectbox("Enter post-exercise angina", (0,1), index=None)

    oldpeak = int(st.number_input("Enter oldpeak value"))

    major_vessels = st.select_slider("Number of major vessels", options=[0,1,2,3,4])

with input4:
    slope = st.selectbox("Enter slope value", (0,1,2), index=None)

    max_heart_rate = int(st.number_input("Enter maximum heart rate"))

    thal = st.selectbox("Enter thalassemia type", ("fixed defect", "normal blood flow", "reversible defect"), index=None)

rbp = int(st.number_input("Resting blood pressure"))

col1 , col2 = st.columns(2)

# Importing the model and running it

model = pickle.load(open("C:\\Users\\BISHAL BHATI\\Pictures\\Code\\ParnaSoft\\Day-18\\Heart Disease Detection Model\\Heart_Disease_Detection_Model_Using_LR", "rb"))

if gender == 'Male':
    gender = 0
else:
    gender = 1

if chestpain == 'asymptomatic':
    chestpain = 1
elif chestpain == 'atypical angina':
    chestpain = 2
elif chestpain == 'non-anginal pain':
    chestpain = 3
else:
    chestpain = 4

if thal == 'fixed defect':
    thal = 1
elif thal == 'normal blood flow':
    thal = 2
else:
    thal = 3

with col1:
    run = st.button("Run & Predict", type="primary")

with col2:
    if run:
        result = model.predict([[age,gender,chestpain,rbp,cholestrol,fbs,restecg,max_heart_rate,eia,oldpeak,slope,major_vessels,thal]])
        result = result[0]

        if result == 0:
            st.success("You have a healthy heart.", icon=":material/check_circle:")
        else:
            st.error("You have an unhealthy heart.", icon=":material/cancel:")

