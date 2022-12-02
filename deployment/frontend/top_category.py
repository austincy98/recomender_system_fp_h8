import top_category_like
import top_category_view
import top_category_sold
import streamlit as st

def apps():
    Pages={
        "by Like":top_category_like,
        "by View":top_category_view,
        "by Product Sold":top_category_sold
    }

    selected=st.sidebar.selectbox("Pages", list(Pages.keys()))

    page=Pages[selected]

    page.apps()