import streamlit as st
import pandas as pd

from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport

st.title("Data Profiling App")
st.subheader("This app will help you to do Data Exploration")

st.sidebar.header("User Input Features")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input file", type=["xlsx", "csv"])

if uploaded_file is not None:
    st.markdown("---")

    if uploaded_file.name.endswith(".xlsx"):
        input_df = pd.read_excel(uploaded_file, engine="openpyxl")
    elif uploaded_file.name.endswith(".csv"):
        input_df = pd.read_csv(uploaded_file)
    else:
        st.error("Unsupported file format. Please upload an XLSX or CSV file.")
        st.stop()

    profile = ProfileReport(input_df, title="New Data for profiling")

    st.subheader("Detailed Report of the Data Used")

    st.write(input_df)

    st_profile_report(profile)
else:
    st.write("You did not upload a file")
