# Laporan Praktikum Kriptografi
Minggu ke-: 14  
Topik: [Analisis Serangan Kriptografi]  
Nama: [Fiqri Nur Hidayanto]  
NIM: [230202754]  
Kelas: [5IKKA]  

---

## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
1. Pengertian Kriptografi
    Kriptografi adalah ilmu yang mempelajari teknik pengamanan informasi melalui proses penyandian (enkripsi) dan penguraian (dekripsi) agar data hanya dapat diakses oleh pihak yang berwenang. Tujuan utama kriptografi meliputi kerahasiaan (confidentiality), integritas (integrity), otentikasi (authentication), dan non-repudiation.
    Analisis serangan kriptografi merupakan studi mengenai berbagai metode yang digunakan untuk menyerang, melemahkan, atau memecahkan sistem kriptografi, baik dengan mengeksploitasi kelemahan algoritma, implementasi, maupun manajemen kunci.
2. Tujuan Analisis Serangan Kriptografi
    Analisis serangan kriptografi bertujuan untuk:
    1. Mengidentifikasi kelemahan algoritma kriptografi.
    2. Menguji ketahanan sistem terhadap serangan nyata.
    3. Menentukan tingkat keamanan suatu sistem kriptografi.
    4. Memberikan rekomendasi perbaikan untuk meningkatkan keamanan.
3. Model Serangan dalam Kriptografi
    Beberapa model serangan yang umum digunakan dalam analisis kriptografi antara lain:
    a. Ciphertext-Only Attack (COA)
        Penyerang hanya memiliki akses ke ciphertext tanpa mengetahui plaintext atau kunci. Serangan ini mengandalkan analisis statistik atau pola pada ciphertext.
    b. Known-Plaintext Attack (KPA)
        Penyerang memiliki beberapa pasangan plaintext dan ciphertext. Informasi ini digunakan untuk menebak kunci atau memecahkan sistem enkripsi.
    c. Chosen-Plaintext Attack (CPA)
        Penyerang dapat memilih plaintext tertentu dan memperoleh ciphertext hasil enkripsi. Model ini umum digunakan untuk menguji algoritma kriptografi modern.
    d. Chosen-Ciphertext Attack (CCA)
        Penyerang dapat memilih ciphertext dan mendapatkan hasil dekripsinya. Serangan ini sangat berbahaya dan sering digunakan untuk mengevaluasi keamanan sistem kriptografi kunci publik.
4. Jenis-Jenis Serangan Kriptografi
    a. Brute Force Attack
        Serangan dengan mencoba seluruh kemungkinan kunci hingga ditemukan kunci yang benar. Ketahanan terhadap brute force bergantung pada panjang kunci dan kompleksitas algoritma.
    b. Cryptanalysis Attack
        Serangan yang memanfaatkan kelemahan matematis atau struktur algoritma kriptografi, seperti serangan diferensial dan linear pada algoritma simetris.
    c. Side-Channel Attack
        Serangan yang memanfaatkan informasi dari implementasi fisik, seperti waktu eksekusi, konsumsi daya, atau radiasi elektromagnetik.
    d. Man-in-the-Middle Attack (MITM)
        Penyerang berada di antara dua pihak yang berkomunikasi dan dapat memodifikasi atau menyadap pesan tanpa disadari oleh kedua pihak.
    e. Replay Attack
        Penyerang merekam komunikasi yang sah lalu mengirimkannya kembali untuk mendapatkan akses ilegal.
5. Analisis Serangan pada Sistem Kriptografi Modern
    Pada sistem modern seperti TLS, PKI, Blockchain, dan E-commerce, analisis serangan tidak hanya difokuskan pada algoritma kriptografi, tetapi juga pada:
    - Manajemen kunci
    - Protokol komunikasi
    - Implementasi perangkat lunak
    - Keamanan infrastruktur pendukung
    Contohnya, pada TLS, kelemahan dapat muncul akibat sertifikat palsu, konfigurasi protokol yang salah, atau penggunaan algoritma kriptografi yang sudah usang.
