import top_product_view
import top_product_sold
import streamlit as st

def apps():
    Pages={
        "by View":top_product_view,
        "by Product Sold":top_product_sold
    }

    selected=st.sidebar.selectbox("Pages", list(Pages.keys()))

    page=Pages[selected]

    page.apps()