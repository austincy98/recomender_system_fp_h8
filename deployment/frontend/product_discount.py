import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def apps():
        st.title("Product Discount and lowest guarantee and rating")
        st.set_option('deprecation.showPyplotGlobalUse', False)

        cp_df = pd.read_csv('2021June-July_product_data.csv')
        cp_df.groupby(by=['product_category','feature_lowest_price_guarantee']).product_total_rating.agg(["mean"]).plot(kind='barh')
        st.pyplot()
        if st.checkbox("Show Data"):
                st.subheader("Data")
                st.write(cp_df.groupby(by=['product_category','feature_lowest_price_guarantee']).product_total_rating.agg(["mean"]))