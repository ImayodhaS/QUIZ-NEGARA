# 🌍 Bot Kuis Karakteristik Negara (Discord.py)

Proyek ini adalah bot Discord interaktif berbasis teks untuk bermain kuis tebak karakteristik negara. Proyek ini dibuat terstruktur dengan memisahkan file logika data dan file utama bot agar kode tetap bersih dan mudah dikembangkan.

## 👥 Anggota Kelompok
* [Nama Anggota 1] - (Tugas: Programmer Utama / Bot Setup)
* [Nama Anggota 2] - (Tugas: Penyusun Data Soal / Logika Kuis)
* [Nama Anggota 3] - (Tugas: Tester & Dokumentasi)

---

## 🛠️ Struktur File Proyek
Proyek ini terdiri dari dua file Python utama:
1. main.py : Berisi konfigurasi bot Discord, pengaturan hak akses (Intents), pesan tampilan (Embed), dan perintah chat (commands).
2. logikakuis.py : Berisi bank data kuis (pertanyaan pilihan ganda) dan fungsi logika untuk memilih soal acak serta memeriksa jawaban.

---

## 🚀 Fitur Bot
* *Pilihan Ganda Teks:* Menampilkan soal karakteristik negara (terbesar, terkecil, terpadat) lengkap dengan pilihan opsi (A, B, C, D).
* *Tampilan Estetik (Embed):* Menggunakan kotak pesan premium berwarna oranye khas Discord agar terlihat rapi dan profesional.
* *Sistem Memori Channel:* Bot mengingat kuis yang sedang berjalan di setiap channel chat agar kunci jawaban tidak tertukar.
* *Anti-Typo Case Insensitive:* Pengguna bisa menjawab dengan huruf besar maupun kecil (contoh: !jawab rusia atau !jawab Rusia tetap dianggap benar).

---

## 🎮 Cara Menggunakan di Discord

1. *Memulai Kuis*
   Ketik perintah berikut di channel Discord untuk mengeluarkan soal secara acak:
   ```text
   !kuis
Bot akan memunculkan kotak pertanyaan beserta opsi jawaban.

Menjawab Kuis
Lihat pilihan jawaban yang ada, lalu ketik perintah diikuti dengan nama negaranya secara langsung:

Plaintext
!jawab [Nama Negara]
Contoh: !jawab Singapura atau !jawab Vatikan

💻 Cara Menjalankan Proyek (Bagi Pengembang)
Pastikan sudah menginstal pustaka discord.py di komputer:

Bash
pip install discord.py
Buka file main.py dan ganti bagian bot.run('TOKEN_BOT_DISCORD_KAMU') dengan Token Bot Discord milik kelompok kalian yang diambil dari Discord Developer Portal.

Jalankan file main.py:

Bash
python main.py