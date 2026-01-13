import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Complaint Analysis", layout="wide")

st.title("📊 Customer Complaint Analysis")
st.write("Upload a CSV file to analyze customer complaints")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        st.subheader("Dataset Info")
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

        if df.shape[1] > 0:
            col = df.columns[0]
            st.subheader(f"Distribution of {col}")
            fig, ax = plt.subplots()
            df[col].value_counts().head(10).plot(kind="bar", ax=ax)
            st.pyplot(fig)

    except Exception as e:
        st.error("Error while reading the file")
        st.error(e)
else:
    st.info("Please upload a CSV file to continue")
