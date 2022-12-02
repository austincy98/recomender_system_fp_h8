import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def apps():
    st.title("Top Product by Total Product Sold")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    cp_df = pd.read_csv('2021June-July_product_data.csv')


    # Grouping Top viewstop_views
    product_name_sold = cp_df.groupby(by=['product_name']).sum().round(2)
    # Sorting
    product_name_sold = product_name_sold.sort_values('units_sold', ascending=False).head(20)
    #plot the top Products with most sales

    # Define size
    plt.figure(figsize=[20,6])
    # Define Bar
    plt.bar(product_name_sold.index, product_name_sold.units_sold, color='#EF0107', edgecolor='#B31B1B')
    # Define font rotation
    plt.xticks(rotation=90)
    # Define Title and label
    plt.title("TOP PRODUCTS SOLD", fontsize=16)
    plt.xlabel('PRODUCT', fontsize=14)
    plt.ylabel('UNIT SOLD', fontsize=14)
    # Define Text
    for i, v in product_name_sold.units_sold.items():
        if v>60000:
            plt.text(i, v-15000, s='SOLD : '+str(v), color='blue', fontsize=12 ,rotation=50, horizontalalignment='center')
        else:
            plt.text(i, v+4000, s=' '+str(v), color='blue', fontsize=12 ,rotation=90, horizontalalignment='center')
    # Showin Plot    
    st.pyplot()
    if st.checkbox("Show Data Top Product"):
            st.subheader("Data")
            st.write(product_name_sold)