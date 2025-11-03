📚 UTS Struktur Data — Pencarian Data Paper Mahasiswa

Program ini merupakan implementasi konsep pencarian data (searching) menggunakan Linear Search dan Binary Search dalam mata kuliah Struktur Data. Program membaca data dari file CSV yang berisi informasi paper mahasiswa, kemudian memungkinkan pengguna untuk mencari data berdasarkan nama mahasiswa, judul paper, tahun terbit, atau penulis.

🧠 Fitur Utama

Membaca data paper dari file CSV secara otomatis.

Menerapkan dua metode pencarian:

Linear Search → cocok untuk dataset kecil dan pencarian sederhana.

Binary Search → lebih efisien untuk dataset besar yang sudah terurut.

Menampilkan hasil pencarian secara rapi dan mudah dibaca.

Mampu melakukan pencarian lanjutan berdasarkan judul, tahun, atau penulis.

🏗️ Struktur Kode

Program ini dibangun dengan pendekatan OOP (Object-Oriented Programming) menggunakan class Paper.

Kelas Paper

Menyimpan atribut penting seperti:

no, nim, namaMahasiswa

sumberDatabase, fokusKataKunci

title, year, author

abstractText, conclusion, link

Fungsi Utama

display_paper(p) → menampilkan detail paper secara rapi.

linear_search(papers, keyword) → mencari berdasarkan nama mahasiswa.

binary_search(papers_sorted, keyword) → pencarian cepat pada data terurut.

main() → mengatur alur utama program (input, pencarian, dan output).

⚙️ Cara Menjalankan Program

Pastikan kamu sudah menyiapkan file CSV dataset (misal: Struktur_Data_Dataset_Kelas_A_B_C.csv).

Letakkan file tersebut di direktori yang sesuai dengan path di dalam kode.

Jalankan program menggunakan terminal atau IDE:

python main.py


Ketik nama mahasiswa yang ingin dicari.

Pilih metode pencarian (linear atau binary).

Setelah hasil muncul, kamu bisa mempersempit pencarian berdasarkan judul, tahun, atau penulis.

🧩 Contoh Output
Masukkan nama mahasiswa yang ingin dicari: firdaus
Pilih metode pencarian - linear atau binary: linear

Ditemukan 2 jurnal untuk mahasiswa 'firdaus':
1. Peran Prosesor dalam Memfasilitasi AI (2023) - John Doe
2. Optimasi Jaringan IoT (2022) - Jane Smith

🧑‍💻 Kontributor

Muhammad Hafirst Firdaus
Informatics Student — Universitas Sultan Ageng Tirtayasa
📧 muhammadhafirst@gmail.com

🐙 GitHub: hafirstfirdaus

📄 Lisensi

Proyek ini dibuat untuk keperluan akademik dalam mata kuliah Struktur Data. Bebas digunakan untuk pembelajaran atau referensi.
