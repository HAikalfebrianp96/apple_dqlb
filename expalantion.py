import streamlit as st
title = "Conclusion"

def run():
    st.markdown(
    """
    <div style="text-align: justify;">

    <h2 style="color: #ff5733;">Analisis Saham Apple (AAPL)</h2>

    <p>Berdasarkan analisis grafik Daily Chart EOD fmp 2018-2022 menggunakan model LSTM, dapat ditarik kesimpulan sebagai berikut:</p>

    <p><strong>1. <span style="color: #4CAF50;">Kenaikan Signifikan:</span></strong></p>

    <p>Harga saham AAPL mengalami kenaikan signifikan, mencapai angka $180.
    Tren kenaikan ini terjadi secara konsisten dalam periode yang dianalisis (2018-2022).</p>

    <p><strong>2. <span style="color: #4CAF50;">Prediksi Kenaikan Lebih Curam:</span></strong></p>

    <p>Prediksi harga untuk tahun selanjutnya menunjukkan tren kenaikan yang lebih curam.
    Nilai prediksi tidak jauh berbeda dari hasil validasi, menunjukkan tingkat akurasi yang tinggi.</p>

    <p><strong>3. <span style="color: #4CAF50;">Visualisasi Saham:</span></strong></p>

    <p>Saham AAPL menunjukkan kinerja yang sangat baik dengan tren kenaikan yang konsisten.
    Prediksi menunjukkan bahwa tren ini akan berlanjut di tahun selanjutnya dengan kenaikan yang lebih curam.
    Hal ini menjadikan saham AAPL sebagai pilihan investasi yang menarik dengan potensi keuntungan yang tinggi.</p>

    <p>Kesimpulan ini didasarkan pada analisis grafik dan prediksi menggunakan model LSTM untuk saham AAPL dalam periode 2018-2022.</p>

    </div>
    """, unsafe_allow_html=True
    )

