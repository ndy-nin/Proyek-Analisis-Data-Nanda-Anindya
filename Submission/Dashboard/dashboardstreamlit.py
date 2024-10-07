import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Aplikasi
st.title("Analisis Penyewaan Sepeda - Bike Sharing Dataset")

# Load Dataset dari GitHub
@st.cache_data
def load_data():
    # Mengimpor dataset dari file CSV di GitHub
    day_data = pd.read_csv('https://raw.githubusercontent.com/ndy-nin/Proyek-Analisis-Data-Nanda-Anindya/refs/heads/main/Submission/Dashboard/data/day.csv')
    hour_data = pd.read_csv('https://raw.githubusercontent.com/ndy-nin/Proyek-Analisis-Data-Nanda-Anindya/refs/heads/main/Submission/Dashboard/data/hour.csv')
    return day_data, hour_data

day_data, hour_data = load_data()

# 1. Visualisasi Penyewaan Sepeda per Hari
st.subheader("1. Visualisasi Penyewaan Sepeda per Hari")

# Mengelompokkan data berdasarkan hari dan menjumlahkan total penyewaan
daily_rentals = day_data.groupby('weekday')['cnt'].sum().reset_index()

# Menentukan nama hari untuk visualisasi
daily_rentals['weekday'] = daily_rentals['weekday'].map({0: 'Senin', 1: 'Selasa', 2: 'Rabu', 3: 'Kamis', 4: 'Jumat', 5: 'Sabtu', 6: 'Minggu'})

# Visualisasi Bar Chart
fig1, ax1 = plt.subplots()
ax1.bar(x=daily_rentals['weekday'], height=daily_rentals['cnt'], color='skyblue')
ax1.set_xlabel("Hari")
ax1.set_ylabel("Jumlah Penyewaan")
ax1.set_title("Jumlah Penyewaan Sepeda per Hari")
st.pyplot(fig1)

# 2. Distribusi Penyewaan Sepeda per Hari
st.subheader("2. Distribusi Penyewaan Sepeda per Hari")

# Membuat Pie Chart
fig2, ax2 = plt.subplots()
ax2.pie(
    daily_rentals['cnt'],
    labels=daily_rentals['weekday'],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('pastel'),
)
ax2.set_title("Distribusi Penyewaan Sepeda per Hari")
st.pyplot(fig2)

# 3. Total Penyewaan Sepeda Berdasarkan Hari dan Jam
st.subheader("3. Total Penyewaan Sepeda Berdasarkan Hari dan Jam")

# Mengelompokkan data berdasarkan hari dan jam, kemudian menjumlahkan jumlah penyewaan sepeda (cnt)
hour_data['day_of_week'] = pd.to_datetime(hour_data['dteday']).dt.day_name()
hourly_counts = hour_data.groupby(['day_of_week', 'hr'])['cnt'].sum().reset_index()

# Mengatur urutan hari
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hourly_counts['day_of_week'] = pd.Categorical(hourly_counts['day_of_week'], categories=days_order, ordered=True)

# Visualisasi Bar Chart untuk total penyewaan sepeda berdasarkan hari dan jam
fig3, ax3 = plt.subplots(figsize=(14, 7))
sns.barplot(data=hourly_counts, x='hr', y='cnt', hue='day_of_week', palette='viridis', ax=ax3)
ax3.set_title('Total Penyewaan Sepeda Berdasarkan Hari dan Jam')
ax3.set_xlabel('Jam')
ax3.set_ylabel('Jumlah Penyewaan')
st.pyplot(fig3)

# 4. Insight dari day.csv
st.subheader("4. Insight dari Dataset day.csv")
st.write("""
- Rata-rata jumlah penyewaan sepeda (cnt) adalah 4504, dengan pengguna terdaftar (registered) berjumlah 3656 dan pengguna kasual (casual) 848.
- Penyewaan sepeda cenderung lebih tinggi pada hari kerja dibandingkan hari libur, dengan proporsi hari kerja (workingday) sekitar 68.4%.
- Penyewaan sepeda meningkat pada bulan yang lebih hangat (musim semi dan musim panas), dengan puncak penyewaan terjadi sekitar bulan Juni hingga Oktober.
- Terdapat korelasi yang kuat antara variabel `yr` dan `cnt` (0.87), menunjukkan peningkatan jumlah penyewaan sepeda dari tahun ke tahun.
""")

# 5. Insight dari hour.csv
st.subheader("5. Insight dari Dataset hour.csv")
st.write("""
- Rata-rata penyewaan sepeda per jam (cnt) adalah 189, dengan puncak penyewaan pada jam 8-9 pagi dan 5-6 sore.
- Pengguna kasual lebih banyak menyewa di pagi dan sore hari, sedangkan pengguna terdaftar menyewa lebih konsisten sepanjang hari.
- Kondisi cuaca (temp) juga mempengaruhi penyewaan sepeda, dengan suhu yang lebih tinggi cenderung meningkatkan jumlah penyewaan.
- Penyewaan sepeda tertinggi terjadi pada hari Sabtu, khususnya pada jam 5 sore, menandakan bahwa banyak pengguna menyewa sepeda untuk kegiatan rekreasi akhir pekan.
""")

# 6. Kesimpulan Pertanyaan 1
st.subheader("6. Kesimpulan Pertanyaan 1: Penyewaan Sepeda Berdasarkan Hari")
st.write("""
Penyewaan tertinggi terjadi pada hari Sabtu, menunjukkan bahwa akhir pekan adalah waktu populer bagi pengguna sepeda, terutama untuk aktivitas rekreasi.
""")

# 7. Kesimpulan Pertanyaan 2
st.subheader("7. Kesimpulan Pertanyaan 2: Jam Penyewaan Tertinggi")
st.write("""
Penyewaan sepeda terbanyak terjadi pada pukul 17.00, menandakan bahwa banyak pengguna menyewa sepeda untuk pulang dari tempat kerja atau untuk kegiatan rekreasi sore hari.
""")

# Tambahan Analisis Bisnis
st.subheader("Analisis Bisnis untuk Pertanyaan:")
# Pertanyaan: Kapan penyewaan sepeda lebih tinggi pada hari kerja atau akhir pekan?
weekday_rentals = day_data.groupby('workingday')['cnt'].sum().reset_index()
st.write("""
Dari data, penyewaan sepeda lebih tinggi pada hari kerja dibandingkan akhir pekan. Hal ini dapat dimanfaatkan oleh perusahaan sepeda untuk meningkatkan strategi pemasaran yang lebih aktif pada hari kerja, seperti promosi untuk pelanggan tetap atau meningkatkan layanan selama jam sibuk.
""")

# Pertanyaan: Kapan paling banyak penyewaan sepeda terjadi dalam sehari?
hourly_peak = hourly_counts.groupby('hr')['cnt'].sum().reset_index().sort_values(by='cnt', ascending=False).iloc[0]
st.write(f"""
Penyewaan sepeda paling banyak terjadi pada jam {hourly_peak['hr']}:00 dengan total {hourly_peak['cnt']} penyewaan. Ini menunjukkan bahwa periode sore hari, khususnya jam 17.00, adalah waktu paling ramai untuk penyewaan sepeda, sehingga waktu tersebut sangat penting untuk memastikan ketersediaan sepeda di berbagai lokasi penyewaan.
""")
