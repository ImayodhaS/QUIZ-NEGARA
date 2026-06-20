# 🌍 Bot Quiz Dunia

Proyek ini adalah bot Discord interaktif berbasis teks untuk bermain kuis tebak karakteristik negara. Proyek ini dibuat terstruktur dengan memisahkan file logika data dan file utama bot agar kode tetap bersih dan mudah dikembangkan.

## 👥 Anggota Kelompok
* Gibran Akhtar Arkananta : Tugas sebagai ketua kelompok dan membuat file README.md, config.py, dan pertanyaan-pertanyaan
* I Made Yogi Dharma Satyawadi : Tugas membuat logic.py dan bot.py

---

## 🛠️ Struktur File Proyek
Proyek ini terdiri dari dua file Python utama:
1.  README.md : Berisi tentang tata cara pengguna bot.
2.  main.py : Berisi konfigurasi bot Discord, pengaturan hak akses (Intents), pesan tampilan (Embed), dan perintah chat (commands).
3. logiC.py : Berisi bank data kuis (pertanyaan pilihan ganda) dan fungsi logika untuk memilih soal acak serta memeriksa jawaban.
4. config.py : Berisi data token bot.

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
   !quiz [nama pemain yang didaftarkan]
Bot akan memunculkan kotak pertanyaan beserta opsi jawaban.

2. Menjawab Kuis
   Lihat pilihan jawaban yang ada, lalu ketik perintah diikuti dengan nama negaranya secara langsung:

   Plaintext
   !jawab [Opsi Jawaan Nama Negara]
   Contoh: !jawab Singapura atau !jawab Vatikan

💻 Cara Menjalankan Proyek (Bagi Pengembang)
Pastikan sudah menginstal pustaka discord.py di komputer:

Bash
pip install discord.py
Buka file config.py dan ganti bagian TOKEN = "MASUKAN TOKEN DISINI" dengan Token Bot Discord milik kelompok kalian yang diambil dari Discord Developer Portal.

Jalankan file main.py:

Bash
python main.py

3.Score
   Untuk melihat Score jawaban anda, ketik Perintah berikut:

   Plaintext
   !Score [Menampilkan papan score]
   !Score [...]
Bot akan memunculkan papan socre


   
   
