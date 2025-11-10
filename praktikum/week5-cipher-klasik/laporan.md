# Laporan Praktikum Kriptografi
Minggu ke-: 5  
Topik: Cipher Klasik 
Nama: Fiqri Nur Hidayanto 
NIM: 230202754  
Kelas: 5IKKA  

---

## 1. Tujuan
1. Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
2. Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
3. Mengimplementasikan algoritma transposisi sederhana.
4. Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
1. Pengertian Cipher Klasik

Cipher klasik adalah metode penyandian (enkripsi) yang digunakan sebelum berkembangnya komputer modern. Teknik ini berfokus pada manipulasi huruf atau karakter dalam pesan asli (plaintext) menjadi bentuk sandi (ciphertext) menggunakan aturan tertentu. Tujuannya adalah menjaga kerahasiaan pesan agar tidak dapat dibaca oleh pihak yang tidak berwenang.
Cipher klasik merupakan bagian awal dari kriptografi, yaitu ilmu yang mempelajari cara mengamankan informasi melalui proses penyandian (enkripsi) dan pengembalian (dekripsi).

2. Konsep Dasar Kriptografi

    Dalam sistem kriptografi klasik, terdapat beberapa komponen utama:
    1. Plaintext → Pesan asli yang ingin dikirim atau disembunyikan.
    2. Ciphertext → Hasil penyandian dari plaintext.
    3. Cipher / Algoritma Enkripsi → Metode atau aturan untuk mengubah plaintext menjadi ciphertext.
    4. Kunci (Key) → Nilai atau parameter rahasia yang digunakan dalam proses enkripsi dan dekripsi.
    5. Dekripsi → Proses mengembalikan ciphertext menjadi plaintext menggunakan kunci.

3. Jenis-Jenis Cipher Klasik
    Cipher klasik terbagi menjadi dua kategori utama:
    a. Substitution Cipher (Sandi Substitusi)
    Setiap huruf pada plaintext digantikan (disubstitusi) oleh huruf lain berdasarkan aturan tertentu.
    Contohnya:
    - Caesar Cipher
    Menggeser setiap huruf sebanyak n posisi dalam alfabet.
    Misal dengan pergeseran 3:
    Plaintext: A B C D E
    Ciphertext: D E F G H
    
    - Monoalphabetic Cipher
    Setiap huruf plaintext diganti oleh huruf lain dengan pemetaan acak, bukan hanya bergeser.
    Misalnya:
    A → Q
    B → W
    C → E, dst.

    - Polyalphabetic Cipher (contoh: Vigenère Cipher)
    Menggunakan beberapa alfabet pengganti tergantung pada posisi huruf dan kunci.

    b. Transposition Cipher (Sandi Transposisi)
    Tidak mengganti huruf, tetapi mengubah urutan posisi huruf dalam pesan.
    Contohnya:
    - Rail Fence Cipher
    Menulis pesan dengan pola zigzag di beberapa “rel”, lalu dibaca per baris.

    - Columnar Transposition Cipher
    Pesan ditulis dalam bentuk tabel berdasarkan panjang kunci, lalu dibaca per kolom sesuai urutan huruf kunci.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
LAngkah 1 — Implementasi Caesar Cipher
langkah 2 — Implementasi Vigenère Cipher
langkah 3 — Implementasi Transposisi Sederhana

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: 
    1. Kelemahan Utama Caesar Cipher
        a. Ruang kunci yang sangat kecil
        Caesar Cipher hanya memiliki 25 kemungkinan kunci (karena ada 26 huruf dalam alfabet, dan pergeseran 0 tidak mengubah pesan).
        Ini berarti mudah dipecahkan dengan brute force, cukup coba semua kemungkinan pergeseran.
        
        b. Pola frekuensi huruf tidak berubah
        Caesar Cipher hanya menggeser huruf tanpa mengacak frekuensinya.
        Jadi, huruf yang paling sering muncul dalam ciphertext tetap mewakili huruf yang paling sering muncul dalam plaintext.
        Hal ini membuat cipher ini mudah dipecahkan dengan analisis frekuensi.

        c. Tidak cukup aman untuk komunikasi nyata
        Karena kedua kelemahan di atas, Caesar Cipher tidak bisa digunakan untuk pengamanan pesan modern.
        Bahkan seseorang tanpa pengetahuan kriptografi bisa memecahkannya hanya dalam hitungan detik.

    2. Kelemahan Utama Vigenère Cipher
        a. Pola berulang pada kunci
        Jika kunci pendek dan pesan panjang, kunci akan berulang, sehingga pola huruf ciphertext juga berulang.
        Pola berulang ini bisa dianalisis menggunakan metode Kasiski atau Friedman test untuk menebak panjang kunci.

        b. Masih rentan terhadap analisis frekuensi
        Meskipun lebih aman dari Caesar Cipher, Vigenère Cipher masih bisa dipecahkan dengan analisis frekuensi jika panjang kunci berhasil ditebak.
        Setelah panjang kunci diketahui, pesan dapat dibagi menjadi beberapa Caesar Cipher yang lebih kecil — dan setiap bagian bisa dipecahkan dengan cara biasa.

        c. Tidak aman untuk komunikasi digital
        Dengan adanya komputer modern, semua kemungkinan kunci dapat diuji dengan cepat.
        Oleh karena itu, Vigenère Cipher tidak lagi dianggap aman untuk aplikasi kriptografi masa kini.

