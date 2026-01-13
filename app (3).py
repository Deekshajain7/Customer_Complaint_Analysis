import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Complaint Analysis", layout="wide")

st.title("📊 Customer Complaint Analysis Dashboard")

st.write("Analyze customer complaints using data analytics and visualization.")

# Upload CSV
uploaded_file = st.file_uploader("Upload Customer Complaint CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # Example Visualization
    if "Product" in df.columns:
        st.subheader("📌 Complaints by Product")
        product_count = df["Product"].value_counts().head(10)

        fig, ax = plt.subplots()
        product_count.plot(kind="bar", ax=ax)
        st.pyplot(fig)

    st.success("Analysis Completed Successfully ✅")
