[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8075471&assignment_repo_type=AssignmentRepo)

Final project oleh `Group 1`, Batch: `11`

Anggota Group 1:
- Evita Ardhiya Ramadhani
- Jhon Kristian Vieri
- Austin Christian Yonatan
- Timothy H

Judul: `FashionFinder`

Dataset source: Kaggle dataset
- Dataset Produk: 2021June-July_product_data.csv
- Dataset Customer dan rating: /2021June-July_review_data.csv

**Latar Belakang:**
- Perkembangan dunia fashion yang sangat pesat mengakibatkan banyaknya jenis dan model yang tersedia. Selain itu, dari setiap jenis produk tersebut memiliki keberagaman kualitas.
- Hal tersebut mengakibatkan terlalu banyak informasi yang harus diperhatikan dalam memilih suatu produk yang sesuai kebutuhan dengan kualitas yang bagus. 

**Output:**
- Rekomendasi produk yang diberikan berdasarkan rating review yang telah diberikan customer sebelumnya, karena dari informasi tersebut secara implisit telah menggambarkan produk yang disukai atau kurang disukai.
- Produk yang direkomendasikan berupa produk yang memiliki kemiripan  dengan produk yang diberikan rating tinggi oleh customer tersebut.

**Rekomendasi sistem:**
- Rekomendasi sistem yang dibuat merupakan collaborative filtering dimana membuat model yang digunakan untuk melakukan prediksi rating produk yang belum dibeli oleh customer, kemudian dari prediksi tersebut digunakan untuk memberikan rekomendasi 5 barang dengan rating tertinggi ke customer.
- Collabarative filtering mencari kerimiripan antar produk dari hasil cosinus similarity. Jika customer merupakan pengguna baru dan belum memberikan rating, maka rekomendasi yang diberikan berdasarkan kemiripan customer satu dengan customer lainnya.
- Menggunakan User - Based Collaborative Filtering, karena teknik rekomendasi produk yang sering digunakan dalam membuat algoritma machine learning, algoritma ini dapat memberikan rekomendasi yang lebih baik seiring dengan bertambahnya jumlah pembelian dari penggunanya dan metode sistem rekomendasi ini sudah digunakan oleh perusahaan-perusahaan besar seperti Amazon, Netflix, eBay dan perusahaan yang menyimpan data penggunanya.

Aplikasi FashionFinder: https://fp-001.herokuapp.com/"# recomender_system_fp_h8" 
