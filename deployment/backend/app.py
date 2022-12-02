#from distutils.log import debug
#from re import X
from flask import Flask, jsonify, request
import numpy as np
import pandas as pd
import tensorflow as tf

app = Flask(__name__)


columns=['cmtid']
       

model=tf.keras.models.load_model("model_fp.hdf5")

@app.route("/")
def homepage():
    return "<h1>Backend </h1>"

@app.route("/predict", methods=["GET", "POST"])
def model_inference():
    if request.method == 'POST':
        data = request.json
        print(data)
        
        new_data = [data['cmtid']]

        x1=pd.DataFrame([new_data],columns=columns)

        cr_df=pd.read_csv('2021June-July_review_data.csv')
        cp_df = pd.read_csv('2021June-July_product_data.csv')
        cr_df.rename(columns = {'itemid':'product_itemid'}, inplace = True)
        cr_df['cmtid'] = pd.factorize(cr_df['cmtid'])[0]
        cr_df['product_itemid'] = pd.factorize(cr_df['product_itemid'])[0]
        cp_df['product_itemid'] = pd.factorize(cp_df['product_itemid'])[0]
        
        #new_data = pd.DataFrame(new_data,columns=columns)

        #Prediksi rekomendasi untuk user 1 - Produk yang populer random
        num_product= 100

        product_list = cr_df.groupby('product_itemid').count().sort_values('cmtid',ascending=False).index[:num_product]
        x=x1['cmtid']
        user_1 = np.array([x for i in range(len(product_list))])

        result = model.predict([user_1,product_list]).reshape(num_product)

        top_5_ids = (-result).argsort()[:5]
        top_5_product_id = product_list[top_5_ids]
        top_5_product_rating = result[top_5_ids]*(cr_df.rating_star.max() - cr_df.rating_star.min()) + cr_df.rating_star.min()


        
        product=[]
        rating=[]
        for i,id in enumerate(top_5_product_id):
            product.append(cp_df['product_name'].loc[id])
            rating.append(str(top_5_product_rating[i]))

        liked_products_user_1 = cr_df[cr_df['cmtid']==x[0]].sort_values('rating_star',ascending=False)['product_itemid'][:5].values
        user_rating = cr_df[cr_df['cmtid']==x[0]].sort_values('rating_star',ascending=False)['rating_star'][:5].values
        
        product_yangdisukai=[]
        rating_yangdisukai=[]
        for i,id in enumerate(liked_products_user_1):
            product_yangdisukai.append(cp_df['product_name'].loc[id])
            rating_yangdisukai.append(str(user_rating[i]))

        res={'product rekomendasi': product,'rating': rating }
        res2={'product yang disukai user':product_yangdisukai, 'rating dari product yang disukai': rating_yangdisukai}
        res3={'rekomendasi':res, 'product yang disukai': res2}
        print("res :", res3)

        #response = str(res[:5])


                    #str(res1[:5])}
        #'code':200, 'status':'OK','result': 

        return jsonify(res3)
            

    return "Silahkan gunakan method post untuk mengakses model"

#app.run(debug=True)