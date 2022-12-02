import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def apps():
    st.title("Categorical Feature")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    cp_df = pd.read_csv('2021June-July_product_data.csv')

    #3.2 categorical feature
    cp_df['product_category'].value_counts().plot(kind='bar')
    st.pyplot()
    if st.checkbox("Show Data"):
            st.subheader("Data")
            st.write(cp_df['product_category'].value_counts())