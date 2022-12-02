import side
import app
import streamlit as st


Pages={
    "Predict": app,
    "EDA": side
}

selected=st.sidebar.selectbox("Pages", list(Pages.keys()))

page=Pages[selected]

page.apps()