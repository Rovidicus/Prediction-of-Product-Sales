# Imports
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import plotly.express as px
import plotly.io as pio


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

# Use plotly for explore functions
def plotly_explore_numeric(df, x):
    fig = px.histogram(df,x=x,marginal='box',title=f'Distribution of {x}', 
                      width=1000, height=500)
    return fig
def plotly_explore_categorical(df, x):
    fig = px.histogram(df,x=x,color=x,title=f'Distribution of {x}', 
                          width=1000, height=500)
    fig.update_layout(showlegend=False)
    return fig
# Add a selectbox for all possible features
column = st.selectbox(label="Select a column", options=df.columns, key="col")
# Conditional statement to determine which function to use
if df[column].dtype == 'object':
    fig = plotly_explore_categorical(df, column)
else:
    fig = plotly_explore_numeric(df, column)
    
st.markdown("#### Displaying appropriate Plotly plot based on selected column")
# Display appropriate eda plots
st.plotly_chart(fig)


# functionizing numeric vs target
def plotly_numeric_vs_target(df, x, y='Item_Outlet_Sales', trendline='ols',add_hoverdata=True):
    if add_hoverdata == True:
        hover_data = list(df.columns)
    else: 
        hover_data = None
        
    pfig = px.scatter(df, x=x, y=y,width=800, height=600,
                     hover_data=hover_data,
                      trendline=trendline,
                      trendline_color_override='red',
                     title=f"{x} vs. {y}")
    
    pfig.update_traces(marker=dict(size=3),
                      line=dict(dash='dash'))
    return pfig

# functionizing categoric vs target
def plotly_categoric_vs_target(df, x, y = 'Item_Outlet_Sales', histfunc = 'avg', width=800, height=500):
    fig = px.histogram(df, x=x,y=y, color=x, width=width, height=height,
                       histfunc=histfunc, title=f'Compare {histfunc.title()} {y} by {x}')
    fig.update_layout(showlegend=False)
    fig.update_layout(showlegend=False)
    return fig

X = df.drop(columns="Item_Outlet_Sales").copy()
# Add a selectbox for all possible features
column2 = st.selectbox(label="Select a column", options = X.columns, key="col2")
# Conditional statement to determine which function to use
if df[column2].dtype == 'object':
    fig = plotly_categoric_vs_target(df, column2)
else:
    fig = plotly_numeric_vs_target(df, column2)
st.markdown("#### Plotly numeric or categoric vs target")
# Display appropriate eda plots
st.plotly_chart(fig)


