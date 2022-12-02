import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def apps():
    st.title("Top Category by View")
    st.set_option('deprecation.showPyplotGlobalUse', False)

    cp_df = pd.read_csv('2021June-July_product_data.csv')

    top_views = cp_df.groupby(by=['product_category']).sum().round(2)
    # Sorting
    top_views = top_views.sort_values('product_total_rating', ascending=False).head(20)
    #plot the top Products with most sales

    # Define size
    plt.figure(figsize=[20,6])
    # Define Bar
    plt.bar(top_views.index, top_views.product_views, color='#EF0107', edgecolor='#B31B1B')
    # Define font rotation
    plt.xticks(rotation=30)
    # Define Title and label
    plt.title("TOP PRODUCTS VIEW", fontsize=16)
    plt.xlabel('PRODUCT', fontsize=14)
    plt.ylabel('TOTAL VIEWS', fontsize=14)
    # Define Text
    for i, v in top_views.product_views.items():
        if v>60000:
            plt.text(i, v-15000, s='VIEWS : '+str(v), color='blue', fontsize=12 ,rotation=30, horizontalalignment='center')
        else:
            plt.text(i, v+4000, s='$'+str(v), color='blue', fontsize=12 ,rotation=90, horizontalalignment='center')
    # Showin Plot    
    st.pyplot()
    if st.checkbox("Show Data Top Category"):
            st.subheader("Data")
            st.write(top_views)