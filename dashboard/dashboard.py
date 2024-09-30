import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.caption("I Made Treshnanda Mas")

df = pd.read_csv('hour.csv')

st.title("Bike Sharing Demand Dashboard")

st.sidebar.header("Filter Options")

selected_season = st.sidebar.selectbox("Season", options=df['season'].unique())
filtered_df = df[df['season'] == selected_season]

selected_weather = st.sidebar.selectbox("Weather", options=df['weathersit'].unique())
filtered_df = filtered_df[filtered_df['weathersit'] == selected_weather]

st.subheader("Filtered Data")
st.write(filtered_df)

st.subheader("Demand by Hour and Day")
fig, ax = plt.subplots(figsize=(10, 6))
sns.pointplot(x='hr', y='cnt', hue='weekday', data=filtered_df, ax=ax)
plt.title('Demand Sewa Sepeda Berdasarkan Jam dan Hari')
plt.xlabel('Jam')
plt.ylabel('Jumlah Sewa Sepeda')
st.pyplot(fig)

st.subheader("Demand by Hour and Weather")
fig, ax = plt.subplots(figsize=(10, 6))
sns.pointplot(x='hr', y='cnt', hue='weathersit', data=filtered_df, ax=ax)
plt.title('Demand Sewa Sepeda Berdasarkan Jam dan Cuaca')
plt.xlabel('Jam')
plt.ylabel('Jumlah Sewa Sepeda')
st.pyplot(fig)

st.subheader("Registered User Demand by Hour")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='hr', y='registered', data=filtered_df, ax=ax)
plt.title('Distribusi Jumlah Sewa Sepeda Setiap Jam User Terdaftar')
plt.xlabel('Jam')
plt.ylabel('Jumlah')
st.pyplot(fig)

st.subheader("Casual User Demand by Hour")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='hr', y='casual', data=filtered_df, ax=ax)
plt.title('Distribusi Jumlah Sewa Sepeda Setiap Jam User Kasual')
plt.xlabel('Jam')
plt.ylabel('Jumlah')
st.pyplot(fig)