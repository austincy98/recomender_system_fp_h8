import streamlit as st
import requests
import pandas as pd

def apps():
        st.title("Fashion Finder")

        cmtid = st.number_input("Costumer Id", min_value=0)
        #product_itemid =st.number_input("Product Id", min_value=0)
        #rating_star=st.number_input("Rating", min_value=0, max_value=5)

        # inference
        data = {'cmtid':cmtid}
                

        URL = "https://backend-fp001.herokuapp.com/predict"

        # komunikasi
        if st.button('Predict'):
                r = requests.post(URL, json=data)
                res = r.json()
                #if res['code'] == 200:
                        #dic=res['result']
                df = pd.DataFrame(res['rekomendasi'])
                df2 =pd.DataFrame(res['product yang disukai'])
                        #col=['product','product rating']
                st.write('product yang disukai')
                st.dataframe(df2)
                
                st.write('rekomendasi')
                st.dataframe(df)
                
                #df=pd.DataFrame.from_dict(res)
                #df.columns=['Date', 'DateValue']
                #st.write(pd.DataFrame({

        # }))

