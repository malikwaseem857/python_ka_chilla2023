import pandas as pd
import streamlit as st
import seaborn as sns

from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Load dataset
df = sns.load_dataset("titanic")

# Create profile report
profile = ProfileReport(df, explorative=True)

# Streamlit app
st.title("Titanic Dataset EDA Report")
st_profile_report(profile)

