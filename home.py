import streamlit as st
title = "Home"  # Position at the top


def run():
    st.image('18.jpg', caption='Apple', width=30, use_column_width=True)
    # Mengurangi margin atas agar tulisan lebih dekat dengan gambar
    st.write("""
    <div style="text-align: center; margin-top: -20px;">
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["tentang saham ", "Identifikasi Masalah"])
        # Center align the information and marketing content
    with tab1:
        # Content for the first tab
        st.subheader("Tentang Saham")
        st.subheader("Menjelajahi Dunia Apple: Kisah Saham AAPL (2017 - 2022) ")
        
        st.markdown(
            """
            Pernahkah Anda membayangkan memiliki sebuah perusahaan yang menghasilkan produk-produk ikonik dan inovatif seperti iPhone, iPad, dan Mac?

            Perjalanan Apple (AAPL) di pasar saham bagaikan roller coaster yang penuh petualangan. Mari kita jelajahi kisahnya dari tahun 2017 hingga 2022, di mana kita akan menemukan momen-momen seru seperti:

            **2017:**

            * Peluncuran iPhone X, smartphone revolusioner dengan Face ID dan layar OLED.
            * Saham AAPL melesat 55%!

            **2018:**

            * Apple menjadi perusahaan AS pertama yang menembus kapitalisasi pasar $1 triliun!
            * Perang dagang AS-China dan kekhawatiran ekonomi global menyebabkan harga saham AAPL turun 21%.

            **2019:**

            * Penjualan iPhone di China menurun dan produk baru Apple kurang inovatif.
            * Harga saham AAPL terjun bebas hingga 63%!

            **2020:**

            * Di tengah pandemi Covid-19, permintaan untuk produk Apple meningkat.
            * Saham AAPL melonjak 156%!

            **2021:**

            * Peluncuran iPhone 12 series yang mendukung jaringan 5G.
            * Harga saham AAPL mencapai rekor tertinggi baru!

            **2022:**

            * Apple menghadapi berbagai hambatan, seperti inflasi, krisis chip global, dan perang di Ukraina.
            * Harga saham AAPL berfluktuasi, namun tetap menunjukkan performa yang stabil.

            **Cerita yang Menginspirasi:**

            Kisah saham AAPL adalah kisah tentang inovasi, adaptasi, dan ketangguhan. Ini adalah kisah inspiratif bagi para investor dan pengusaha yang ingin mencapai kesuksesan di dunia yang penuh dengan perubahan.
            """
            )

        with tab2:
            st.subheader("Identifikasi Masalah untuk Pembeli Saham AAPL (2017-2022)")
            st.markdown(
                    """
                    <style>
                    .reportview-container {
                        background: #f6f6f6;
                        padding: 1rem;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                    )
                
                # Set title style
            st.markdown(
                    """
                    <style>
                    .title {
                        color: #333333;
                        text-align: center;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                
                # Set text style
            st.markdown(
                    """
                    <style>
                    .text {
                        color: #555555;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )
                
            st.markdown("""
                <div class='text'>
                <p>Berdasarkan data Daily Chart EOD AAPL dari fmp (2017-2022) dan menggunakan model LSTM, berikut adalah 3 poin identifikasi masalah untuk pembeli saham AAPL:</p>
                <ol>
                    <li><strong>Tren Penurunan Jangka Panjang:</strong> Model LSTM menunjukkan tren penurunan harga saham AAPL dalam jangka panjang (2017-2022). Hal ini dapat menjadi sinyal risiko bagi pembeli saham, karena harga saham AAPL diprediksi akan terus turun dalam jangka panjang. Pembeli saham perlu mempertimbangkan faktor ini sebelum membeli saham AAPL, dan melakukan analisis lebih lanjut untuk menentukan apakah tren ini akan berlanjut atau tidak.</li>
                </ol>
                <p><strong>Tujuan analisis ini adalah:</strong></p>
                <ul>
                    <li>Mendeteksi adanya tren penurunan jangka panjang pada harga saham AAPL yang dapat menjadi sinyal risiko bagi pembeli saham.</li>
                    <li>Memberikan informasi kepada pembeli saham AAPL agar mempertimbangkan kemungkinan tren penurunan harga jangka panjang sebelum membeli saham.</li>
                    <li>Membantu pembeli saham AAPL melakukan analisis lebih lanjut dengan mempelajari faktor-faktor fundamental perusahaan dan kondisi pasar untuk menentukan apakah tren penurunan akan berlanjut atau terjadi pembalikan tren.</li>
                </ul>
                <p>Secara umum, analisis ini bertujuan untuk membantu pembeli saham AAPL mengambil keputusan investasi yang lebih baik berdasarkan informasi prediksi harga di masa depan menggunakan data historis dan pembelajaran mesin.</p>
                </div>
                """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

