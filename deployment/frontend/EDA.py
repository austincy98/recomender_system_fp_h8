from turtle import width
import pandas as pd
import seaborn as sns
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

st.title("Data Visualization")
st.set_option('deprecation.showPyplotGlobalUse', False)

cp_df = pd.read_csv('C:\\Users\\Bloodink\\Documents\\hacktiv8\\graded_challenge\\p2---final-project-group-001\\2021June-July_product_data.csv')

#3.2 categorical feature
st.header('Categorical Feature')
cp_df['product_category'].value_counts().plot(kind='bar')
st.pyplot()
if st.checkbox("Show Data"):
        st.subheader("Data")
        st.write(cp_df['product_category'].value_counts())
#3.3
st.header("Product Discount and lowest guarantee and rating")

cp_df.groupby(by=['product_category','feature_lowest_price_guarantee']).product_total_rating.agg(["mean"]).plot(kind='barh')
st.pyplot()
if st.button("Show Data"):
        st.subheader("Data")
        st.write(cp_df.groupby(by=['product_category','feature_lowest_price_guarantee']).product_total_rating.agg(["mean"]))
#3.4
st.header("Top Category by like count")
cp_df.groupby(by=['product_category']).product_like_count.agg(["mean"]).plot(kind='barh')
st.pyplot()
if st.button("Show Data Category"):
        st.subheader("Data")
        st.write(cp_df.groupby(by=['product_category']).product_like_count.agg(["mean"]))

#3.5
st.header("Top Category by View")
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
if st.button("Show Data Top Category"):
        st.subheader("Data")
        st.write(top_views)

st.header("Top Category by Total Product Sold")
# Grouping Top viewstop_views
top_sold = cp_df.groupby(by=['product_category']).sum().round(2)
# Sorting
top_sold = top_sold.sort_values('units_sold', ascending=False).head(20)

#plot the top Products with most sales

# Define size
plt.figure(figsize=[20,6])
# Define Bar
plt.bar(top_sold.index, top_sold.units_sold, color='#EF0107', edgecolor='#B31B1B')
# Define font rotation
plt.xticks(rotation=20)
# Define Title and label
plt.title("TOP PRODUCTS SOLD", fontsize=16)
plt.xlabel('PRODUCT', fontsize=14)
plt.ylabel('UNIT SOLD', fontsize=14)
# Define Text
for i, v in top_sold.units_sold.items():
    if v>60000:
        plt.text(i, v-15000, s='SOLD : '+str(v), color='blue', fontsize=12 ,rotation=30, horizontalalignment='center')
    else:
        plt.text(i, v+4000, s='$'+str(v), color='blue', fontsize=12 ,rotation=90, horizontalalignment='center')
# Showin Plot    
st.pyplot()
if st.button("Show Data Top Category "):
        st.subheader("Data")
        st.write(top_sold)
#3.6
st.header("Top Product by View")

# Grouping Top viewstop_views
top_product_views = cp_df.groupby(by=['product_name']).sum().round(2)
# Sorting
top_product_views = top_product_views.sort_values('product_total_rating', ascending=False).head(20)


#plot the top Products with most sales

# Define size
plt.figure(figsize=[20,6])
# Define Bar
plt.bar(top_product_views.index, top_product_views.product_views, color='#EF0107', edgecolor='#B31B1B')
# Define font rotation
plt.xticks(rotation=90)
# Define Title and label
plt.title("TOP PRODUCTS VIEW", fontsize=16)
plt.xlabel('PRODUCT', fontsize=14)
plt.ylabel('TOTAL VIEWS', fontsize=14)
# Define Text
for i, v in top_product_views.product_views.items():
    if v>60000:
        plt.text(i, v-15000, s='VIEWS : '+str(v), color='blue', fontsize=12 ,rotation=30, horizontalalignment='center')
    else:
        plt.text(i, v+4000, s=' '+str(v), color='blue', fontsize=12 ,rotation=90, horizontalalignment='center')
# Showin Plot    
st.pyplot()
if st.button("Show Data Top Product "):
        st.subheader("Data")
        st.write(top_product_views)

st.header("Top Product by Total Product Sold")

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