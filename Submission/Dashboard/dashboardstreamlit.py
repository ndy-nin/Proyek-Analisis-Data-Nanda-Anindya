import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Aplikasi
st.title("Analisis Penyewaan Sepeda - Bike Sharing Dataset")

# Load Dataset
@st.cache_data
def load_data():
    # Mengimpor dataset dari file CSV
    day_data = pd.read_csv('https://raw.githubusercontent.com/ndy-nin/Proyek-Analisis-Data-Nanda-Anindya/refs/heads/main/Submission/Dashboard/data/day.csv')
    hour_data = pd.read_csv('https://raw.githubusercontent.com/ndy-nin/Proyek-Analisis-Data-Nanda-Anindya/refs/heads/main/Submission/Dashboard/data/hour.csv')
    return day_data, hour_data

day_data, hour_data = load_data()

# Tampilkan beberapa data untuk dilihat
st.write("Data penyewaan sepeda berdasarkan hari")
st.dataframe(day_data.head())

# Pertanyaan Bisnis 1: Kapan penyewaan sepeda lebih tinggi pada hari kerja atau akhir pekan?
st.subheader("Analisis Penyewaan: Hari Kerja vs Akhir Pekan")

# Visualisasi Penyewaan Sepeda Berdasarkan Hari Kerja dan Akhir Pekan
fig, ax = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=day_data, ax=ax)
ax.set_title('Penyewaan Sepeda: Hari Kerja vs Akhir Pekan')
ax.set_xlabel('Hari Kerja (0 = Akhir Pekan, 1 = Hari Kerja)')
ax.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig)

# Insight Pertanyaan 1
st.write("""
Insight:
- Jumlah penyewaan sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan.
- Ini mungkin terkait dengan banyaknya pengguna sepeda untuk keperluan kerja atau sekolah pada hari kerja.
""")

# Pertanyaan Bisnis 2: Kapan paling banyak penyewaan sepeda terjadi dalam sehari?
st.subheader("Analisis Penyewaan: Jam Sibuk dalam Sehari")

# Mengelompokkan data per jam untuk analisis ini
hour_grouped = hour_data.groupby('hr')['cnt'].mean().reset_index()

# Visualisasi Penyewaan Berdasarkan Jam
fig2, ax2 = plt.subplots()
sns.lineplot(x='hr', y='cnt', data=hour_grouped, ax=ax2)
ax2.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Jam')
ax2.set_xlabel('Jam dalam Sehari')
ax2.set_ylabel('Jumlah Penyewaan Sepeda')
st.pyplot(fig2)

# Insight Pertanyaan 2
st.write("""
Insight:
- Penyewaan sepeda paling tinggi terjadi pada jam sibuk, sekitar jam 08:00 dan 17:00, yang menunjukkan bahwa banyak orang menggunakan sepeda untuk perjalanan ke/dari tempat kerja atau sekolah.
- Jam paling sedikit penyewaan terjadi pada dini hari (antara jam 00:00 - 04:00).
""")

# Kesimpulan
st.subheader("Kesimpulan")
st.write("""
Dari analisis ini, kita dapat menyimpulkan bahwa:
- Hari kerja memiliki tingkat penyewaan sepeda yang lebih tinggi dibandingkan akhir pekan.
- Jam sibuk (pagi dan sore) adalah waktu dengan jumlah penyewaan tertinggi dalam sehari.
""")
