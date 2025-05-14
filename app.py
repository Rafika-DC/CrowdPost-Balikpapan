
import streamlit as st

st.set_page_config(page_title="KodePos Pintar", layout="centered")

st.title("CrowdPost Balikpapan")
st.write("Situs rekomendasi lokasi tempat tinggal di daerah Balikpapan berdasarkan gaya hidupmu.")

keramaian = st.selectbox("Suka lingkungan seperti apa?", ["Ramai", "Tenang"])
transport = st.selectbox("Butuh akses ke transportasi umum?", ["Ya", "Tidak"])
sekolah dasar = st.selectbox("Perlu dekat sekolah dasar?", ["Ya", "Tidak"])
sekolah menengah pertama = st.selectbox("Perlu dekat sekolah menengah pertama?", ["Ya", "Tidak"])
sekolah menengah atas/kejuruan = st.selectbox("Perlu dekat sekolah menengah atas/kejuruan?", ["Ya", "Tidak"])
kampus = st.selectbox("Perlu dekat kampus?", ["Ya", "Tidak"])
taman = st.selectbox("Suka aktivitas di taman?", ["Ya", "Tidak"])

data = [
    {"kode": "76111", "nama": "Prapatan & Telaga Sari", "keramaian": "Ramai", "transport": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "taman": "Ya"},
    {"kode": "76132", "nama": "Kampung Baru Tengah", "keramaian": "Ramai", "transport": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "taman": "Tidak"},
    {"kode": "76124", "nama": "Sumber Rejo & Karang Rejo", "keramaian": "Ramai", "transport": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "taman": "Ya"},
    {"kode": "76131", "nama": "Manggar", "keramaian": "Ramai", "transport": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "taman": "Ya"},
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
