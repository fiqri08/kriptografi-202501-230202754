# Laporan Praktikum Kriptografi
Minggu ke-: 4  
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
def entropy(keyspace_size):
    return math.log2(keyspace_size)
menjadi 
entropy -= p * math.log2(p)

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))
menjadi
def hitung_unicity_distance(entropy_per_char, key_space):
    return key_space / entropy_per_char

Entropy ruang kunci = 4.7 bit
Unicity distance ≈ 0.24 huruf
menjadi
Entropy teks ≈ 4.5 bit/karakter
Key space = 4.7 bit
Unicity distance ≈ 1.04 karakter


---

## 6. Hasil dan Pembahasan
-hasil masih masuk akal
-untuk error nya adalah dimana tidak boleeh kosong di bagian inputnya


---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Dalam konteks kekuatan kunci kriptografi, entropi adalah ukuran seberapa tidak terduga (random) atau seberapa banyak ketidakpastian yang ada dalam pemilihan kunci. 
- Pertanyaan 2: Unicity distance (U) adalah jumlah minimal ciphertext (biasanya dalam satuan karakter atau bit) yang diperlukan agar hanya ada satu kunci yang mungkin menghasilkan plaintext yang masuk akal.
- Pertanyaan 3: Meskipun algoritma enkripsi modern seperti AES, RSA, ChaCha20, dll dirancang agar sangat kuat secara matematis, brute force masih dianggap ancaman nyata. bukan karena lemah di algoritma, tapi karena faktor manusia, implementasi, dan sistem di sekitarnya.
1. Manusia jarang menggunakan kunci dengan entropi maksimum
2. Kelemahan implementasi, bukan algoritma
3. Kekuatan komputasi terus meningkat
4. Serangan hibrida: brute force + kecerdasan
)
---

## 8. Kesimpulan
Entropi menggambarkan tingkat keacakan atau ketidakpastian suatu kunci. semakin tinggi entropinya, semakin sulit kunci ditebak.
Unicity distance menunjukkan seberapa banyak ciphertext yang dibutuhkan agar hanya satu kunci yang mungkin benar, sehingga mengukur batas teoretis keamanan cipher.
Keduanya bersama-sama menentukan seberapa kuat suatu sistem kriptografi terhadap upaya pemecahan kunci.

---
