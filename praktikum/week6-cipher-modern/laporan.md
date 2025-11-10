# Laporan Praktikum Kriptografi
Minggu ke-: 6  
Topik: Cipher Modern  
Nama: Fiqri Nur Hidayanto  
NIM: 230202754  
Kelas: 5IKKA  

---

## 1. Tujuan
1. Mengimplementasikan algoritma DES untuk blok data sederhana.
2. Menerapkan algoritma AES dengan panjang kunci 128 bit.
3. Menjelaskan proses pembangkitan kunci publik dan privat pada algoritma RSA.

---

## 2. Dasar Teori
1. Pengertian Cipher Modern
    Cipher modern adalah metode penyandian (enkripsi) yang dikembangkan untuk mengamankan data digital menggunakan prinsip matematika dan komputasi yang kompleks. Tidak seperti cipher klasik yang hanya memanipulasi huruf atau posisi karakter, cipher modern bekerja pada bit atau blok data dan menggunakan algoritma serta kunci kriptografi panjang untuk mencapai tingkat keamanan tinggi.
    Cipher modern digunakan dalam berbagai aplikasi, seperti komunikasi internet (HTTPS), sistem perbankan, jaringan komputer, hingga keamanan data perangkat mobile.
2. Karakteristik Cipher Modern
    Cipher modern memiliki beberapa ciri utama:
    1. Berbasis matematika kompleks – menggunakan operasi logika, permutasi, dan fungsi non-linear.
    2. Menggunakan kunci panjang – kunci bisa mencapai ratusan bit sehingga tidak dapat dipecahkan dengan brute force.
    3. Memiliki sifat Confusion dan Diffusion
        a. Confusion: hubungan antara kunci dan ciphertext dibuat sekompleks mungkin agar sulit ditebak.
        b. Diffusion: perubahan kecil pada plaintext menghasilkan perubahan besar pada ciphertext.
    4. Diproses secara digital – bekerja pada bit, byte, atau blok data, bukan huruf alfabet.
    5. Dapat diuji secara ilmiah – keamanan diukur berdasarkan teori matematika dan probabilitas, bukan kerahasiaan metode.
3. Jenis Cipher Modern
    Cipher modern umumnya dibagi menjadi dua kelompok utama:
    a. Symmetric Key Cipher (Kriptografi Simetris)
    Menggunakan kunci yang sama untuk enkripsi dan dekripsi.
    Prosesnya cepat dan cocok untuk data dalam jumlah besar.
    Contoh algoritma:
        - DES (Data Encryption Standard)
        - AES (Advanced Encryption Standard)
        - Blowfish
        - RC4
    b. Asymmetric Key Cipher (Kriptografi Asimetris)
    Menggunakan dua kunci berbeda: kunci publik (public key) untuk enkripsi dan kunci privat (private key) untuk dekripsi.
    Lebih aman untuk pertukaran data rahasia, namun prosesnya lebih lambat.
    Contoh algoritma:
        - RSA (Rivest–Shamir–Adleman)
        - ECC (Elliptic Curve Cryptography)
        - Diffie–Hellman Key Exchange
4. Kelebihan Cipher Modern
    Keamanan tinggi terhadap brute force dan analisis statistik.
    Dapat diimplementasikan secara digital untuk berbagai sistem komunikasi.
    Mendukung autentikasi, integritas, dan kerahasiaan data
5. Kelemahan Cipher Modern
    Kompleksitas tinggi, membutuhkan kemampuan komputasi besar.
    Manajemen kunci sulit, terutama pada sistem asimetris.
    Jika implementasi atau pengelolaan kunci salah, keamanan tetap bisa bocor.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
