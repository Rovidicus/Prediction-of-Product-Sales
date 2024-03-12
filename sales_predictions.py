# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO

# Title
st.title("Grocery Sales Investigation")

# Dataset
df = pd.read_csv("Data/sales_prepped.csv")

# Display an interactive dataframe
st.header("Item Sales Dataframe")
st.dataframe(df, width=800)

# Display descriptive statistics
st.markdown('#### Descriptive Statistics')
if st.button("Show Descriptive Statistics"):
    st.dataframe(df.describe().round(2))

st.markdown('#### Summary Info')
if st.button("Show Summary Info"):
    # Capture .info()
    # Create a string buffer to capture the content
    buffer = StringIO()
    # Write the info into the buffer
    df.info(buf=buffer)
    # Retrieve the content from the buffer
    summary_info = buffer.getvalue()
    # Use Streamlit to display the info
    st.text(summary_info)

st.markdown('#### Null Values')
if st.button("Show Null Values"):
    nulls = df.isna().sum()
    st.dataframe(nulls)
    # Making string buffer to capture content
    buffer = StringIO()
    # Write nulls into the buffer
    df.isna().sum().to_string(buffer)
