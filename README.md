# Proyek Analisis Data 

## Setup Environment - Shell/Terminal
```
cd dashboardstreamlit.py
pip install requirements.txt
```

## Run steamlit app
```
streamlit run dashboardstreamlit.py
```
# Proyek Analisis Data Penyewaan Sepeda

## Deskripsi
Proyek ini bertujuan untuk menganalisis data penyewaan sepeda untuk mengetahui pola penggunaan sepeda berdasarkan hari kerja dan akhir pekan. Analisis dilakukan menggunakan Python dengan pustaka seperti Pandas, Matplotlib, dan Streamlit.

## Dataset
Dataset yang digunakan dalam proyek ini adalah `dataset.csv`, yang berisi informasi tentang penyewaan sepeda. Data mencakup kolom-kolom berikut:
- `tanggal`: Tanggal penyewaan
- `jumlah_penyewaan`: Jumlah sepeda yang disewakan
- `hari`: Hari penyewaan (kerja/akhir pekan)

## Analisis Data
Analisis dilakukan dengan langkah-langkah berikut:
1. **Pembersihan Data**: Menghapus data yang tidak relevan dan mengisi nilai yang hilang.
2. **Analisis Deskriptif**: Menghitung total penyewaan sepeda berdasarkan hari kerja dan akhir pekan.
3. **Visualisasi Data**: Membuat grafik untuk memvisualisasikan data penyewaan sepeda.

## Teknologi yang Digunakan
- Python 3.12.7
- Pandas
- Matplotlib
- Streamlit
