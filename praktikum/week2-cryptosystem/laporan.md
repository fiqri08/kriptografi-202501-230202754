# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: Cryptosystem (Komponen, Enkripsi & Dekripsi, Simetris & Asimetris)
Nama: Fiqri Nur Hidayanto 
NIM: 230202754  
Kelas: 5IKKA  

---

## 1. Tujuan

    1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).
    2. Menggambarkan proses enkripsi dan dekripsi sederhana.
    3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris).

---

## 2. Dasar Teori
1. Pengertian Cryptosystem
    Cryptosystem (sistem kriptografi) adalah kerangka kerja atau sistem matematis yang digunakan untuk mengamankan komunikasi dengan cara mengubah pesan asli (plaintext) menjadi bentuk yang tidak dapat dibaca (ciphertext), lalu mengembalikannya lagi ke bentuk semula oleh pihak yang berhak.
    Tujuan utamanya adalah menjaga kerahasiaan, integritas, autentikasi, dan non-repudiation dalam komunikasi digital.

2. Komponen Utama Cryptosystem

Sebuah cryptosystem umumnya terdiri dari lima komponen dasar:

1. Plaintext (Teks Asli):
    Pesan atau data yang ingin dilindungi.
    Contoh: “Halo Dunia”

2. Encryption Algorithm (Algoritma Enkripsi):
    Prosedur atau aturan matematis untuk mengubah plaintext menjadi ciphertext.
    Contoh: algoritma AES, RSA.

3. Ciphertext (Teks Terenkripsi):
    Hasil dari proses enkripsi yang tidak dapat dibaca oleh orang lain.
    Contoh: “0x9fa23bd7...”

4. Decryption Algorithm (Algoritma Dekripsi):
    Prosedur untuk mengubah ciphertext kembali menjadi plaintext menggunakan kunci tertentu.

5. Key (Kunci):
    Nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi. Kunci inilah yang menentukan siapa yang bisa membaca pesan.

3. Proses Enkripsi dan Dekripsi
    Enkripsi: Mengubah teks asli menjadi kode rahasia menggunakan algoritma dan kunci.
    Dekripsi: Mengembalikan kode rahasia menjadi teks asli menggunakan kunci (yang sama atau berbeda, tergantung sistemnya).

4. Jenis Cryptosystem
    Terdapat dua jenis utama cryptosystem berdasarkan cara penggunaan kuncinya:
        a. Symmetric Key Cryptosystem (Kriptografi Simetris)
            Menggunakan satu kunci yang sama untuk enkripsi dan dekripsi.
            Kunci harus dijaga agar tidak bocor, karena siapa pun yang tahu kunci bisa membaca pesan.
            Contoh algoritma: AES, DES, Blowfish.
            Kelebihan: Cepat dan efisien untuk data besar.
            Kelemahan: Distribusi kunci sulit — harus dibagikan secara aman.
            Contoh:
            Kamu dan temanmu memiliki kunci “1234”. Kamu enkripsi pesan dengan kunci itu, dan temanmu gunakan kunci yang sama untuk membuka pesannya.
        b. Asymmetric Key Cryptosystem (Kriptografi Asimetris)
            Menggunakan dua kunci berbeda tapi saling terkait, yaitu:
            Public key (kunci publik) → boleh dibagikan ke siapa pun.
            Private key (kunci privat) → hanya pemilik yang tahu.
            Data yang dienkripsi dengan public key hanya bisa dibuka dengan private key, dan sebaliknya.
            Contoh algoritma: RSA, ECC, ElGamal.
            Kelebihan: Aman untuk pertukaran kunci dan tanda tangan digital.
            Kelemahan: Lebih lambat dibanding simetris.
            Contoh:
            Kamu kirim pesan ke seseorang menggunakan kunci publik miliknya. Hanya dia yang bisa membuka pesan itu menggunakan kunci privat-nya.
---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

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
- Pertanyaan 1: …  
- Pertanyaan 2: …  
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
