

import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from apps import data
import  numpy as np
import pandas as pd




arr_output = np.array([item for sublist in data.list_features for item in sublist])
# data.list_features
list_input_data=[data.data_all,data.data_string]
# col1 = st.beta_columns(3)
# col2 = st.beta_columns(3)
# col3 = st.beta_columns(3)
# Use the full page instead of a narrow central column

# Space out the maps so the first one is 2x the size of the other three


def plotFigure(list_input_data):
    # st.write(data.list_features)
    col1 = st.beta_columns(3)
    col2 = st.beta_columns(3)
    col3 = st.beta_columns(3)
    st.subheader("Modelisation")
    arr_output=[item for sublist in data.list_features[2:] for item in sublist]
    sns.set()

    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4, aspect=1)
    fig.map(sns.kdeplot, 'AGE', shade=True)
    plt.axvline(arr_output[14], color='red')
    col1[0].pyplot(fig)

    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4, aspect=1)
    fig.map(sns.kdeplot, 'DAYS_EMPLOYED', shade=True)
    plt.axvline(arr_output[10], color='red')
    col1[1].pyplot(fig)

    fig, ax = plt.subplots(figsize=(16, 10))
    ax.hist(list_input_data[1][['CODE_GENDER','TARGET']])
    col1[2].pyplot(fig)

    fig, ax = plt.subplots(figsize=(16, 10))
    ax.hist(list_input_data[1][['NAME_FAMILY_STATUS','TARGET']])
    col2[0].pyplot(fig)


    fig, ax = plt.subplots(figsize=(16, 10))
    ax.hist(list_input_data[1][['FLAG_OWN_CAR','TARGET']])
    col2[1].pyplot(fig)


    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4, aspect=1)
    fig.map(sns.kdeplot, 'CNT_CHILDREN', shade=True)
    col2[2].pyplot(fig)

    fig, ax = plt.subplots()
    ax.hist(list_input_data[1][['FLAG_OWN_REALTY','TARGET']])
    col3[0].pyplot(fig)


    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4,size=4, aspect=1)
    fig.map(sns.kdeplot, 'AMT_INCOME_TOTAL', shade=True)
    plt.axvline(arr_output[10], color='red')
    col3[1].pyplot(fig)

    fig, ax = plt.subplots(figsize=(16, 10))
    fig = sns.FacetGrid(list_input_data[0], hue='TARGET', height=4, aspect=1)
    fig.map(sns.kdeplot, 'AMT_CREDIT', shade=True)
    plt.axvline(arr_output[11], color='red')
    col3[2].pyplot(fig)