6. Pentingnya Analisis Serangan Kriptografi
    Analisis serangan kriptografi sangat penting karena:
    1. Membantu meningkatkan keamanan sistem informasi.
    2. Mencegah kebocoran data dan penyalahgunaan informasi.
    3. Menjadi dasar pengembangan algoritma kriptografi yang lebih kuat.
    4. Mendukung penerapan keamanan pada sistem kritis seperti perbankan, e-commerce, dan pemerintahan.
7. Kesimpulan
    Analisis serangan kriptografi merupakan bagian penting dalam evaluasi keamanan sistem informasi. Dengan memahami berbagai model dan jenis serangan, pengembang dapat merancang sistem kriptografi yang lebih aman dan andal. Pendekatan ini memastikan bahwa sistem tidak hanya aman secara teori, tetapi juga tahan terhadap serangan di dunia nyata.

---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

Langkah 1 — Identifikasi Serangan
    - Pilih salah satu kasus nyata serangan kriptografi (contoh: serangan brute force pada hash MD5, kebocoran SSL/TLS, serangan dictionary password).
    - Identifikasi vektor serangan dan penyebab kelemahan.

Langkah 2 — Evaluasi Kelemahan
    - Analisis kelemahan algoritma yang digunakan.
    - Apakah kelemahan ada pada algoritma kriptografi, implementasi, atau konfigurasi sistem?

Langkah 3 — Rekomendasi Solusi
    - Usulkan algoritma atau mekanisme yang lebih aman.
        Contoh: mengganti MD5 → SHA-256, RSA lama → ECC, password plaintext → bcrypt/scrypt/Argon2.
    - Jelaskan alasan pemilihan algoritma dan dampaknya terhadap keamanan sistem.


---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

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
- Pertanyaan 1: Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
    Banyak sistem lama masih rentan terhadap brute force atau dictionary attack karena penggunaan algoritma kriptografi yang sudah usang dan lemah, seperti MD5 atau SHA-1, yang memiliki ruang kunci terbatas dan mudah diprediksi. Selain itu, praktik manajemen kunci yang buruk, seperti penggunaan password sederhana atau tidak adanya mekanisme pembatasan percobaan login, juga meningkatkan risiko serangan tersebut. Kurangnya pembaruan keamanan dan kesadaran pengguna terhadap pentingnya keamanan siber turut berkontribusi pada kerentanan ini.
- Pertanyaan 2: Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
    Kelemahan algoritma merujuk pada cacat atau kelemahan yang melekat dalam desain matematis suatu algoritma kriptografi itu sendiri, yang dapat dieksploitasi untuk memecahkan enkripsi atau mengungkapkan informasi rahasia. Contohnya adalah serangan diferensial pada algoritma block cipher tertentu. Sementara itu, kelemahan implementasi berkaitan dengan kesalahan atau kekurangan dalam cara algoritma tersebut diimplementasikan dalam perangkat lunak atau perangkat keras, seperti bug pemrograman, penggunaan kunci yang lemah, atau konfigurasi yang salah, yang dapat membuka celah keamanan meskipun algoritma itu sendiri aman. 
- Pertanyaan 3: Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?
    Organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan dengan mengadopsi beberapa praktik terbaik, antara lain: secara rutin memperbarui dan meninjau algoritma kriptografi yang digunakan untuk memastikan mereka masih dianggap aman oleh komunitas keamanan; menerapkan manajemen kunci yang kuat, termasuk penggunaan kunci yang panjang dan kompleks serta rotasi kunci secara berkala; melakukan audit keamanan dan pengujian penetrasi secara berkala untuk mengidentifikasi dan memperbaiki potensi kerentanan; serta meningkatkan kesadaran dan pelatihan keamanan siber bagi staf untuk mengurangi risiko kesalahan manusia. Selain itu, mengikuti standar industri dan pedoman keamanan yang diakui juga penting untuk menjaga keamanan sistem kriptografi.
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
