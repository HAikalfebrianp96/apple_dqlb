import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import keras
from keras import models
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
from statsmodels.tsa.stattools import adfuller
from pylab import rcParams
import plotly.graph_objs as go
title = "Stock Market Prediction"
def run():
    df=pd.read_csv('AAPL.csv')
    avg_30 = df['Close'].rolling(window=30, min_periods=1).mean()
    avg_50 = df['Close'].rolling(window=50, min_periods=1).mean()
    

    trace1 = go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        close=df['Close'],
        high=df['High'],
        low=df['Low'],
        name='AAPL'
    )

    # Create the data list
    data = [trace1]

    # Configure graph layout
    layout = go.Layout(
        title='Apple (AAPL) Moving Averages',
        font=dict(size=15)
    )
    st.markdown(
    """
    <div style="font-size: 18px; line-height: 1.6;">

    <p>Grafik menunjukkan pergerakan harga saham AAPL dan Moving Average (MA) 50 hari, 100 hari, dan 150 hari selama periode 2018 - 2022.</p>

    <h3 style="color: #000000;">Analisis:</h3>

    <ul>
        <li><strong>Tren:</strong> Saham AAPL menunjukkan tren naik secara keseluruhan selama periode ini.</li>
        <li><strong>Moving Average:</strong>
            <ul>
                <li style="color: #2ca02c;"><strong>MA 50 hari (hijau):</strong> Berada di atas MA 100 hari (merah) dan MA 150 hari (hijau), menunjukkan tren naik jangka pendek.</li>
                <li style="color: #d62728;"><strong>MA 100 hari (merah):</strong> Berada di atas MA 150 hari (hijau), menunjukkan tren naik jangka menengah.</li>
            </ul>
        </li>
        <li><strong>Support & Resistance:</strong>
            <ul>
                <li style="color: #2ca02c;"><strong>MA 50 hari (hijau):</strong> Dapat bertindak sebagai support (level support) saat harga turun.</li>
                <li style="color: #d62728;"><strong>MA 100 hari (merah) dan MA 150 hari (hijau):</strong> Dapat bertindak sebagai resistance (level resistance) saat harga naik.</li>
            </ul>
        </li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True
    )

    
   
    # Create the figure
    fig = go.Figure(data=data, layout=layout)
  

    # Display the candlestick chart
    st.plotly_chart(fig)
    trace2 = go.Scatter(
        x=df['Date'],
        y=avg_30,
        mode='lines',
        line=dict(color='blue', width=1),
        name='Moving Average of 30 periods'
    )

    trace3 = go.Scatter(
        x=df['Date'],
        y=avg_50,
        mode='lines',
        line=dict(color='red', width=1),
        name='Moving Average of 50 periods'
    )

    # Define the data
    data = [trace1, trace2, trace3]

    # Define graph layout
    layout = go.Layout(
        title='Apple (AAPL) Moving Averages',
        font=dict(size=15)
    )

    # Create the figure
    fig = go.Figure(data=data, layout=layout)
    
    st.markdown(
    """
    <div style="font-size: 18px; line-height: 1.6;">

    <p>Tren: Saham AAPL menunjukkan tren naik secara keseluruhan selama periode ini.</p>
    <p>Moving Average:</p>
    <ul>
        <li><strong style="color: #1f77b4;">Garis biru (MA 30) :</strong> berada di atas <strong style="color: #FFA500;">Garis oranye (MA 50) :</strong> , menunjukkan tren naik jangka pendek.</li>
        <li>Kedua garis MA (30 dan 50) berada di atas garis <strong style="color: #FF0000;">merah :</strong> dan <strong style="color: #00FF00;">hijau :</strong> nila dari saham AAPL (harga penutupan), menunjukkan tren naik jangka menengah dan panjang.</li>
    </ul>
    <p>Volume: Volume perdagangan saham AAPL meningkat pada tahun 2020 dan 2021, menunjukkan minat investor yang tinggi.</p>
    
    <div style="border: 2px solid #ccc; padding: 10px; margin-top: 20px;">
        <p><strong>Note:</strong> Analisis teknikal lebih lanjut menunjukkan bahwa terdapat level support yang kuat di sekitar MA 50, dengan potensi untuk memantulkan harga saham kembali ke arah tren naik utama.</p>
    </div>

    </div>
    """,
    unsafe_allow_html=True
    )


    # Display the candlestick chart with moving averages
    st.plotly_chart(fig)



    #Splitting the data into training and testing
    data_training = df['Close'].iloc[:int(len(df)*0.70)]
    data_testing = df['Close'].iloc[int(len(df)*0.70):]

    # Plotting
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.title('AAPL Stocks Train & Test Data')
    plt.xlabel('Scale (Year)')
    plt.ylabel('Closing Prices')
    plt.plot(data_training.index, data_training, 'blue', label='Train data')
    plt.plot(data_testing.index, data_testing, 'green', label='Test data')
    plt.legend()

    # Display the plot
    st.markdown(
    """
    <div style="font-size: 18px; line-height: 1.6;">

    <p>data :</p>
    <ul>
        <li><strong style="color: #1f77b4;">Data Latih (Train Data):</strong> 80% dari data (dari tahun 2000 hingga 2020)</li>
        <li><strong style="color: #2ca02c;">Data Uji (Test Data):</strong> 20% dari data (dari tahun 2021 hingga 2023)</li>
    </ul>

    <h3>Analisis:</h3>

    <p><strong style="color: #1f77b4;">Data Latih:</strong></p>
    <ul>
        <li><strong>Pola:</strong> Data menunjukkan tren naik yang jelas selama periode ini.</li>
        <li><strong>Volatilitas:</strong> Volatilitas data relatif rendah pada periode ini, dengan beberapa fluktuasi di sekitar tren naik.</li>
    </ul>

    <p><strong style="color: #2ca02c;">Data Uji:</strong></p>
    <ul>
        <li><strong>Pola:</strong> Data menunjukkan tren naik yang berlanjut, meskipun dengan volatilitas yang lebih tinggi dibandingkan data latih.</li>
        <li><strong>Keakuratan Prediksi:</strong> Model yang dilatih pada data latih dapat memprediksi harga penutupan saham AAPL dengan cukup akurat pada data uji.</li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True
    )

   
    st.pyplot(plt)


    data = df.filter(['Close'])
    dataset = data.values

    def test_stationarity(timeseries):
        adft = adfuller(timeseries, autolag='AIC')
        result_df = pd.DataFrame(index=['Test Statistic', 'p-value', '#Lags Used', '#Observations Used'], columns=['Results'])
        result_df['Results']['Test Statistic'] = adft[0]
        result_df['Results']['p-value'] = adft[1] 
        result_df['Results']['#Lags Used'] = adft[2] 
        result_df['Results']['#Observations Used'] = adft[3]
        for key,val in adft[4].items():
            result_df.loc['Critical Value {}'.format(key)] = val      
        st.table(result_df)
    test_stationarity(data)
    st.markdown(
    """
    <div style="font-size: 18px; line-height: 1.6;">

    <p>Statistik uji: <strong>0,4295</strong> nilai p: <strong>0,9826</strong> Nilai kritis:</p>

    <ul>
        <li>1%: -3.4356</li>
        <li>5%: -2.8639</li>
        <li>10%: -2.5680</li>
    </ul>

    <h3>Penafsiran:</h3>

    <p>Statistik uji (<strong>0,4295</strong>) jauh lebih besar dari ketiga nilai kritis (<strong>-3,4356</strong>, <strong>-2,8639</strong>, <strong>-2,5680</strong>). Artinya, nilai p (<strong>0,9826</strong>) juga jauh lebih besar dibandingkan tingkat signifikansinya (biasanya ditetapkan pada 0,05 atau 0,10). Dengan kata lain, terdapat bukti yang sangat kuat untuk menolak hipotesis nol.</p>

    </div>
    """,
    unsafe_allow_html=True
    )

    st.image('77.jpg', caption='Apple', width=30, use_column_width=True)
    st.markdown(
    """
    <div style="font-size: 18px; line-height: 1.6;">

    <p>Grafik menunjukkan pergerakan harga saham AAPL yang mengalami kenaikan signifikan, mencapai angka <strong style="color: #00FF00;">180 dolar</strong>. Prediksi harga untuk tahun selanjutnya menunjukkan tren kenaikan yang lebih curam, dengan nilai yang tidak jauh berbeda dari hasil validasi.</p>

    </div>
    """,
    unsafe_allow_html=True
    )
