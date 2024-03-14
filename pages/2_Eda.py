import streamlit as st

st.title('Klasifikasi Harga Jual Rumah Wilayah Malang')
st.header("Model")

st.subheader("1. Data Collection")
st.write("Dataset penjualan rumah diambil dari website www.lamudi.co.id pada tanggal 08 Februari 2024, menggunakan apk octoparse dengan filter:")
st.write("- Tipe penawaran: dijual")
st.write("- Property: apapun")
st.write("- Lokasi: Malang")
st.write("- Harga: apapun")
st.write("- Kamar tidur: apapun")
st.write("Didapatkan dataset terdiri dari 800 instance dan 6 atribut")

st.subheader("2. Data Cleansing")
st.write("-	Data duplikasi")
st.code("duplicate_rows = df.duplicated()")
st.write("-	Merubah data non integer menjadi integer") 
st.code("luas_lahan_m2 = int(luas_lahan)")
st.write("-	Memilih atribut-atribut yang akan digunakan dalam pemodelan")
st.code("df_new = df.drop(df.columns[[0]], axis=1)")
st.write("-	Mengecek nilai null")
st.code("df.isnull().sum()")
st.write("- Mengecek outlier")
st.code("outliers = detect_outliers_iqr(data)")

st.subheader("3. Model")
st.write("Model menggunakan algoritma regresi linear. Regresi linear sering dipilih untuk memprediksi suatu harga karena kemampuannya yang mudah diinterpretasikan, kemampuan untuk menangkap hubungan linier antara variabel prediktor dan harga, serta ketersediaan data yang mencukupi. Model ini menawarkan prediksi yang sederhana namun cukup akurat, cocok untuk situasi di mana interpretasi yang mudah dipahami lebih diutamakan daripada kompleksitas model. Kemampuan regresi linear untuk memberikan rekomendasi harga yang berguna bagi pembeli dan penjual, serta kecepatan komputasinya yang tinggi, membuatnya menjadi pilihan yang populer dalam analisis harga rumah.")

st.subheader("4. Evaluasi")
st.write("Evaluasi yang digunakan adalah akurasi yang menggambarkan ketepatan model menebak harga target")
st.write("Akurasi : 78%")