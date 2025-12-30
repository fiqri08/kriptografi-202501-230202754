# Laporan Praktikum Kriptografi
Minggu ke-: 1  
Topik: Sejarah kriptografi dan prinsip CIA  
Nama: Fiqri Nur Hidayanto  
NIM: 230202754  
Kelas: 5IKKA  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:  
1. Menjelaskan **sejarah dan evolusi kriptografi** dari masa klasik hingga modern.  
2. Menyebutkan **prinsip Confidentiality, Integrity, Availability (CIA)** dengan benar.  
3. Menyimpulkan **peran kriptografi** dalam sistem keamanan informasi modern.  
4. Menyiapkan repositori GitHub sebagai media kerja praktikum.  

---

## 2. Dasar Teori
(Ringkas teori relevan (cukup 2–3 paragraf).  
Contoh: definisi cipher klasik, konsep modular aritmetika, dll.  )

---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

Langkah 1 — Ringkasan Sejarah Kriptografi

Kriptografi merupakan ilmu dan seni menyembunyikan pesan agar hanya pihak yang berwenang yang dapat membacanya. Perkembangan kriptografi dapat ditelusuri dalam tiga era utama: klasik, modern, dan kontemporer.
Pada era kriptografi klasik, metode enkripsi masih bersifat sederhana dan berbasis pada manipulasi huruf. Contoh paling terkenal adalah Caesar Cipher yang digunakan oleh Julius Caesar, yaitu teknik pergeseran huruf dalam alfabet dengan jumlah langkah tertentu. Meski mudah dipahami, metode ini cepat terpecahkan dengan teknik analisis frekuensi. Untuk meningkatkan keamanan, kemudian muncul Vigenère Cipher yang menggunakan kunci berbentuk kata atau frasa, menghasilkan pola substitusi yang lebih kompleks. Namun, dengan perkembangan ilmu matematika, cipher klasik tetap dapat dibobol.
Memasuki era kriptografi modern, kebutuhan komunikasi yang aman semakin meningkat, terutama pada abad ke-20 saat perang dunia dan munculnya komputer digital. Algoritma modern memanfaatkan teori matematika dan komputasi. Salah satu pencapaian besar adalah RSA (Rivest–Shamir–Adleman), algoritma kunci publik yang bergantung pada sulitnya memfaktorkan bilangan prima besar. Selain itu, AES (Advanced Encryption Standard) menjadi standar global untuk enkripsi simetris karena efisiensi dan tingkat keamanannya yang tinggi. Kriptografi modern memungkinkan komunikasi terenkripsi dalam skala global, seperti pada HTTPS dan aplikasi pesan instan.
Selanjutnya, perkembangan teknologi membawa kriptografi ke arah era kontemporer. Kriptografi kini tidak hanya berfokus pada kerahasiaan, tetapi juga integritas, autentikasi, dan non-repudiation. Teknologi hash function dan tanda tangan digital memungkinkan verifikasi data yang aman. Inovasi terbaru muncul dalam blockchain dan cryptocurrency (misalnya Bitcoin), yang menggunakan prinsip kriptografi hash, kunci publik, serta konsensus terdistribusi untuk menciptakan sistem finansial tanpa otoritas pusat.
Dengan demikian, kriptografi telah berevolusi dari sekadar seni menyamarkan pesan menjadi pilar utama keamanan informasi modern. Dari sandi sederhana hingga algoritma kompleks yang menopang internet dan transaksi digital, sejarah kriptografi menunjukkan perannya yang semakin vital dalam dunia yang terhubung secara global.

Langkah 2 — Prinsip CIA

1. Confidentiality (Kerahasiaan)
Confidentiality berarti memastikan bahwa data hanya bisa diakses oleh pihak yang berwenang. Tujuannya adalah melindungi informasi sensitif agar tidak bocor ke pihak yang salah.
Contoh nyata: Enkripsi end-to-end pada WhatsApp. Pesan yang dikirim hanya dapat dibaca oleh pengirim dan penerima, bahkan pihak WhatsApp sendiri tidak bisa membacanya.

2. Integrity (Integritas)
Integrity memastikan bahwa data tetap utuh, konsisten, dan tidak mengalami perubahan tanpa izin. Jika ada modifikasi, maka harus bisa terdeteksi.
Contoh nyata: Digital signature pada dokumen PDF. Tanda tangan digital menjamin isi dokumen tidak diubah setelah ditandatangani. Jika ada perubahan sekecil apapun, tanda tangan digital akan dianggap tidak valid.

