
import streamlit as st

st.set_page_config(page_title="KodePos Pintar", layout="centered")

st.title("KodePos Pintar")
st.write("Sistem rekomendasi lokasi tempat tinggal berdasarkan gaya hidupmu.")

keramaian = st.selectbox("Suka lingkungan seperti apa?", ["Ramai", "Tenang"])
transport = st.selectbox("Butuh akses ke transportasi umum?", ["Ya", "Tidak"])
sekolah = st.selectbox("Perlu dekat sekolah/kampus?", ["Ya", "Tidak"])
taman = st.selectbox("Suka aktivitas di taman?", ["Ya", "Tidak"])

data = [
    {"kode": "76111", "nama": "Prapatan & Telaga Sari", "keramaian": "Ramai", "transport": "Ya", "sekolah": "Ya", "taman": "Ya"},
    {"kode": "67890", "nama": "Daerah B", "keramaian": "Tenang", "transport": "Tidak", "sekolah": "Ya", "taman": "Ya"},
    {"kode": "54321", "nama": "Daerah C", "keramaian": "Tenang", "transport": "Ya", "sekolah": "Tidak", "taman": "Ya"},
]

if st.button("Cari Rekomendasi"):
    best_match = None
    best_score = -1
    for area in data:
        score = sum([
            area["keramaian"] == keramaian,
            area["transport"] == transport,
            area["sekolah"] == sekolah,
            area["taman"] == taman
        ])
        if score > best_score:
            best_score = score
            best_match = area

    if best_match:
        st.success(f"Rekomendasi: {best_match['nama']} (Kode Pos: {best_match['kode']})")
        st.write(f"Karakteristik: {best_match['keramaian']}, Transport: {best_match['transport']}, "
                 f"Sekolah: {best_match['sekolah']}, Taman: {best_match['taman']}")
    else:
        st.warning("Tidak ditemukan lokasi yang cocok.")
