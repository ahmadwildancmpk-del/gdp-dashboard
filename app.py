import streamlit as st
import pandas as pd

st.set_page_config(page_title="Seismic Data App", layout="wide")

st.title("📊 Seismic Data Dashboard")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data.csv")

st.subheader("Preview Data")
st.dataframe(df)

st.subheader("Basic Info")
st.write(df.describe())

st.subheader("Columns")
column = st.selectbox("Select column to visualize", df.columns)

st.line_chart(df[column])

st.success("App running successfully 🚀")