3. Availability (Ketersediaan)
Availability berarti menjamin bahwa sistem, data, dan layanan selalu dapat diakses saat dibutuhkan oleh pengguna yang berhak. Gangguan pada aspek ini bisa menyebabkan kerugian besar.
Contoh nyata: Sistem perbankan online yang harus tetap tersedia 24/7. Untuk mencegah downtime, bank menggunakan server redundancy dan backup system agar layanan tetap berjalan meskipun ada kerusakan pada salah satu server.

Langkah 4 — Quiz Singkat

Jawab pertanyaan berikut di laporan:

    1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
        Claude Elwood Shannon (1916–2001) adalah ilmuwan Amerika yang dikenal sebagai “Bapak Teori Informasi”. Pada tahun 1949, ia menulis makalah berjudul “Communication Theory of Secrecy Systems”, yang menjadi dasar teori kriptografi modern.
    2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
        Beberapa algoritma kunci publik (public key algorithms) yang populer dan banyak digunakan saat ini antara lain:
        1.	RSA (Rivest–Shamir–Adleman)
            Merupakan algoritma kunci publik paling klasik dan luas digunakan.
            Keamanannya didasarkan pada sulitnya memfaktorkan bilangan prima besar.
            Umumnya dipakai dalam SSL/TLS, tanda tangan digital, dan enkripsi email.
        2.	ECC (Elliptic Curve Cryptography)
            Menggunakan konsep matematika kurva eliptik.
            Memberikan tingkat keamanan tinggi dengan ukuran kunci yang lebih kecil dibanding RSA.
            Digunakan pada sistem modern seperti WhatsApp, Signal, dan protokol keamanan internet (TLS).
        3.	DSA (Digital Signature Algorithm)
            Fokus pada pembuatan dan verifikasi tanda tangan digital, bukan enkripsi data.
            Banyak digunakan dalam standar keamanan seperti e-government dan dokumen resmi.
        4.	Diffie–Hellman Key Exchange
            Bukan untuk enkripsi langsung, tetapi untuk pertukaran kunci rahasia secara aman di jaringan publik.
            Sering digunakan bersama algoritma lain sebagai bagian dari protokol keamanan (misalnya pada HTTPS).
        5.	ElGamal
            Berdasarkan prinsip yang mirip dengan Diffie–Hellman.
            Digunakan untuk enkripsi dan tanda tangan digital di beberapa sistem keamanan.

    3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
        1. Dasar Keamanan
            Kriptografi Klasik:
            Berdasarkan pada kerahasiaan algoritma. Jika algoritmanya diketahui, pesan bisa mudah dibobol.
            Contoh: Caesar Cipher, Vigenère Cipher.
            Kriptografi Modern:
            Berdasarkan pada kerahasiaan kunci (key), bukan algoritma. Algoritmanya bisa diketahui publik, tetapi tanpa kunci, pesan tetap aman.
            Contoh: RSA, AES.
        2. Teknik Enkripsi
            Klasik: Menggunakan manipulasi huruf atau simbol, seperti substitusi (penggantian huruf) atau transposisi (penyusunan ulang huruf).
            Modern: Menggunakan rumus matematika dan operasi logika kompleks, melibatkan bilangan biner, fungsi hash, serta teori bilangan prima.
        3. Media Penggunaan
            Klasik: Dikerjakan secara manual atau dengan alat mekanis sederhana (misalnya mesin Enigma).
            Modern: Dilakukan oleh komputer atau perangkat digital dengan algoritma yang sangat cepat dan kompleks.
        4. Jenis Kunci
            Klasik: Biasanya hanya menggunakan satu kunci (simetris) untuk enkripsi dan dekripsi.
            Modern: Bisa menggunakan dua kunci (asimetris) — kunci publik dan kunci privat, seperti pada RSA.
        5. Tingkat Keamanan
            Klasik: Mudah dipecahkan dengan analisis frekuensi dan percobaan manual.
            Modern: Sangat kuat karena bergantung pada persoalan matematika yang sulit diselesaikan (misalnya faktorisasi bilangan besar).

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit 52a16d6
Author: Fiqri NH <fiqrinur0801@gmail.com>
Date:   2025-10-7

    week1-intro: Ringakasan sejarah kriptografi dan prinsip CIA)
```
