# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force) 
Nama: Fiqri Nur Hidayanto  
NIM: 230202754
Kelas: 5IKKA  

---

## 1. Tujuan
    1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
    2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
    3. Menghitung unicity distance untuk ciphertext tertentu.
    4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
    5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

## 2. Dasar Teori
1. Entropy (Entropi Kunci)
Entropy dalam kriptografi merupakan ukuran tingkat ketidakpastian atau kerandoman dari suatu kunci. Semakin tinggi entropi suatu kunci, semakin sulit kunci tersebut ditebak atau diprediksi.
1.1 Definisi
Secara matematis, entropi biasanya dinyatakan dalam bit dan dihitung menggunakan rumus:
H=〖log⁡〗_2 (N)

di mana:
	H = nilai entropi (bit)
	N = jumlah kemungkinan kombinasi kunci
1.2 Makna Entropi
	Entropi tinggi ⇒ kunci sulit ditebak & kuat terhadap brute force.
	Entropi rendah ⇒ kunci mudah diprediksi & rentan dibobol.
1.3 Contoh
Jika sebuah password menggunakan 26 huruf kecil, dan panjangnya 5 karakter:
N=26^5=11,881,376
H=〖log⁡〗_2 (11,881,376)≈23.5" bit" 

Artinya, entropi password tersebut hanya 23,5 bit, termasuk lemah untuk standar keamanan modern.

2. Brute Force Attack
Brute force adalah metode pemecahan kunci dengan mencoba semua kemungkinan kombinasi kunci hingga menemukan yang benar.
2.1 Waktu Serangan Brute Force
Jika kecepatan komputer adalah Rpercobaan/detik, maka:
T=N/2R

(Menggunakan asumsi rata-rata menemukan kunci pada setengah dari ruang pencarian)
2.2 Contoh
Jika komputer mampu mencoba 1 miliar kunci/detik:
Kunci 64-bit memiliki:
N=2^64≈1.8×10^19
T=2^64/(2⋅10^9 )≈2.9×10^9 " detik "≈92" tahun" 

Maka kunci 64-bit masih relatif aman.

3. Unicity Distance
Unicity Distance adalah ukuran seberapa banyak ciphertext (data terenkripsi) yang diperlukan penyerang untuk dapat memecahkan kunci tanpa ambiguitas, dengan asumsi penyerang mengetahui struktur bahasa/data.
3.1 Rumus Unicity Distance
U=(H(K))/D

di mana:
	U = Unicity Distance (jumlah minimal ciphertext yang diperlukan)
	H(K) = Entropi kunci (bit)
	D = Redundansi per karakter dalam plaintext (bit/karakter)
3.2 Interpretasi
	Jika ciphertext lebih sedikit dari U → serangan sulit berhasil.
	Jika ciphertext lebih banyak dari U → kunci dapat ditebak dengan analisis statistik.
3.3 Contoh
Bahasa Indonesia & Inggris memiliki redundansi sekitar 1,3 bit/karakter.
Jika kunci memiliki entropi 64 bit, maka:
U=64/1.3≈49" karakter ciphertext" 

Artinya, untuk cipher tersebut, mulai sekitar 49 karakter ciphertext, analisis frekuensi dapat mulai mengungkap pola dan membantu pemecahan.

4. Hubungan Entropy, Unicity Distance, dan Brute Force
Konsep	Fokus	Dampaknya terhadap Keamanan
Entropy	Kerandoman kunci	Semakin tinggi entropinya, semakin sulit kunci ditebak
Brute Force	Waktu mencoba semua kunci	Semakin besar ruang kunci, waktu brute force meningkat
Unicity Distance	Banyaknya ciphertext yang dibutuhkan untuk memulihkan kunci	Semakin tinggi U → semakin aman terhadap analisis statistik


---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
Langkah 1 — Perhitungan Entropi
Gunakan rumus:
[ H(K) = \log_2 |K| ]
dengan (|K|) adalah ukuran ruang kunci.
Langkah 2 — Menghitung Unicity Distance

Gunakan rumus:
[ U = \frac{H(K)}{R \cdot \log_2 |A|} ]
dengan:

    (H(K)): entropi kunci,
    (R): redundansi bahasa (misal bahasa Inggris (R \approx 0.75)),
    (|A|): ukuran alfabet (26 untuk A–Z).

Langkah 3 — Analisis Brute Force
Simulasikan waktu brute force dengan asumsi kecepatan komputer tertentu.

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