- Pertanyaan 2: 
    1. Bahasa manusia memiliki pola frekuensi yang khas
    Dalam setiap bahasa, huruf-huruf tidak muncul dengan peluang yang sama.
    Misalnya, dalam bahasa Inggris huruf “E”, “T”, dan “A” muncul jauh lebih sering daripada huruf “Q” atau “Z”.
    Dalam bahasa Indonesia, huruf yang sering muncul adalah “A”, “N”, dan “I”. 

    2. Cipher klasik tidak mengubah frekuensi huruf
    Sebagian besar cipher klasik hanya mengganti atau menukar huruf, tanpa menyamarkan seberapa sering huruf itu muncul.
    Substitution cipher (seperti Caesar Cipher) hanya menggeser huruf; huruf yang sering muncul tetap sering muncul, hanya berubah simbolnya.
    Transposition cipher hanya mengacak urutan huruf, tetapi tetap mempertahankan jumlah kemunculan setiap huruf.
    Akibatnya, meskipun bentuk huruf berubah, pola statistiknya tetap sama.

    3. Analisis frekuensi dapat memetakan ciphertext ke plaintext
    Seorang kriptanalis dapat:
        1. Menghitung frekuensi setiap huruf pada ciphertext.
        2. Membandingkan dengan tabel frekuensi umum dalam bahasa tertentu.
        3. Menebak huruf mana yang mungkin mewakili huruf tertentu dalam plaintext.
    
    4. Tidak ada proses penyamaran statistik (confusion dan diffusion)
    Cipher klasik tidak memiliki sifat confusion dan diffusion seperti pada algoritma modern (misalnya AES).
    Confusion: menyembunyikan hubungan antara kunci dan ciphertext.
    Diffusion: menyebarkan pola dari plaintext ke seluruh ciphertext.
    Karena dua sifat ini tidak ada, cipher klasik menyisakan pola-pola yang bisa dianalisis secara matematis.

- Pertanyaan 3:
    1. Konsep Dasar
        a. Cipher substitusi = Mengganti setiap huruf (atau simbol) pada plaintext dengan huruf lain berdasarkan aturan tertentu.
        b. Cipher Transposisi = Mengubah urutan posisi huruf tanpa mengubah huruf itu sendiri.
    2. Contoh umum
        a. Substitusi: Caesar Cipher, Monoalphabetic Cipher, Vigenère Cipher.
        b. Transposisi: Rail Fence Cipher, Columnar Transposition Cipher.
    3. Proses enkripsi
        a. Substitusi: Setiap huruf pada plaintext digantikan oleh huruf lain sesuai aturan kunci.
        b. Transposisi: Huruf-huruf pada plaintext diatur ulang berdasarkan pola tertentu.
    4. Proses dekripsi
        a. Substitusi: Mengganti kembali huruf-huruf ciphertext ke huruf asli menggunakan aturan kunci.
        b. Transposisi: Mengembalikan urutan huruf ke posisi semula berdasarkan pola yang sama.
    5. Kelebihan utama
        a. Substitusi: - Sederhana dan cepat diimplementasikan.
                       - Beberapa variasi (seperti Vigenère) lebih sulit dipecahkan dibanding transposisi dasar.
        b. Transposisi:- Tidak mengubah frekuensi huruf, tetapi menyulitkan analisis langsung karena susunan huruf acak.
                       - Lebih kuat jika dikombinasikan dengan substitusi.
    6. Kelemahan utama
        a. Substitusi: - Rentan terhadap analisis frekuensi, terutama untuk cipher sederhana seperti Caesar.
                       - Kunci pendek mudah ditebak.
        b. Transposisi:- Masih mempertahankan frekuensi huruf asli, sehingga bisa dianalisis.
                       - Pola tertentu dapat dikenali jika pesan cukup panjang.
    7. Kemudahan Implementasi
        a. Substitusi: Sangat mudah diimplementasikan dengan tabel substitusi sederhana.
        b. Transposisi: Juga mudah diimplementasikan dengan pengaturan ulang indeks karakter.
    8. Kelebihan kombinasi
        a. Menggabungkan kedua metode dapat meningkatkan keamanan.
        b. Misalnya, menerapkan substitusi terlebih dahulu, lalu transposisi, atau sebaliknya.
)
---

## 8. Kesimpulan
Cipher klasik merupakan metode penyandian sederhana yang menjadi dasar perkembangan kriptografi modern, dengan prinsip utama substitusi dan transposisi. Meskipun mudah dipahami dan diimplementasikan, cipher klasik tidak lagi aman karena pola huruf dan frekuensi bahasa masih dapat dianalisis dengan mudah. Namun, konsep dasarnya tetap penting sebagai fondasi bagi algoritma kriptografi modern seperti AES dan RSA.

---
