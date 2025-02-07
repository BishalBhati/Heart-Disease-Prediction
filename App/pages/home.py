import streamlit as st

st.set_page_config(layout="wide")

st.title("Heart Disease Prediction")

col1 , col2 = st.columns(2, gap="large")

with col1:
    st.write("The Heart Disease Prediction model is designed to assist in identifying the risk of heart disease in individuals based on various health metrics. Leveraging a machine learning algorithm, this model analyzes a range of factors such as age, cholesterol levels, blood pressure, and other relevant medical data to predict the likelihood of heart disease. The goal is to provide a tool that can aid healthcare professionals in making more informed decisions by highlighting potential risk areas.")

with col2:
    st.image("C:\\Users\\BISHAL BHATI\\Pictures\\Code\\ParnaSoft\\Day-18\\Heart Disease Detection Model\\App\\img.png", width=250)

st.write("This model is built using a dataset that includes numerous patient records, ensuring a robust and comprehensive analysis. The algorithm has been trained and tested on this data, allowing it to recognize patterns and correlations that may not be immediately apparent through traditional methods. The model's accuracy and reliability make it a valuable resource for early detection, potentially leading to better patient outcomes through timely intervention.")

st.write("In this Streamlit application, you can explore the model's predictions and understand how different factors contribute to the overall risk. The user-friendly interface allows for easy interaction, providing insights into the model's functioning and the significance of various health indicators. Whether you are a healthcare professional or someone interested in understanding heart disease risks, this tool offers a clear and accessible way to engage with predictive analytics in healthcare.")