langkah 1 — Implementasi DES
langkah 2 — Implementasi AES
langkah 3 — Implementasi RSA

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
    Perbedaan mendasar antara DES, AES, dan RSA dalam hal kunci dan keamanan
    1. Jenis algoritma
        - DES (Data Encryption Standard) = Symmetric key (kunci simetris)
        - AES (Advanced Encryption Standard) = Symmetric key (kunci simetris)
        - RSA (Rivest–Shamir–Adleman) = Asymmetric key (kunci asimetris)
    2. Sistem kunci
        - DES (Data Encryption Standard) = Menggunakan kunci tunggal untuk enkripsi dan dekripsi
        - AES (Advanced Encryption Standard) = Menggunakan kunci tunggal untuk enkripsi dan dekripsi
        - RSA (Rivest–Shamir–Adleman) = Menggunakan pasangan kunci publik dan privat
    3. Panjang kunci
        - DES (Data Encryption Standard) = 56 bit(dari 64 bit total, 8 bit digunakan untuk parity).
        - AES (Advanced Encryption Standard) = 128, 192, atau 256 bit
        - RSA (Rivest–Shamir–Adleman) = Umumnya 1024-4096 bit atau lebih
    4. Blok Data
        - DES (Data Encryption Standard) = Memproses data dalam blok 64 bit
        - AES (Advanced Encryption Standard) = Memproses data dalam blok 128 bit
        - RSA (Rivest–Shamir–Adleman) = Tidak memproses data dalam blok tetap, melainkan mengenkripsi data yang lebih kecil dari panjang kunci
    5. Keamanan
        - DES (Data Encryption Standard) = Rentan terhadap serangan brute force karena panjang kunci yang pendek
        - AES (Advanced Encryption Standard) = Sangat aman dan tahan terhadap berbagai jenis serangan kriptografi
        - RSA (Rivest–Shamir–Adleman) = Keamanan didasarkan pada kesulitan faktorisasi bilangan besar, namun lebih lambat dibandingkan algoritma simetris
    6. Kecepatan Proses
        - DES (Data Encryption Standard) = Cepat dalam enkripsi dan dekripsi karena menggunakan kunci simetris, tapi cepat usang
        - AES (Advanced Encryption Standard) = Cepat dalam enkripsi dan dekripsi, lebih efisien dibandingkan DES
        - RSA (Rivest–Shamir–Adleman) = Lebih lambat dibandingkan algoritma simetris karena menggunakan operasi matematika yang kompleks
    7. Contoh Penggunaan Umumnya
        - DES (Data Encryption Standard) = Digunakan pada aplikasi lama, sekarang jarang digunakan karena keamanannya yang lemah
        - AES (Advanced Encryption Standard) = Digunakan secara luas dalam berbagai aplikasi modern, termasuk komunikasi aman dan penyimpanan data
        - RSA (Rivest–Shamir–Adleman) = Digunakan untuk pertukaran kunci aman, tanda tangan digital, dan enkripsi data dalam komunikasi internet
    8. Dasar matematis
        - DES (Data Encryption Standard) = Berdasarkan pada struktur Feistel dan operasi bitwise
        - AES (Advanced Encryption Standard) = Berdasarkan pada transformasi matriks dan operasi aljabar pada bidang Galois
        - RSA (Rivest–Shamir–Adleman) = Berdasarkan pada teori bilangan, khususnya faktorisasi bilangan prima besar

- Pertanyaan 2:
    Mengapa AES Lebih Banyak Digunakan Dibanding DES di Era Modern
    1. AES Memiliki Panjang Kunci yang Lebih Kuat
    DES hanya menggunakan 56-bit key, yang kini terlalu pendek untuk menghadapi kekuatan komputasi modern.
    AES mendukung 128, 192, dan 256-bit key, yang membuatnya jutaan kali lebih sulit dipecahkan dengan brute force.
    Contohnya, DES bisa ditembus dalam hitungan jam atau menit dengan komputer modern, sementara AES-256 butuh waktu ribuan tahun bahkan dengan superkomputer.

    2. AES Dirancang Lebih Aman secara Matematis
    DES memiliki kelemahan pada struktur internal Feistel dan S-box yang bisa dianalisis dengan teknik differential atau linear cryptanalysis.
    AES menggunakan struktur Substitution–Permutation Network (SPN) dengan operasi non-linear dan difusi kuat, sehingga lebih tahan terhadap analisis kriptografi.

    3. AES Lebih Efisien di Perangkat Modern
    AES dioptimalkan untuk komputasi 32-bit dan 64-bit, serta memiliki dukungan hardware acceleration (seperti AES-NI di prosesor Intel dan AMD).
    Hasilnya: AES lebih cepat dan hemat energi dibanding DES, terutama untuk data besar.

    4. DES Sudah Resmi Digantikan
    Pada tahun 2001, NIST (National Institute of Standards and Technology) menetapkan AES sebagai standar enkripsi nasional menggantikan DES.
    DES bahkan tidak direkomendasikan lagi untuk digunakan karena tingkat keamanannya rendah.

    5. AES Dapat Digunakan di Berbagai Aplikasi Modern
    AES menjadi standar di berbagai protokol keamanan, seperti:
        - HTTPS / TLS (internet secure connection)
        - Wi-Fi (WPA2, WPA3)
        - VPN dan enkripsi file (BitLocker, VeraCrypt, dsb.)
        - Kecepatan dan keamanannya membuat AES cocok untuk perangkat mobile, cloud, maupun sistem embedded.
- Pertanyaan 3:
Mengapa RSA Dikatakan Sebagai Algoritma Asimetris
    RSA disebut algoritma asimetris (asymmetric key algorithm) karena Ia menggunakan dua kunci berbeda:
        1. Kunci publik (public key) → digunakan untuk enkripsi data (dapat diketahui semua orang).
        2. Kunci privat (private key) → digunakan untuk dekripsi data (hanya dimiliki oleh pemilik sah).
    Kedua kunci ini berpasangan secara matematis, namun tidak dapat dihitung satu sama lain dengan mudah, bahkan dengan mengetahui kunci publik.
Proses Pembangkitan Kunci RSA (Key Generation)
    RSA didasarkan pada teori bilangan prima dan kesulitan memfaktorkan bilangan besar.
)
---

## 8. Kesimpulan
Cipher modern menggunakan algoritma matematis yang kompleks untuk menjamin kerahasiaan, integritas, dan autentikasi data. Contohnya seperti AES (simetris) dan RSA (asimetris) yang jauh lebih aman dibanding cipher klasik karena sulit dipecahkan dengan serangan brute force. Teknologi ini menjadi dasar utama dalam keamanan komunikasi digital masa kini.

---
