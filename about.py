import streamlit as st
import pandas as pd
title = "About Data "
df = pd.read_csv('AAPL.csv')
# Describe the data

def run():
        st.subheader('Data from 2018-2022')
        st.write(df.describe())
        st.markdown(
            """
            <style>
                .container {
                    max-width: 800px;
                    margin: auto;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                    background-color: #f9f9f9;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                }
                .title {
                    text-align: center;
                    font-size: 24px;
                    color: #333;
                    margin-bottom: 20px;
                }
                .description {
                    font-size: 18px;
                    color: #666;
                    line-height: 1.5;
                }
                .source {
                    font-style: italic;
                    color: #888;
                    margin-top: 20px;
                }
                .highlight {
                    background-color: #ffff99;
                    padding: 5px 10px;
                    border-radius: 5px;
                }
            </style>
            """
            , unsafe_allow_html=True
        )

        st.markdown("<div class='container'>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class='description'>
                Data historis harga EOD (End-of-Day) harian untuk saham Apple (AAPL) dari Financial Modeling Prep (FMP), meliputi periode 2017 hingga 2022.
            </div>
            """
            , unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class='highlight'>
                Sumber:
            </div>
            <div class='description'>
                Financial Modeling Prep (FMP): Ini adalah platform penyedia data keuangan yang menawarkan API untuk mengakses data historis dan real-time untuk berbagai instrumen keuangan, termasuk saham, obligasi, dan mata uang.
            </div>
            """
            , unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class='highlight'>
                Jenis Data:
            </div>
            <div class='description'>
                <ul>
                    <li><strong>EOD (End-of-Day):</strong> Data EOD mengacu pada informasi harga dan aktivitas perdagangan yang dikumpulkan pada akhir setiap hari bursa.</li>
                    <li><strong>Daily Chart:</strong> Ini menunjukkan bagaimana harga saham berfluktuasi sepanjang hari selama periode tertentu.</li>
                    <li><strong>Data Historis:</strong> Data ini mencakup periode tahun 2017 hingga 2022, memungkinkan Anda menganalisis kinerja saham AAPL selama 6 tahun terakhir.</li>
                </ul>
            </div>
            """
            , unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class='highlight'>
                Jenis Data:
            </div>
            <div class='description'>
                <ul>
                    <li><strong>Open:</strong> Harga pembukaan saham pada setiap hari.</li>
                    <li><strong>High:</strong> Harga tertinggi yang dicapai saham pada setiap hari.</li>
                    <li><strong>Low:</strong> Harga terendah yang dicapai saham pada setiap hari.</li>
                    <li><strong>Close:</strong> Harga penutupan saham pada setiap hari.</li>
                    <li><strong>Volume:</strong> Jumlah saham yang diperdagangkan pada setiap hari.</li>
                </ul>
            </div>
            """
            , unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class='source'>
                Sumber data: <a href="https://financialmodelingprep.com/api/v3/historical-price-full/AAPL" target="_blank">Daily Chart EOD FMP</a>
            </div>
            """
            , unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)
