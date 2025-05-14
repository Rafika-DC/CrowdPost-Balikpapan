
import streamlit as st

st.set_page_config(page_title="CrowdPost Balikpapan", layout="centered")

st.title("CrowdPost Balikpapan")
st.write("Situs rekomendasi lokasi tempat tinggal di daerah Balikpapan berdasarkan gaya hidupmu.")

keramaian = st.selectbox("Suka lingkungan seperti apa?", ["Ramai", "Tenang"])
transport = st.selectbox("Butuh akses ke transportasi umum?", ["Ya", "Tidak"])
sd = st.selectbox("Perlu dekat SD?", ["Ya", "Tidak"])
smp = st.selectbox("Perlu dekat SMP?", ["Ya", "Tidak"])
sma_atau_smk = st.selectbox("Perlu dekat SMA atau SMK?", ["Ya", "Tidak"])
kampus = st.selectbox("Perlu dekat kampus?", ["Ya", "Tidak"])
wisata alam = st.selectbox("Ingin dekat dengan wisata alam?", ["Ya", "Tidak"])

data = [
    {"kode": "76111", "nama": "Prapatan & Telaga Sari", "keramaian": "Ramai", "transport": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "kampus": "Tidak", "wisata alam": "Ya"},
    {"kode": "76132", "nama": "Kampung Baru Tengah", "keramaian": "Ramai", "transport": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "kampus": "Tidak", "wisata alam": "Tidak"},
    {"kode": "76124", "nama": "Sumber Rejo & Karang Rejo", "keramaian": "Ramai", "transport": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "kampus": "Tidak", "wisata alam": "Ya"},
    {"kode": "76131", "nama": "Manggar", "keramaian": "Ramai", "transport": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "kampus": "Tidak", "wisata alam": "Ya"},
    {"kode": "76127", "nama": "Karang Joang", "keramaian": "Tenang", "transport": "Tidak", "SD": "Ya", "SMP": "Ya", "SMA/K": "Tidak", "kampus": "Ya", "wisata alam": "Ya"},
    {"kode": "76125", "nama": "Gunung Samarinda", "keramaian": "Ramai", "transport": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "kampus": "Tidak", "wisata alam": "Ya"},
    {"kode": "76114", "nama": "Gunung Bahagia", "keramaian": "Ya", "transpot": "Ya", "SD": "Ya", "SMP": "Ya", "SMA/K": "Ya", "kampus": "Ya", "wisata alam": "Tidak"},
]

if st.button("Cari Rekomendasi"):
    best_match = None
    best_score = -1
    for area in data:
        score = sum([
            area["keramaian"] == keramaian,
            area["transport"] == transport,
            area["SD"] == sd,
            area["SMP"] == smp,
            area["SMA/K"] == sma_atau_smk,
            area["kampus"] == kampus,
            area["wisata alam"] == wisata alam
        ])
        if score > best_score:
            best_score = score
            best_match = area

    if best_match:
        st.success(f"Rekomendasi: {best_match['nama']} (Kode Pos: {best_match['kode']})")
        st.write(f"Keramaian: {best_match['keramaian']}, Transportasi: {best_match['transport']}, "
                 f"SD: {best_match['SD']}, SMP:{best_match['SMP']}, SMP: {best_match['SMP']}, "
                 f"SMA/K: {best_match['SMA/K']}, Kampus: {best_match['kampus']}, Taman: {best_match['taman']}")
    else:
        st.warning("Tidak ditemukan lokasi yang cocok.")
