import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Import dataset lengkap_df
lengkap_df = pd.read_csv("dashboard/lengkap_df.csv")

st.title('Olist E-Commerce Public Data Analysis')

# Eksplorasi data untuk menemukan review terbaik pada kategori produk
product_category_review_tertinggi = lengkap_df[lengkap_df['review_score'] == 5]
category_rating_5 = product_category_review_tertinggi.groupby('product_category_name_english').size().reset_index(name='Jumlah Rating 5')
category_rating_5 = category_rating_5.sort_values(by='Jumlah Rating 5', ascending=False).reset_index(drop=True)
category_rating_5_topTen = category_rating_5[1:11]

# Eksplorasi data untuk menemukan review terburuk pada kategori produk
product_category_review_tertinggi = lengkap_df[lengkap_df['review_score'] == 1]
category_rating_1 = product_category_review_tertinggi.groupby('product_category_name_english').size().reset_index(name='Jumlah Rating 1')
category_rating_1 = category_rating_1.sort_values(by='Jumlah Rating 1', ascending=False).reset_index(drop=True)
category_rating_1_topTen = category_rating_1[1:11]



# Eksplorasi data untuk menemukan kategori produk dengan orderan terbanyak dan tidak dicancel
lengkap_df['order_status'] = 1
lengkap_df.rename(columns={'order_status': 'total_order'}, inplace=True)
product_and_order_status = lengkap_df.groupby('product_category_name_english')['total_order'].sum().sort_values(ascending=False).reset_index()

# Eksplorasi data untuk menemukan kategori produk dengan orderan paling sedikit dan tidak dicancel
product_and_order_status_tidak_laku = lengkap_df.groupby('product_category_name_english')['total_order'].sum().sort_values(ascending=True).reset_index()

with st.container():
    st.header("Kategori Produk Terlaris")
    # Visualisasi data kategori produk yang memiliki pesanan terbanyak dan tidak dicancel
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(y='product_category_name_english', x='total_order', data=product_and_order_status.head(), orient='h', palette=colors)
    plt.xlabel("Total Order")
    plt.ylabel("Nama Kategori Produk")
    plt.title("Kategori Produk Terlaris")
    plt.tick_params(axis ='y', labelsize=12)
    st.pyplot(plt)
    plt.clf()
    st.write("Berdasarkan visualisasi data di atas didapatkan bahwa bed_bath_table merupakan kategori produk terlaris.")

    st.header("Kategori Produk yang Tidak Laris")

    # Visualisasi data kategori produk yang memiliki pesanan terbanyak dan tidak dicancel
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(y='product_category_name_english', x='total_order', data=product_and_order_status_tidak_laku.head(), orient='h', palette=colors)
    plt.xlabel("Total Order")
    plt.ylabel("Nama Kategori Produk")
    plt.title("Kategori Produk Tidak Laris")
    plt.tick_params(axis ='y', labelsize=12)
    st.pyplot(plt)
    plt.clf()
    st.write("Berdasarkan visualisasi data di atas didapatkan bahwa seurity_and_services merupakan kategori produk paling tidak laris.")

    st.header("Kategori Produk dengan Review Terbaik")

    # Visualisasi data kategori produk dengan review terbaik
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(y='product_category_name_english', x='Jumlah Rating 5', data=category_rating_5_topTen.head(), orient='h', palette=colors)
    plt.xlabel("Pelanggan")
    plt.ylabel("Nama Kategori Produk")
    plt.title("Kategori Produk dengan Review Sempurna Terbanyak")
    plt.tick_params(axis ='y', labelsize=12)
    st.pyplot(plt)
    plt.clf()
    st.write("Visualisasi di atas merupakan 5 kategori produk dengan review 5 terbanyak.")
    
    st.header("Kategori Produk dengan Review Terburuk")

    # Visualisasi data kategori produk dengan review terbaik
    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(y='product_category_name_english', x='Jumlah Rating 1', data=category_rating_1_topTen.head(), orient='h', palette=colors)
    plt.xlabel("Pelanggan")
    plt.ylabel("Nama Kategori Produk")
    plt.title("Kategori Produk dengan Review Rendah Terbanyak")
    plt.tick_params(axis ='y', labelsize=12)
    st.pyplot(plt)
    plt.clf()
    st.write("Visualisasi di atas merupakan 5 kategori produk dengan review 1 terbanyak.")
