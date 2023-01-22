import streamlit as st

st.title(
    'Kalkulator Segitiga'
)
"""
Ini Adalah Kalkulator khusus untuk menghitung segitiga
"""

alas = st.number_input("Alas", 0)
tinggi = st.number_input("Tinggi", 0)
luas = 0.5 * alas * tinggi

hasil = st.button("Hasil")

if hasil:
    st.success(luas)