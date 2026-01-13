import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Customer Complaint Analysis Dashboard",
    layout="wide"
)

st.title("📊 Customer Complaint Analysis Dashboard")
st.write("Upload a CSV or Excel file to analyze customer complaints")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xls", "xlsx"]
)

if uploaded_file is not None:
    try:
        file_name = uploaded_file.name.lower()

        # Read file based on extension
        if file_name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)

        elif file_name.endswith(".xlsx"):
            df = pd.read_excel(uploaded_file, engine="openpyxl")

        elif file_name.endswith(".xls"):
            df = pd.read_excel(uploaded_file, engine="xlrd")

        else:
            st.error("Unsupported file format")
            st.stop()

        # Preview
        st.subheader("📄 Dataset Preview")
        st.dataframe(df.head())

        # Dataset info
        st.subheader("📌 Dataset Information")
        col1, col2 = st.columns(2)
        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])

        # Column-wise analysis
        st.subheader("📊 Column-wise Analysis")
        selected_column = st.selectbox(
            "Select a column",
            df.columns
        )

        top_values = df[selected_column].value_counts().head(10)
        st.write(f"Top 10 values in **{selected_column}**")
        st.bar_chart(top_values)

        st.success("✅ File processed successfully")

    except Exception as e:
        st.error("❌ Error while processing the file")
        st.code(str(e))

else:
    st.info("ℹ️ Please upload a CSV or Excel file to continue")
