import categorical_feature
import product_discount
import top_category
import top_product
#import market_consider
import streamlit as st

def apps():
    Pages={
        "Categorical Feature": categorical_feature,
        "Product Discount": product_discount,
        "Top Category":top_category,
        "Top Product":top_product,
        #"Marketing Reconsideration": market_consider
    }

    selected=st.sidebar.selectbox("Pages", list(Pages.keys()))

    page=Pages[selected]

    page.apps()