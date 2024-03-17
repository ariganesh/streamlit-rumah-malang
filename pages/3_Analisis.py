import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt


st.title('Klasifikasi Harga Jual Rumah Wilayah Malang')
st.header("Analisis")

file_path = 'dataset2.xlsx'
df = pd.read_excel(file_path)


col1, col2= st.columns(2)

with col1:
    import pandas as pd
    import altair as alt
    import streamlit as st

# Menghitung jumlah kemunculan alamat
    wilayah = df['address'].value_counts().reset_index()
    wilayah.columns = ['Wilayah', 'Jumlah']

# Plot bar chart menggunakan Altair
    bar_chart = alt.Chart(wilayah).mark_bar().encode(
        x=alt.X('Wilayah', title='Wilayah', sort='-y'),  # Mengurutkan berdasarkan jumlah secara descending
        y='Jumlah'
    ).properties(
        title='Jumlah Kemunculan Penjualan'
    )

# Menampilkan bar chart menggunakan Streamlit
    st.altair_chart(bar_chart, use_container_width=True)


with col2:
# Scatter plot menggunakan Altair
    scatter_plot = alt.Chart(df).mark_circle().encode(
        x=alt.X('luas_bangunan_m2', title='Luas Bangunan'),
        y=alt.Y('luas_lahan_m2', title='Luas Lahan'),
    ).properties(
        title='Scatter Plot Luas Bangunan vs. Luas Lahan'
    )
# Menampilkan scatter plot menggunakan Streamlit
    st.altair_chart(scatter_plot, use_container_width=True)

# Mendapatkan harga tertinggi dan terendah setiap wilayah
harga_tertinggi = df.groupby('address')['price'].max().reset_index(name='price_max')
harga_terendah = df.groupby('address')['price'].min().reset_index(name='price_min')
harga_avg = df.groupby('address')['price'].mean().reset_index(name='price_avg')

# Menggabungkan data harga tertinggi dan terendah
df_merged = harga_tertinggi.merge(harga_terendah, on='address')
df_merged = df_merged.merge(harga_avg, on='address')
# Membuat visualisasi menggunakan Altair
bars_max = alt.Chart(df_merged).mark_bar().encode(
    x=alt.X('address', title='Wilayah'),
    y=alt.Y('price_max'),
    tooltip=['price_max']
)
bars_min = alt.Chart(df_merged).mark_bar(color='blue').encode(
    x=alt.X('address', title='Wilayah'),
    y=alt.Y('price_min', title='Harga'),
    tooltip=['price_min']
)
line_chart_min = alt.Chart(df_merged).mark_line(color='red').encode(
    x=alt.X('address', title='Wilayah'),
    y=alt.Y('price_avg', title='Harga'),
    tooltip=['price_avg']
)
chart = (bars_max + bars_min + line_chart_min).properties(
    width=500,
    title='Harga Tertinggi dan Terendah Setiap Wilayah'
).interactive()
# Menampilkan visualisasi menggunakan Streamlit
st.altair_chart(chart, use_container_width=True)


st.write('- Dengan sebaran data, wilayah pusat kota malang memiliki mendominasi 5 wilayah dengan penjualan teratas. yang berarti kota/padat penduduk banyaknya transaksi jual beli rumah.')

st.write('- Teruntuk luas-luas rumah yang akan jual belikan memiliki hubungan seimbang antara luas rumah dengan luas lahan yang dijual.')

st.write('- Harga setiap rumah pada wilayah yang sama, cenderung memiliki yang sama. tetapi luas lahan dan bangunan mempengaruhi harga yang akan dijual.')

# Membuat scatter plot dengan Altair
scatter_plot = alt.Chart(df).mark_circle().encode(
    x=alt.X('luas_bangunan_m2', title='Luas Bangunan'),
    y=alt.Y('luas_lahan_m2', title='Luas Lahan'),
    color='kode_address',
    size=alt.Size('price', scale=alt.Scale(range=[50, 500])),
    tooltip=['address', 'luas_lahan', 'luas_bangunan', 'price']
).properties(
title='Harga rumah berdasarkan luas bangunan dan luas lahan'
).interactive()
# Menampilkan scatter plot menggunakan Streamlit
st.altair_chart(scatter_plot, use_container_width=True)

st.write('- Akan tetapi, ketika membandingkan harga setiap wilayah dengan luas yang sama. Ternyata terjadi perbedaan yang cukup signifikan antar wilayah tersebut, khususnya pada wilayah kota.')















