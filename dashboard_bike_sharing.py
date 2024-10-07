# Nama          : R. Muhammad Luqman Harjito
# Email         : lukmanmsoediro@gmail.com
# Id Dicoding   : muhammad_luqman

# Import Library
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==============================
# LOAD DATA
# ==============================


@st.cache_resource
def load_data():
    data = pd.read_csv("dataset/Bike-sharing-dataset/hour.csv")
    return data


data = load_data()


# ==============================
# TITLE DASHBOARD
# ==============================
# Set page title
st.title("Bike Share Dashboard")


st.sidebar.title("Dataset Bike Share")
# Show the dataset
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)

# Display summary statistics
if st.sidebar.checkbox("Show Summary Statistics"):
    st.subheader("Summary Statistics")
    st.write(data.describe())


st.sidebar.markdown('**Cuaca:**')
st.sidebar.markdown('Cuaca Cerah / Berawan: Clear, Few clouds, Partly cloudy')
st.sidebar.markdown('Kabut / Awan Tebal: Mist, Cloudy, Broken clouds, Fog')
st.sidebar.markdown('Hujan Ringan / Salju: Light Rain, Light Snow, Scattered clouds')
st.sidebar.markdown('Cuaca Ekstrem: Heavy Rain, Thunderstorm, Ice Pellets, Snow')





# create a layout with two columns
col1, col2 = st.columns(2)

with col1:
    # Season-wise bike share count
    # st.subheader("Season-wise Bike Share Count")

    # Mapping dari angka ke label musim
    season_mapping = {1: "semi", 2: "panas", 3: "gugur", 4: "dingin"}
    data["musim_label"] = data["season"].map(season_mapping)

    season_count = data.groupby("musim_label")["cnt"].sum().reset_index()
    fig_season_count = px.bar(season_count, x="musim_label",
                              y="cnt", title="Season-wise Bike Share Count")
    st.plotly_chart(fig_season_count, use_container_width=True,
                    height=400, width=600)

with col2:
    # Weather situation-wise bike share count
    # st.subheader("Weather Situation-wise Bike Share Count")

    # Membuat mapping dari angka cuaca ke deskripsi
    weather_mapping = {
        1: "Cerah",
        2: "Kabut",
        3: "Hujan Ringan",
        4: "Ekstrem"
    }

    # Mengubah kolom weathersit menjadi kategori deskriptif
    data["cuaca_label"] = data["weathersit"].replace(weather_mapping)

    # Mengelompokkan data berdasarkan kategori cuaca yang baru
    weather_count = data.groupby("cuaca_label")["cnt"].sum().reset_index()

    # Membuat bar chart dengan deskripsi cuaca
    fig_weather_count = px.bar(weather_count, x="cuaca_label",
                               y="cnt", title="Weather Situation-wise Bike Share Count")

    # Mengatur tinggi dan lebar gambar
    st.plotly_chart(fig_weather_count, use_container_width=True, height=400, width=800)



# Hourly bike share count
# st.subheader("Hourly Bike Share Count")
hourly_count = data.groupby("hr")["cnt"].sum().reset_index()
fig_hourly_count = px.line(
    hourly_count, x="hr", y="cnt", title="Hourly Bike Share Count")
st.plotly_chart(fig_hourly_count, use_container_width=True,
                height=400, width=600)

# Humidity vs. Bike Share Count
# st.subheader("Humidity vs. Bike Share Count")
fig_humidity_chart = px.scatter(
    data, x="hum", y="cnt", title="Humidity vs. Bike Share Count")
st.plotly_chart(fig_humidity_chart)

# Wind Speed vs. Bike Share Count
# st.subheader("Wind Speed vs. Bike Share Count")
fig_wind_speed_chart = px.scatter(
    data, x="windspeed", y="cnt", title="Wind Speed vs. Bike Share Count")
st.plotly_chart(fig_wind_speed_chart)

# Temperature vs. Bike Share Count
# st.subheader("Temperature vs. Bike Share Count")
fig_temp_chart = px.scatter(data, x="temp", y="cnt",
                            title="Temperature vs. Bike Share Count")
st.plotly_chart(fig_temp_chart, use_container_width=True,
                height=400, width=800)
