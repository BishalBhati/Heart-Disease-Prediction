import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

st.title("Dataset")

df = pd.read_csv("C:\\Users\\BISHAL BHATI\\Pictures\\Code\\ParnaSoft\\Day-18\\Heart Disease Detection Model\\data.csv")

st.write(df.sample(8))
