import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.stattools import adfuller
from pylab import rcParams
import plotly.graph_objs as go
from statsmodels.tsa.seasonal import seasonal_decompose
title = "Stock Market Prediction"
def run():
    df=pd.read_csv('AAPL.csv')
    day_df = pd.read_csv("AAPL.csv")

# Converting 'Date' column to datetime and extracting year and month
    day_df['Date'] = pd.to_datetime(day_df['Date'])
    day_df['Year'] = day_df['Date'].dt.year
    day_df['Month'] = day_df['Date'].dt.month

    # Mapping numeric months to month names
    def create_monthly_rent_df(dt):
        monthly_rent_dt = dt.groupby(by='Month').agg({
            'Close': 'sum'
        })
        ordered_months = [
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ]
        monthly_rent_dt = monthly_rent_dt.reindex(ordered_months, fill_value=0)
        return monthly_rent_dt

    def Open_df(dt):
        daily_open_dt = dt.groupby(by='Date').agg({
            'Open': 'sum'
        }).reset_index()
        return daily_open_dt


    def daily_High_df(dt):
        daily_High_dt = dt.groupby(by='Date').agg({
            'High': 'sum'
        }).reset_index()
        return daily_High_dt

    def create_Low_df(dt):
        low_dt = dt.groupby(by='Date').agg({
            'Low': 'sum'
        }).reset_index()
        return low_dt 

    def create_Close_df(dt):
        close_dt = dt.groupby(by='Date').agg({
            'Close': 'sum'
        }).reset_index()
        return close_dt 


    def create_adj_df(dt):
        adj_dt = dt.groupby(by='Date').agg({
            'Adj Close': 'sum'  # Make sure there is no tab or space after 'Adj Close'
        }).reset_index()
        return adj_dt 


    def create_Volume_df(dt):
        Volume_dt = dt.groupby(by='Date').agg({
            'Volume': 'sum'
        }).reset_index()
        return Volume_dt

    def create_year_rent_df(dt):
        year_rent_dt = dt.groupby(by='Year').agg({
            'Close': 'sum'
        }).reset_index()
        return year_rent_dt

    # Getting the min and max date from the DataFrame
    min_date = day_df['Date'].min().date()
    max_date = day_df['Date'].max().date()

    # Streamlit date input for range selection
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    # Filtering the DataFrame by the selected date range
    main_dt = day_df[(day_df['Date'].dt.date >= start_date) & 
                    (day_df['Date'].dt.date <= end_date)]

    # Calling the processing functions
    year_rent_dt = create_year_rent_df(main_dt)
    adj_dt = create_adj_df(main_dt)
    Volume_dt = create_Volume_df(main_dt)
    close_dt = create_Close_df(main_dt)
    low_dt = create_Low_df(main_dt)
    daily_High_dt = daily_High_df(main_dt)
    daily_open_dt = Open_df(main_dt)
    monthly_rent_dt = create_monthly_rent_df(main_dt)

    def custom_format(number):
        parts = f"{number:,}".split(",")
        if len(parts) > 1:
            return f"{parts[0]}, {','.join(parts[1:])}"
        return f"{number}"

    st.subheader('History Apple Saham')
    col1, col2 = st.columns(2)  # Corrected to two columns, as 3 doesn't match the provided columns

    with col1:
        # Summing the 'Open' values of the filtered DataFrame
        total_open = daily_open_dt['Open'].sum()
        st.metric('Open Saham', value=custom_format(total_open))

    with col2:
        # Summing the 'Close' values of the filtered DataFrame
        total_close = close_dt['Close'].sum()
        st.metric('Close Saham', value=custom_format(total_close))

    st.markdown(
        """
        <div style="font-size: 20px; font-weight: bold; text-align: center;">
        Yearly Close Sum
        </div>
        """,unsafe_allow_html=True)
    
    fig, ax = plt.subplots()
    year_rent_dt.plot(kind='bar', x='Year', y='Close', ax=ax)
    ax.set_title('Yearly Sum of Close Prices')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sum of Close Prices')
    st.pyplot(fig)
    
    

    st.markdown(
        """
        <div style="font-size: 20px; font-weight: bold; text-align: center;">
        Seasonal Decompose
        </div>
        """,unsafe_allow_html=True)
    
    # Filter data based on the selected date range
    filtered_data = main_dt[(main_dt['Date'] >= pd.to_datetime(start_date)) &
                            (main_dt['Date'] <= pd.to_datetime(end_date))].copy()

    # Define the period for the decomposition based on the filtered data
    # For daily data, you can use monthly seasonality if you don't have multiple years of data
    # Approximating month as 22 trading days
    if len(filtered_data) >= 2 * 22:
        period = 22  # Monthly frequency in trading days
    else:
        period = len(filtered_data) // 2  # Fall back to half the data size, not ideal but avoids error

    # Decompose the closing price
    decompose_result = seasonal_decompose(filtered_data['Close'], period=period, model='additive', extrapolate_trend='freq')

    # Plotting the decomposed components
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 8))
    decompose_result.trend.plot(ax=ax1, title='Trend')
    decompose_result.seasonal.plot(ax=ax2, title='Seasonality')
    decompose_result.resid.plot(ax=ax3, title='Residuals')

    # Clear the titles and set a common title for all subplots
    for ax in [ax1, ax2, ax3]:
        ax.set_title('')
    fig.suptitle('Seasonal Decomposition')

    st.pyplot(fig)

    st.markdown(
        """
        <div style="font-size: 20px; font-weight: bold; text-align: center;">
        Grouped Bar Chart
        </div>
        """,unsafe_allow_html=True)
    
    def create_monthly_open_close_df(dt):
    # Assuming 'Month' and 'Year' columns are already present in the DataFrame
        monthly_data = dt.groupby(by=['Year', 'Month']).agg({
            'Open': 'mean',  # Using mean instead of sum for a normalized view
            'Close': 'mean'
        }).reset_index()
        return monthly_data

    # Assuming the 'create_monthly_open_close_df' function has been defined
    monthly_rent_dt = create_monthly_open_close_df(main_dt)

    # Pivot the DataFrame to make 'Month' unique and get separate columns for 'Open' and 'Close'
    monthly_pivot = monthly_rent_dt.pivot(index='Month', columns='Year', values=['Open', 'Close'])

    # Generate the bar positions
    bar_width = 0.35
    index = np.arange(len(monthly_pivot.index))

    # Start plotting
    fig, ax = plt.subplots(figsize=(12, 6))

    # Loop through the years to create stacked bars for each year
    for i, year in enumerate(monthly_pivot['Open'].columns):
        ax.bar(index + bar_width * i, monthly_pivot['Open'][year], bar_width, label=f'Open {year}')
        ax.bar(index + bar_width * i, monthly_pivot['Close'][year], bar_width, bottom=monthly_pivot['Open'][year],
            alpha=0.5, label=f'Close {year}')

    ax.set_xlabel('Month')
    ax.set_ylabel('Average Price')
    ax.set_title('Monthly Average Open and Close Prices Comparison')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(monthly_pivot.index)
    ax.legend()

    # Make the plot tighter and more organized
    fig.tight_layout()

    # Show the plot in Streamlit
    st.pyplot(fig)
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
        font=dict(size=20),
        title_xanchor='center',
        title_x=0.5
    )
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
    st.markdown(
        """
        <div style="font-size: 18px; line-height: 1.6;">

        <p>Grafik menunjukkan pergerakan harga saham AAPL dan Moving Average (MA) 50 hari, 100 hari, dan 150 hari selama periode 2017 - 2022.</p>

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
        <div style="border: 2px solid #ccc; padding: 10px; margin-top: 20px;">
            <p><strong>Note:</strong> Analisis teknikal lebih lanjut menunjukkan bahwa terdapat level support yang kuat di sekitar MA 50, dengan potensi untuk memantulkan harga saham kembali ke arah tren naik utama.</p>
        </div>
        """,unsafe_allow_html=True)
    
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
        title='Apple (AAPL) Moving Averages periods 30- 50',
        font=dict(size=20),
        title_xanchor='center',
        title_x=0.5
    )

    # Create the figure
    fig = go.Figure(data=data, layout=layout)
    # Display the candlestick chart with moving averages
    st.plotly_chart(fig)
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
    
    

    </div>
    """,unsafe_allow_html=True)
    
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
    st.pyplot(plt)

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
    """,unsafe_allow_html=True)
    
    
    
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
        st.markdown(
        """
        <div style="font-size: 20px; font-weight: bold; text-align: center;">
        Dickey-Fuller Test Results
        </div>
        """,unsafe_allow_html=True)      
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

    <h3>Pejelasan:</h3>

    <p>Statistik uji (<strong>0,4295</strong>) jauh lebih besar dari ketiga nilai kritis (<strong>-3,4356</strong>, <strong>-2,8639</strong>, <strong>-2,5680</strong>). Artinya, nilai p (<strong>0,9826</strong>) juga jauh lebih besar dibandingkan tingkat signifikansinya (biasanya ditetapkan pada 0,05 atau 0,10). Dengan kata lain, terdapat bukti yang sangat kuat untuk menolak hipotesis nol.</p>
    </div>
    """,unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="font-size: 20px; font-weight: bold; text-align: center;">
        Forecasting
        </div>
        """,unsafe_allow_html=True)  
    image = Image.open("70.PNG")
    st.image(image,
         use_column_width=True
    )
    st.markdown("""
        <div style="font-size: 18px; line-height: 1.6;">

        <p>
            Grafik menunjukkan pergerakan harga saham AAPL yang mengalami kenaikan signifikan, 
            mencapai angka <strong style="color: #00FF00;">180 dolar</strong>. 
            Prediksi harga untuk tahun selanjutnya menunjukkan tren kenaikan yang lebih curam, 
            dengan nilai yang tidak jauh berbeda dari hasil validasi.
        </p>
        
        <div style="border: 2px solid #ccc; padding: 10px; margin-top: 20px;">
        
        <p><strong>Note:</strong> 
            Grafik menunjukkan bahwa harga saham Apple (AAPL) mengalami kenaikan tajam pada tahun 2021. 
            Harga sahamnya mencapai angka 180 dolar AS per lembar saham, yang merupakan nilai tertinggi baru. 
            Peningkatan harga terjadi karena peluncuran iPhone 12 series 5G oleh Apple pada tahun 2021. 
            Produsen smartphone raksasa ini mencatat penjualan yang kuat di tengah pandemi COVID-19.
        </p>
            
        <p>
            Memasuki tahun 2022, harga saham Apple mengalami fluktuasi akibat tantangan seperti inflasi tinggi, 
            kelangkaan chip komputer global, dan perang Rusia-Ukraina yang memengaruhi rantai pasokan. 
            Meski demikian, performa saham Apple secara keseluruhan tetap stabil dengan baik. 
            Diprediksi pada tahun 2023 harga saham AAPL akan kembali meningkat berdasarkan hasil perhitungan dan 
            prakiraan (forecasting) dari para analis.
        </p>
            
        <p>
            Kenaikan tersebut didorong oleh inovasi dan peluncuran produk-produk baru oleh Apple yang disambut positif investor. 
            Dengan begitu, secara singkat dapat dikatakan bahwa harga saham Apple diperkirakan akan terus menunjukkan tren kenaikan 
            pada masa mendatang, didukung kinerja perusahaan yang solid.
        </p>

        </div>
        
        </div>
    """, unsafe_allow_html=True)


    
