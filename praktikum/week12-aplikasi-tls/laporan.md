# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: [Aplikasi TLS & E-commerce]  
Nama: [Fiqri Nur Hidayanto]  
NIM: [230202754]  
Kelas: [5IKKA]  

---

## 1. Tujuan
(1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
 2. Menjelaskan enkripsi dalam transaksi e-commerce.
 3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.)

---

## 2. Dasar Teori
1. Transport Layer Security (TLS)
    Transport Layer Security (TLS) adalah protokol keamanan yang digunakan untuk melindungi komunikasi data melalui jaringan komputer, khususnya internet. TLS merupakan pengembangan dari Secure Socket Layer (SSL) dan saat ini menjadi standar utama dalam pengamanan komunikasi web melalui protokol HTTPS.
    TLS bekerja dengan menyediakan mekanisme kriptografi untuk menjamin bahwa data yang dikirim antara klien dan server tidak dapat disadap atau dimodifikasi oleh pihak yang tidak berwenang.
2. Tujuan dan Fungsi TLS
    TLS memiliki tiga tujuan utama:
    1. Kerahasiaan (Confidentiality)
        Data dienkripsi sehingga hanya pihak yang berhak yang dapat membacanya.
    2. Integritas (Integrity)
        Data dilindungi dari perubahan selama transmisi.
    3. Otentikasi (Authentication)
        Identitas server (dan klien, jika diperlukan) dapat diverifikasi melalui sertifikat digital.
3. Cara Kerja TLS Secara Umum
    Proses komunikasi TLS diawali dengan TLS Handshake, yang meliputi:
    1. Klien mengirim permintaan koneksi aman ke server.
    2. Server mengirim sertifikat digital yang dikeluarkan oleh Certificate Authority (CA).
    3. Klien memverifikasi keaslian sertifikat server.
    4. Kedua pihak menyepakati algoritma kriptografi dan kunci sesi.
    5. Komunikasi data berlangsung secara terenkripsi menggunakan kunci sesi simetris.
    TLS mengombinasikan kriptografi kunci publik untuk pertukaran kunci dan kriptografi simetris untuk efisiensi komunikasi.
4. Konsep E-Commerce
    E-Commerce (Electronic Commerce) adalah aktivitas jual beli barang dan jasa yang dilakukan secara elektronik melalui jaringan internet. E-Commerce melibatkan pertukaran data sensitif seperti informasi pribadi, kredensial akun, dan data pembayaran.
    Karena sifatnya yang terbuka dan terhubung ke internet, sistem E-Commerce sangat bergantung pada mekanisme keamanan yang kuat.
5. Peran TLS dalam Aplikasi E-Commerce
    TLS memiliki peran krusial dalam aplikasi E-Commerce, antara lain:
    1. Mengamankan Transaksi Online
        Informasi kartu kredit dan pembayaran terenkripsi selama transmisi.
    2. Mencegah Penyadapan dan Manipulasi Data
        Serangan seperti man-in-the-middle dapat dicegah.
    3. Menjamin Keaslian Situs Web
        Sertifikat TLS memastikan pengguna terhubung ke website yang sah.
    4. Meningkatkan Kepercayaan Pengguna
        Ikon gembok pada browser meningkatkan rasa aman konsumen.
6. Hubungan TLS dengan PKI dan Sertifikat Digital
    TLS bergantung pada Public Key Infrastructure (PKI) untuk proses otentikasi. Sertifikat digital yang digunakan dalam TLS diterbitkan oleh Certificate Authority (CA) yang tepercaya.
    Dengan PKI:
    - Identitas server dapat diverifikasi
    - Public key server dapat dipercaya
    - Komunikasi aman dapat terjamin
7. Risiko Tanpa TLS pada E-Commerce
    Tanpa penerapan TLS:
    - Data transaksi dapat disadap
    - Informasi pelanggan dapat dicuri
    - Risiko penipuan meningkat
    - Kepercayaan pengguna terhadap platform menurun
    Oleh karena itu, TLS menjadi komponen wajib dalam sistem E-Commerce modern.
8. Kesimpulan Dasar Teori
    Transport Layer Security (TLS) merupakan protokol keamanan yang menyediakan kerahasiaan, integritas, dan otentikasi dalam komunikasi data. Dalam aplikasi E-Commerce, TLS berperan penting dalam mengamankan transaksi online, melindungi data pelanggan, serta membangun kepercayaan pengguna. Kombinasi TLS, PKI, dan sertifikat digital menjadikan E-Commerce aman dan andal untuk digunakan.

---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan () )

---

## 4. Langkah Percobaan

Langkah 1 — Analisis SSL/TLS pada Email & Web
- Gunakan browser (Chrome/Firefox) untuk mengecek sertifikat digital pada website e-commerce (contoh: Tokopedia, Shopee, Bukalapak).
- Catat informasi berikut:
    - Issuer CA (Certificate Authority).
    - Masa berlaku sertifikat.
    - Algoritma enkripsi yang digunakan (RSA, AES, dll).
- Bandingkan perbedaan antara website dengan HTTPS dan tanpa HTTPS.

Langkah 2 — Studi Kasus E-commerce
- Analisis bagaimana enkripsi digunakan untuk melindungi transaksi online (misalnya saat login atau melakukan pembayaran).
- Diskusikan potensi ancaman jika TLS tidak digunakan (contoh: serangan Man-in-the-Middle).

Langkah 3 — Analisis Etika & Privasi
- Identifikasi isu privasi dalam penggunaan email terenkripsi (PGP, S/MIME).
- Diskusikan dilema etika:
    - Apakah perusahaan boleh melakukan dekripsi email karyawan untuk audit?
    - Bagaimana kebijakan pemerintah dalam pengawasan komunikasi terenkripsi?

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
- Pertanyaan 1: Apa perbedaan utama antara HTTP dan HTTPS?
    HTTPS menggunakan TLS/SSL untuk mengenkripsi data yang dikirim antara klien dan server, sedangkan HTTP tidak mengenkripsi data tersebut. Hal ini membuat HTTPS lebih aman karena melindungi informasi sensitif dari penyadapan dan manipulasi selama transmisi.
- Pertanyaan 2: Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?
    Sertifikat digital penting dalam komunikasi TLS karena sertifikat ini berfungsi untuk mengotentikasi identitas server (dan klien jika diperlukan). Dengan sertifikat digital yang dikeluarkan oleh Certificate Authority (CA) yang tepercaya, klien dapat memastikan bahwa mereka berkomunikasi dengan server yang sah dan bukan pihak yang mencoba
- Pertanyaan 3: Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?
    Kriptografi mendukung privasi dalam komunikasi digital dengan mengenkripsi data sehingga hanya pihak yang berwenang yang dapat mengakses informasi tersebut
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
