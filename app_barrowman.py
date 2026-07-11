import streamlit as st

# Pengaturan Konfigurasi Halaman (Harus di paling atas)
st.set_page_config(
    page_title="Kalkulator CP & CG Minimum Roket Air",
    page_icon="🚀",
    layout="wide"
)

# --- HEADER APLIKASI ---
st.markdown("<h1 style='text-align: center; color: #0066cc;'>🚀 Aplikasi Stabilitas Roket Air Barrowman</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px; opacity: 0.9;'>Menggunakan Persamaan Barrowman • Ilustrasi Interaktif untuk Pengukuran Sederhana</p>", unsafe_allow_html=True)
st.write("---")

# --- PEMBAGIAN KOLOM UTAMA (KIRI & KANAN) ---
col_kiri, col_kanan = st.columns([1, 1], gap="large")

# =========================================================
# SISI KIRI: TUJUAN APLIKASI & ILUSTRASI
# =========================================================
with col_kiri:
    # --- KOTAK TUJUAN APLIKASI (Sekarang di paling atas sisi kiri) ---
    st.markdown("<h3 style='color: #0066cc;'>🎯 Tujuan Penelitian</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div style="background-color: #f8fafc; padding: 20px; border-radius: 12px; border-left: 5px solid #0066cc; color: #444; margin-bottom: 25px;">
        <ul style="margin-bottom: 0; padding-left: 20px;">
            <li style="margin-bottom: 8px;">Penelitian ini digunakan untuk menguji pengaruh tekanan udara dan volume air terhadap jarak luncur roket berdasarkan hukum fisika.</li>
            <li>Perhitungan menggunakan persamaan Barrowman klasik (1967), dan akurasi cukup akurat pada perhitungan roket air sederhana.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- ILUSTRASI ROKET AIR ---
    st.markdown("<h3 style='text-align: center; color: #0066cc;'>📏 Ilustrasi Roket Air (Ukuran cm)</h3>", unsafe_allow_html=True)
    
    # Render SVG Ilustrasi Roket
    svg_code = """
    <div style="display: flex; justify-content: center;">
        <svg width="100%" max-width="520px" height="400" viewBox="0 0 520 420" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(10px 15px 20px rgba(0, 102, 204, 0.15));">
            <rect x="210" y="130" width="100" height="220" rx="8" ry="8" fill="#00aaff" stroke="#222" stroke-width="12"/>
            <polygon points="260,60 210,130 310,130" fill="#ff8800" stroke="#222" stroke-width="12"/>
            <ellipse cx="260" cy="105" rx="48" ry="22" fill="#fff" opacity="0.3"/>
            <polygon points="210,340 140,340 210,290" fill="#ff4400" stroke="#222" stroke-width="10"/>
            <polygon points="310,340 380,340 310,290" fill="#ff4400" stroke="#222" stroke-width="10"/>
            <polygon points="235,355 235,380 285,380 285,355" fill="#ff4400" stroke="#222" stroke-width="8" opacity="0.85"/>
            <line x1="260" y1="65" x2="260" y2="125" stroke="#222" stroke-width="3" stroke-dasharray="4,4"/>
            <text x="275" y="95" font-family="sans-serif" font-weight="600" font-size="13" fill="#222">L_n</text>
            <text x="275" y="110" font-family="sans-serif" font-weight="600" font-size="11" fill="#222">Panjang Nose</text>
            <line x1="310" y1="135" x2="310" y2="335" stroke="#222" stroke-width="3" stroke-dasharray="4,4"/>
            <text x="325" y="230" font-family="sans-serif" font-weight="600" font-size="13" fill="#222">L_b</text>
            <text x="325" y="245" font-family="sans-serif" font-weight="600" font-size="11" fill="#222">Panjang Badan</text>
            <line x1="200" y1="180" x2="200" y2="220" stroke="#222" stroke-width="3"/>
            <line x1="320" y1="180" x2="320" y2="220" stroke="#222" stroke-width="3"/>
            <text x="165" y="205" font-family="sans-serif" font-weight="600" font-size="13" fill="#222">D</text>
            <line x1="210" y1="315" x2="210" y2="340" stroke="#222" stroke-width="3"/>
            <line x1="210" y1="340" x2="140" y2="340" stroke="#222" stroke-width="3"/>
            <text x="160" y="355" font-family="sans-serif" font-weight="600" font-size="13" fill="#222">C_r</text>
            <line x1="140" y1="340" x2="210" y2="290" stroke="#222" stroke-width="2" stroke-dasharray="3,3"/>
            <text x="125" y="325" font-family="sans-serif" font-weight="600" font-size="13" fill="#222">C_t</text>
            <line x1="210" y1="315" x2="140" y2="315" stroke="#222" stroke-width="3"/>
            <text x="170" y="305" font-family="sans-serif" font-weight="600" font-size="13" fill="#222">S</text>
            <text x="20" y="30" font-family="sans-serif" font-size="14" fill="#0066cc" font-weight="600">Roket Air PET Bottle + Sirip</text>
            <text x="20" y="48" font-family="sans-serif" font-size="12" fill="#555">Sirip dipasang di ujung belakang</text>
            <text x="20" y="390" font-family="sans-serif" font-size="12" fill="#555">Ukur semua dimensi dengan penggaris</text>
        </svg>
    </div>
    """
    st.components.v1.html(svg_code, height=410)
    
    # Info Catatan Pengukuran di bawah gambar
    st.info("**Catatan:**\n\n* Gambar di atas menunjukkan semua ukuran yang dibutuhkan.\n* Ukuran dalam **cm**, harap sesuaikan input sesuai pengukuran roket Anda.")

# =========================================================
# SISI KANAN: PANEL INPUT & LOGIKA BARROWMAN
# =========================================================
with col_kanan:
    st.markdown("<h3 style='color: #0066cc;'>📋 Masukkan Data Ukuran Roket</h3>", unsafe_allow_html=True)
    
    # Input panel grid menggunakan sub-columns streamlit
    grid_col1, grid_col2 = st.columns(2)
    
    with grid_col1:
        D = st.number_input("Diameter Badan (D) dalam cm", value=8.5, step=0.1, min_value=1.0)
        Ln = st.number_input("Panjang Nose (L_n) dalam cm", value=15.0, step=0.1, min_value=1.0)
        nose_type = st.selectbox("Tipe Nose", ["Ogive (Bulat seperti botol PET)", "Cone (Kerucut)"])
        Lb = st.number_input("Panjang Badan (L_b) dalam cm", value=28.0, step=0.1, min_value=1.0)
        
    with grid_col2:
        num_fins = st.selectbox("Jumlah Sirip (N)", [4, 3])
        Cr = st.number_input("Panjang Akar Sirip (C_r) dalam cm", value=12.0, step=0.1, min_value=1.0)
        Ct = st.number_input("Panjang Ujung Sirip (C_t) dalam cm", value=4.0, step=0.1, min_value=0.0)
        S = st.number_input("Rentang Sirip / Span (S) dalam cm", value=10.0, step=0.1, min_value=1.0)
        
    # --- PROSES PERHITUNGAN (LOGIKA BARROWMAN PYTHON) ---
    nose_factor = 0.466 if "Ogive" in nose_type else 0.666
    
    CNn = 2.0
    Xn = Ln * nose_factor
    
    if Cr > 0 and (1 + Ct / Cr) != 0:
        CNf = num_fins * (4.0 * S * S) / (Cr * (1.0 + Ct / Cr))
    else:
        CNf = 0
        
    Xb = Ln + Lb - Cr
    
    if (Cr + Ct) != 0:
        Xfcp = ((Cr + 2.0 * Ct) / (3.0 * (Cr + Ct))) * Cr
    else:
        Xfcp = 0
        
    Xf = Xb + Xfcp
    totalCN = CNn + CNf
    
    if totalCN != 0:
        Xcp = (CNn * Xn + CNf * Xf) / totalCN
    else:
        Xcp = 0
        
    # Margin Stabilitas
    num_D = D
    CG_min = Xcp - num_D

    # --- PANEL HASIL ---
    st.write("")
    st.markdown("<h3 style='color: #0066cc;'>📊 Hasil Perhitungan (Metode Barrowman)</h3>", unsafe_allow_html=True)
    
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.metric(label="Posisi CP dari ujung nose", value=f"{Xcp:.2f} cm")
    with res_col2:
        st.metric(label="Posisi CG Minimum (stabilitas 1 kaliber)", value=f"{CG_min:.2f} cm")
        
    st.success(f"✅ **Stabilitas baik** jika posisi CG roket asli Anda **lebih kecil** dari posisi CG Minimum ({CG_min:.2f} cm). (CG harus berada di depan CP minimal 1× diameter badan roket)")
    
    # Expander untuk Catatan Formula Fisika
    with st.expander("📝 Lihat Rumus & Catatan Persamaan Barrowman"):
        st.markdown("""
        Perhitungan ini berlaku untuk aliran udara subsonik & sudut serang roket yang kecil.
        * $CN_{nose} = 2$
        * $CN_{fins} = \\frac{N \\times 4S^2}{C_r \\times (1 + \\frac{C_t}{C_r})}$
        * Kontribusi aerodinamis bodi silinder diabaikan karena kecil.
        * Margin stabilitas aman = 1 kaliber (D).
        """)

# --- FOOTER ---
st.write("")
st.write("")
st.markdown("<p style='text-align: center; color: #555; font-size: 13px; border-top: 1px solid #eee; padding-top: 20px;'>Aplikasi dibuat oleh tim SMPN 13 dalam rangka lomba Olimpiade Penelitian Siswa Yogyakarta(OPSY) tahun 2026, Anabel Fidelia Ariwibowo dan Dhia Tsurayya Santoso.</p>", unsafe_allow_html=True)
