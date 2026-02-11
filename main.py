import streamlit as st
import sys
import os

# --- FIX UNTUK MODULE NOT FOUND ---
# Mengambil path absolut dari file main.py
root_path = os.path.dirname(os.path.abspath(__file__))
# Masukkan ke dalam daftar pencarian Python
if root_path not in sys.path:
    sys.path.insert(0, root_path)

# Sekarang panggil modul dengan aman
try:
    from modules.inspection import mechanical
except Exception as e:
    st.error(f"Gagal memuat modul. Detail Error: {e}")
    st.info(f"Root Path: {root_path}")
    st.info(f"Isi Folder Root: {os.listdir(root_path)}")

# --- 1. KONFIGURASI HALAMAN (WAJIB PALING ATAS) ---
st.set_page_config(
    page_title="Reliability Assistant",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="collapsed" # Sidebar tertutup agar fokus
)

# --- 2. CSS CUSTOM (AGAR TAMPILAN PROFESIONAL) ---
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
    }
    h1 { color: #1e3799; }
    h2 { color: #4a69bd; }
    div[data-testid="stMetricValue"] {
        font-size: 1.4rem; 
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER GLOBAL ---
col1, col2 = st.columns([0.1, 0.9])
with col1:
    # Anda bisa ganti URL ini dengan logo Pertamina jika ada
    st.image("https://cdn-icons-png.flaticon.com/512/2912/2912288.png", width=60)
with col2:
    st.title("Digital Reliability Assistant")
    st.caption("PT Pertamina Patra Niaga - Infrastructure Management & Project")

st.divider()

# --- 4. PEMANGGILAN MODUL (INTI APLIKASI) ---
try:
    # Memanggil fungsi render dari mechanical.py
    # Fungsi ini yang akan menarik logic dari analyzers.py & decision_engine.py
    mechanical.render_mechanical_page()

except Exception as e:
    st.error(f"Terjadi Kesalahan Sistem: {e}")
    st.warning("Pastikan struktur folder 'modules/' sudah benar.")

# --- 5. FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: grey; font-size: 0.8em;'>
        Developed for Reliability OJT Project | © 2026
    </div>
    """, 
    unsafe_allow_html=True
)
