import streamlit as st
from PIL import Image
st.set_page_config(
    page_title = "Harga Rumah",
    layout = "wide"
)

st.title('Klasifikasi Harga Jual Rumah Wilayah Malang')

kol1, kol2, kol3 = st.columns([4,5,4])
with kol2:
    image = Image.open("rumah2.png")
    st.image(
        image,
        caption="Rumahku",
        width=400,  # Atur lebar gambar menjadi 300 piksel
        #use_column_width=False  # Nonaktifkan penggunaan lebar kolom Streamlit
    )
st.write('Rumah merupakan salah satu kebutuhan primer bagi manusia. Dalam abad 20 ini, rumah sudah berkembang dengan berbagai manfaat bagi manusia seperti :')
st.write('-	Perlindungan dan Keamanan: Rumah menyediakan tempat perlindungan dan keamanan bagi manusia dari cuaca eksternal dan bahaya alam.')
st.write('-	Tempat Tinggal dan Kebutuhan Dasar: Rumah sebagai tempat untuk manusia untuk tinggal dan bermukim')
st.write('-	Kesejahteraan Mental dan Emosional: Lingkungan rumah yang nyaman, hangat, dan berkesan dapat menciptakan rasa kenyamanan, kedamaian, dan kebahagiaan bagi penghuninya.')
st.write('-	Kehidupan Sosial dan Keluarga: Rumah merupakan tempat pertemuan dan interaksi antara anggota keluarga serta tempat untuk membentuk ikatan sosial dan emosional.')
st.write('-	Pembangunan dan Perkembangan Peradaban: Karena awal peradaban berasal dari tempat yang disebut sebagai rumah.')
st.write('- Investasi dan Kekayaan: Sebagai salah satu bentuk investasi, simbol keberhasilan, dan stabilitas finansial, serta sebagai aset yang dapat meningkatkan kekayaan dan memperkuat posisi ekonomi mereka.')
