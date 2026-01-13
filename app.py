import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Customer Complaint Analysis Dashboard",
    layout="wide"
)

# Title
st.title("📊 Customer Complaint Analysis Dashboard")
st.write("Upload a CSV or Excel file to analyze customer complaints")

# File uploader (CSV + Excel supported)
uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xls", "xlsx"]
)

if uploaded_file is not None:
    try:
        # Read file based on extension
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        # Dataset preview
        st.subheader("📄 Dataset Preview")
        st.dataframe(df.head())

        # Dataset information
        st.subheader("📌 Dataset Information")
        col1, col2 = st.columns(2)
        col1.metric("Number of Rows", df.shape[0])
        col2.metric("Number of Columns", df.shape[1])

        # Column selection for analysis
        st.subheader("📊 Column-wise Analysis")
        selected_column = st.selectbox(
            "Select a column to analyze",
            df.columns
        )

        # Value counts visualization
        value_counts = df[selected_column].value_counts().head(10)

        st.write(f"Top 10 values in **{selected_column}**")
        st.bar_chart(value_counts)

        st.success("✅ Analysis completed successfully")

    except Exception as e:
        st.error("❌ Error while processing the file")
        st.error(e)

else:
    st.info("ℹ️ Please upload a CSV or Excel file to continue")
