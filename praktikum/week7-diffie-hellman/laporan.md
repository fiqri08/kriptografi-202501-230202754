# Laporan Praktikum Kriptografi
Minggu ke-: 7 
Topik: Diffie–Hellman  
Nama: Fiqri Nur Hidayanto  
NIM: 230202754  
Kelas: 5IKKA  

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
1. Pengertian
    Diffie–Hellman Key Exchange adalah salah satu algoritma kriptografi kunci publik yang digunakan untuk melakukan pertukaran kunci rahasia secara aman melalui jaringan yang tidak aman.
    Algoritma ini diperkenalkan pertama kali oleh Whitfield Diffie dan Martin Hellman pada tahun 1976, dan menjadi dasar bagi banyak sistem keamanan modern seperti TLS/SSL, VPN, dan berbagai protokol enkripsi lainnya.
    Tujuan utama dari algoritma ini adalah memungkinkan dua pihak (biasanya disebut Alice dan Bob) untuk menyepakati sebuah kunci rahasia bersama tanpa harus mengirimkan kunci tersebut secara langsung melalui jaringan.

2. Konsep Dasar

Diffie–Hellman bekerja berdasarkan operasi eksponensial modular dalam teori bilangan.
Konsepnya memanfaatkan sifat matematis fungsi eksponensial yang mudah dihitung satu arah, tetapi sangat sulit dibalik tanpa informasi tertentu (masalah Discrete Logarithm Problem).



---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
Langkah 1 - Simulasi diffie-hellman
Ekspektasi hasil: nilai shared_secret_A dan shared_secret_B harus sama.
Langkah 2 — Analisis Serangan MITM (Man-in-the-Middle)
Tambahkan simulasi sederhana:
- Pihak ketiga (Eve) mencegat dan mengganti public key.
- Alice dan Bob berakhir memiliki kunci berbeda, tetapi Eve mengetahui keduanya.

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
- Pertanyaan 1: 
1. Karena Hanya Nilai Publik yang Dikirim
Dalam algoritma Diffie–Hellman, kedua pihak (misalnya Alice dan Bob) tidak pernah mengirimkan kunci rahasia (private key) mereka melalui jaringan. 

2. Keamanan Berdasarkan Masalah Logaritma Diskrit
Untuk pihak luar (penyadap/Eve), walaupun ia tahu:
ia tetap tidak dapat menghitung kunci rahasia bersama K tanpa mengetahui nilai a atau b, karena ia harus memecahkan Discrete Logarithm Problem (DLP)

3. Fungsi Eksponensial Modular Bersifat “One-Way”
modp mudah dilakukan,tapi proses kebalikannya (mencari a dari hasilnya) sangat sulit.

4. Kunci Rahasia Dihasilkan Secara Terpisah tapi Sama
Alice dan Bob masing-masing menghitung kunci rahasia

5. Pihak Ketiga Tidak Dapat Meniru Tanpa Kunci Privat

- Pertanyaan 2: 
1. Tidak Ada Mekanisme Autentikasi (Tanpa Verifikasi Identitas)
2. Tidak Menyediakan Integritas atau Enkripsi Data
3. Bergantung pada Parameter Umum (p dan g) yang Aman
4. Tidak Melindungi dari Serangan Rekaman (Replay Attack)

-pertanyaan 3:
1. Gunakan Autentikasi Digital
2. Gunakan Varian yang Lebih Aman
3. Validasi Parameter Publik

)
---

## 8. Kesimpulan
Diffie–Hellman merupakan protokol kriptografi kunci publik yang memungkinkan dua pihak membentuk kunci rahasia bersama melalui saluran komunikasi publik secara aman, tanpa perlu mengirimkan kunci itu langsung. Keamanannya bergantung pada sulitnya memecahkan Discrete Logarithm Problem. Namun, versi murninya tidak menyediakan autentikasi sehingga perlu dikombinasikan dengan mekanisme verifikasi identitas untuk mencegah serangan Man-in-the-Middle.


---
