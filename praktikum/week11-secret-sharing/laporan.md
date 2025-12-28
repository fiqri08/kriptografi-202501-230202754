# Laporan Praktikum Kriptografi
Minggu ke-: 11  
Topik: [Secret Sharing (Shamir’s Secret Sharing)]  
Nama: [Fiqri Nur Hidayanto]  
NIM: [230202754]  
Kelas: [5IKKA]  

---

## 1. Tujuan
(1. Menjelaskan konsep Shamir Secret Sharing (SSS).
 2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
 3. Menganalisis keamanan skema distribusi rahasia.)

---

## 2. Dasar Teori
1. Pengertian Secret Sharing
    Secret Sharing adalah teknik kriptografi yang digunakan untuk membagi sebuah rahasia (secret) menjadi beberapa bagian yang disebut share, kemudian mendistribusikannya kepada beberapa pihak. Rahasia asli hanya dapat direkonstruksi jika sejumlah minimum share digabungkan kembali, sedangkan sebagian share yang jumlahnya kurang dari batas tersebut tidak memberikan informasi apa pun tentang rahasia.
    Teknik ini banyak digunakan pada sistem yang membutuhkan keamanan dan keandalan tinggi, seperti manajemen kunci kriptografi, sistem perbankan, dan infrastruktur keamanan.
2. Konsep Shamir’s Secret Sharing
    Shamir’s Secret Sharing (SSS) diperkenalkan oleh Adi Shamir pada tahun 1979. Skema ini merupakan skema (t, n)-threshold, yang berarti:
    Rahasia dibagi menjadi n share
    Minimal t share diperlukan untuk merekonstruksi rahasia
    Jika jumlah share < t, rahasia tidak dapat diketahui
    Contoh:
    Skema (3, 5): rahasia dibagi ke 5 orang, minimal 3 orang harus bekerja sama untuk membuka rahasia.
3. Prinsip Dasar Shamir’s Secret Sharing
    Shamir’s Secret Sharing didasarkan pada interpolasi polinomial dalam aritmetika modulo bilangan prima.
    Langkah umum:
    - Rahasia disimpan sebagai konstanta pada sebuah polinomial derajat (t−1)
    - Koefisien polinomial lainnya dipilih secara acak
    - Nilai polinomial dihitung pada beberapa titik untuk menghasilkan share
    - Rekonstruksi rahasia dilakukan dengan interpolasi Lagrange
    Karena sebuah polinomial derajat (t−1) membutuhkan minimal t titik untuk direkonstruksi, maka keamanan threshold dapat dijamin.
4. Proses Pembagian Rahasia
    - Pilih bilangan prima p yang lebih besar dari rahasia S
    - Tentukan derajat polinomial (t−1) dan buat polinomial acak f(x) = a0 + a1*x + a2*x^2 + ... + at-1*x^(t-1), dengan a0 = S
    - Hitung share Si = f(i) mod p untuk i = 1, 2, ..., n
    - Bagikan share Si kepada pihak i
5. Proses Rekonstruksi Rahasia
    - Kumpulkan minimal t share (S1, S2, ..., St)
    - Gunakan interpolasi Lagrange untuk menghitung f(0) yang merupakan rahasia asli S
    - Formula interpolasi Lagrange:
      S = f(0) = Σ (Si * Li(0)) mod p, di mana Li(0) adalah basis Lagrange  untuk titik i.
6. Keamanan Shamir’s Secret Sharing
    - Keamanan SSS didasarkan pada fakta bahwa polinomial derajat (t−1) tidak dapat direkonstruksi dengan kurang dari t titik.
    - Oleh karena itu, pihak yang memiliki kurang dari t share tidak dapat memperoleh informasi apa pun tentang rahasia asli.
    - SSS juga tahan terhadap serangan kolusi, di mana beberapa pihak mencoba bekerja sama untuk mengungkap rahasia tanpa mencapai ambang batas t.
7. Kelebihan dan Kekurangan
    Kelebihan:
    - Keamanan yang kuat berdasarkan teori polinomial
    - Fleksibilitas dalam menentukan ambang batas t dan jumlah share n
    - Tahan terhadap kegagalan sebagian pihak
    Kekurangan:
    - Kompleksitas perhitungan lebih tinggi dibandingkan metode sederhana
    - Memerlukan manajemen share yang baik untuk menghindari kehilangan atau kerusakan
8. Penerapan Shamir’s Secret Sharing
    - Manajemen Kunci: Digunakan untuk membagi kunci kriptografi di antara beberapa administrator.
    - Sistem Perbankan: Melindungi akses ke rekening bersama atau dana penting.
    - Infrastruktur Keamanan: Digunakan dalam sistem yang memerlukan otorisasi dari beberapa pihak untuk tindakan kritis.
9. Kesimpulan
    Shamir’s Secret Sharing adalah metode yang efektif dan aman untuk membagi rahasia di antara beberapa pihak dengan jaminan bahwa rahasia hanya dapat direkonstruksi jika sejumlah minimum pihak bekerja sama. Dengan dasar matematika yang kuat, SSS menjadi salah satu teknik penting dalam kriptografi modern untuk memastikan keamanan dan keandalan dalam berbagai aplikasi.
---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan

Langkah 1 — Implementasi Shamir Secret Sharing
Contoh sederhana dengan library secretsharing:
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)

Langkah 2 — Simulasi Manual (Tanpa Library)
    Mahasiswa juga dapat mencoba membuat implementasi manual berbasis polinomial modulo p untuk memahami konsep matematis.
    1. Pilih bilangan prima p yang cukup besar.
    2. Bangun polinomial f(x) = a0 + a1x + … + ak-1x^(k-1) mod p, dengan a0 = secret.
    3. Bagikan (x, f(x)) sebagai share.
    4. Rekonstruksi menggunakan Lagrange Interpolation.

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
