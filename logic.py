import random

DATA_KUIS = [
    {
        "pertanyaan": "Negara manakah yang memiliki karakteristik sebagai negara terbesar di dunia berdasarkan luas wilayahnya?",
        "pilihan": ["Kanada", "Amerika Serikat", "Rusia", "Tiongkok"],
        "benar": "Rusia"
    },
    {
        "pertanyaan": "Negara manakah yang terkenal dengan karakteristik sebagai negara terkecil di dunia?",
        "pilihan": ["Vatikan", "Monako", "Malta", "San Marino"],
        "benar": "Vatikan"
    },
    {
        "pertanyaan": "Negara kepulauan di Asia Tenggara yang terkenal sangat maju dan dinobatkan sebagai salah satu negara terpadat di dunia adalah...",
        "pilihan": ["Malaysia", "Singapura", "Thailand", "Filipina"],
        "benar": "Singapura"
    },
    {
        "pertanyaan": "Negara manakah yang memiliki karakteristik sebagai negara terluas nomor satu di benua Afrika?",
        "pilihan": ["Aljazair", "Mesir", "Sudan", "Nigeria"],
        "benar": "Aljazair"
    },
    {
        "pertanyaan": "Negara tetangga Indonesia yang memiliki karakteristik wilayah benua tersendiri dan terkenal dengan hewan kangguru adalah...",
        "pilihan": ["Selandia Baru", "Australia", "Papua Nugini", "Timor Leste"],
        "benar": "Australia"
    },
    {
        "pertanyaan": "Negara Dengan kepulauan terbanyak didunia adalah...",
        "pilihan": ["Swedia", "Norwegia", "Finlandia", "Kanada", "Amerika Serikat"],
        "benar": "Swedia"
    },
    {
        "pertanyaan": " Negara manakah yang memiliki jumlah penduduk paling banyak di dunia adalah...",
        "pilihan": ["India", "Jepang", "Indonesia", "Rusia", "Amerika Serikat"],
        "benar": "India"
    },
    {
        "pertanyaan": " Negara manakah dengan iq tertinggi di dunia adalah...",
        "pilihan": ["Korea utara", "Arab Saudi", "Indonesia", "Rusia", "Korea Selatan"],
        "benar": "Korea Selatan"
    },
    {
        "pertanyaan": " Negara manakah dengan iq terendah di dunia adalah...",
        "pilihan": ["Korea utara", "Nepal", "Indonesia", "Liberia", "China"],
        "benar": "Nepal"
    },
    {
        "pertanyaan": " Negara dengan pasokan minyak terbanyak di dunia? adalah...",
        "pilihan": ["Amerika Utara", "Greenland", "Belanda", " Bolivia", "China"],
        "benar": "Amerika Utara"
    },
    {
        "pertanyaan": " Negara dengan pasokan sumber daya laut terbanyak? adalah...",
        "pilihan": ["Indonesia", "iraq", "Belanda", " Bolivia", "iran"],
        "benar": "Indonesia"
    },
    
]

skor_pemain = {}

def ambil_soal_acak():
    return random.choice(DATA_KUIS)

def periksa_jawaban(soal, jawaban_user):
    if jawaban_user.strip().lower() == soal["benar"].lower():
        return True
    return False

def tambah_skor(nama_pemain):
    if nama_pemain in skor_pemain:
        skor_pemain[nama_pemain] += 10
    else:
        skor_pemain[nama_pemain] = 10
    return skor_pemain[nama_pemain]