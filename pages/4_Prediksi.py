import pickle
import streamlit as st


model = pickle.load(open('predik_harga_rumah.sav', 'rb'))

st.title('Klasifikasi Harga Jual Rumah Wilayah Malang')

address_options = [
        'Arjosari = 1', 'Arjowinangun = 2', 'Balearjosari = 3', 'Bandulan = 4', 'Bareng = 5', 'Blimbing = 6', 'Bumiayu = 7', 
        'Bunulrejo = 8', 'Buring = 9', 'Cemorokandang = 10', 'Dau = 11', 'Dinoyo = 12', 'Gadang = 13', 'Gondanglegi = 14', 
        'Jatimulyo = 15', 'Karang Ploso = 16', 'Karangbesuki = 17', 'Kedungkandang = 18', 'Kepanjen = 19', 'Ketindan = 20', 
        'Klojen = 21', 'Kotalama = 22', 'Lawang = 23', 'Lowokwaru = 24', 'Madyopuro = 25', 'Malang = 26', 'Mergosono = 27', 
        'Merjosari = 28', 'Mulyorejo = 29', 'Oro-oro Dowo = 30', 'Pagelaran = 31', 'Pakis = 32', 'Pakisaji = 33', 'Pandanwangi = 34', 
        'Pisangcandi = 35', 'Purwantoro = 36', 'Sawojajar = 37', 'Singosari = 38', 'Sukun = 39', 'Tajinan = 40', 'Tasik Madu = 41', 
        'Tlogomas = 42', 'Tlogowaru = 43', 'Tulusrejo = 44', 'Tunggulwulung = 45', 'Tunjungsekar = 46', 'Turen = 47', 'Wagir = 48'
    ]
address = st.selectbox("Pilih wilayah & kode wilayah untuk alamat rumah", address_options)
    
col1, col2 = st.columns(2)
with col1:
        kode_address = int(address.split('=')[-1].strip())
        luas_bangunan_m2 = st.number_input('Input luas bangunan rumah (m2)')
        
with col2:
        luas_lahan_m2 = st.number_input('Input luas lahan rumah (m2)')
kamar = st.slider('Pilih jumlah kamar dari rumah', min_value=1, max_value=25, step=1)

predict = ''

if st.button('Prediksi harga'):
    predict = model.predict([[kamar, luas_bangunan_m2, luas_lahan_m2, kode_address]])
    predicted_price = predict[0]  # Misalkan predict mengembalikan list dengan satu elemen
    formatted_price = f'Rp {predicted_price:,.0f}'  # Ubah nilai angka menjadi format uang
    st.write(f'Kemungkinan harga jual rumah: {formatted_price}')
    st.write('Harga yang muncul hanya sebagai **_refrensi_** harga jual/beli. Harga jual/beli bisa lebih atau pun kurang tergantung nilai lebih dari rumah akan dijual, seperti jumlah lantai, desain rumah, garasi, dan lain-lain.')