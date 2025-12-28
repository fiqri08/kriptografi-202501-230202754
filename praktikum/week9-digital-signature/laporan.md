# Laporan Praktikum Kriptografi
Minggu ke-: 9 
Topik: Digital Signature  
Nama: Fiqri Nur Hidayanto 
NIM: 230202754 
Kelas: 5IKKA  

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

---

## 2. Dasar Teori
1. Pengertian
   Tanda tangan digital adalah mekanisme kriptografi yang digunakan untuk memverifikasi keaslian dan integritas pesan atau dokumen digital. Tanda tangan digital menggunakan algoritma kunci publik, di mana pengirim menggunakan kunci privatnya untuk membuat tanda tangan, dan penerima menggunakan kunci publik pengirim untuk memverifikasi tanda tangan tersebut.
2. Algoritma Tanda Tangan Digital
   Beberapa algoritma yang umum digunakan untuk tanda tangan digital meliputi RSA (Rivest-Shamir-Adleman) dan DSA (Digital Signature Algorithm). RSA menggunakan prinsip faktorisasi bilangan besar, sedangkan DSA didasarkan pada konsep logaritma diskrit.
3. Manfaat Tanda Tangan Digital
   Tanda tangan digital memberikan beberapa manfaat penting, termasuk:
   - Otentikasi: Memastikan bahwa pesan benar-benar berasal dari pengirim yang sah.
   - Integritas: Menjamin bahwa pesan tidak diubah selama transmisi.
   - Non-repudiation: Pengirim tidak dapat menyangkal telah mengirim pesan yang ditandatangani.
4. Proses Tanda Tangan Digital
   Proses tanda tangan digital biasanya melibatkan langkah-langkah berikut:
   - Pembuatan Hash: Pesan asli di-hash menggunakan fungsi hash kriptografi untuk menghasilkan ringkasan pesan.
   - Pembuatan Tanda Tangan: Ringkasan pesan dienkripsi dengan kunci privat pengirim untuk membuat tanda tangan digital.
   - Verifikasi Tanda Tangan: Penerima mendekripsi tanda tangan menggunakan kunci publik pengirim dan membandingkan hasilnya dengan hash dari pesan asli untuk memverifikasi keaslian dan integritas pesan.
5. Aplikasi Tanda Tangan Digital
   Tanda tangan digital banyak digunakan dalam berbagai aplikasi, termasuk email aman, transaksi keuangan online, dan dokumen hukum digital.
6. Keamanan Tanda Tangan Digital
   Keamanan tanda tangan digital bergantung pada kekuatan algoritma kriptografi yang digunakan dan keamanan kunci privat pengirim. Oleh karena itu, penting untuk menggunakan algoritma yang kuat dan menjaga kerahasiaan kunci privat.
7. Regulasi dan Standar
   Banyak negara memiliki regulasi dan standar yang mengatur penggunaan tanda tangan digital, seperti eIDAS di Uni Eropa dan ESIGN Act di Amerika Serikat, yang memberikan dasar hukum untuk penggunaan tanda tangan digital dalam transaksi elektronik.
8. Tantangan dan Perkembangan
   Meskipun tanda tangan digital menawarkan banyak manfaat, ada tantangan yang perlu diatasi, seperti ancaman dari komputer kuantum yang dapat memecahkan algoritma kriptografi saat ini. Oleh karena itu, penelitian terus dilakukan untuk mengembangkan algoritma tanda tangan digital yang lebih aman dan tahan terhadap serangan di masa depan. 
9. Kesimpulan
   Tanda tangan digital adalah komponen penting dalam keamanan informasi modern, memberikan otentikasi, integritas, dan non-repudiation untuk pesan dan dokumen digital. Dengan terus berkembangnya teknologi, penting untuk memastikan bahwa metode tanda tangan digital tetap aman dan efektif
---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
1. Langkah1 - Generate Key dan Buat tanda Tangan
2. Verifikasi Tanda Tangan
3. Uji Modifikasi Pesan
)

---

## 5. Source Code
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())

try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")

# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")

---

## 6. Hasil dan Pembahasan
(1. Hasil Program
    Signature: 6f3a9c8e2d4b1a...c7f9e2a4b0
    Verifikasi berhasil: tanda tangan valid.
    Verifikasi gagal: tanda tangan tidak cocok dengan pesan.
    
    - Dibuat RSA key 2048-bit
    - private_key → digunakan untuk menandatangani pesan
    - public_key → digunakan untuk verifikasi tanda tangan

2. Hashing Pesan dengan SHA-256
    message = b"Hello, ini pesan penting."
    h = SHA256.new(message)

    - Pesan tidak langsung ditandatangani
    - Pesan diubah dulu menjadi hash SHA-256
    - Hash bersifat:
        - Panjang tetap
        - Sensitif terhadap perubahan sekecil apa pun
3. Pembuatan Digital Signature
    signature = pkcs1_15.new(private_key).sign(h)

    - Hash pesan ditandatangani menggunakan:
        - Algoritma RSA
        - Skema PKCS#1 v1.5
    - Hasilnya adalah digital signature
    
    Fungsi tanda tangan digital:
    - Menjamin keaslian pesan
    - Menjamin integritas pesan
    - Menjamin non-repudiation (tidak bisa menyangkal)
4. Verifikasi Tanda Tangan (Pesan Asli)
    pkcs1_15.new(public_key).verify(h, signature)
    
    Hasil: Berhasil
    Artinya:
    - Pesan tidak diubah
    - Signature memang dibuat menggunakan private key pasangan public key tersebut
    Output:
    Verifikasi berhasil: tanda tangan valid.
5. Verifikasi dengan Pesan yang Dimodifikasi
    fake_message = b"Hello, ini pesan palsu."
    h_fake = SHA256.new(fake_message)

    - Pesan diubah sedikit saja
    - Hash yang dihasilkan berbeda total
    - Signature lama dicoba diverifikasi dengan pesan baru
    Hasil: Gagal
    Output:
    Verifikasi gagal: tanda tangan tidak cocok dengan pesan.

    Ini membuktikan:
    - Digital signature sangat sensitif terhadap perubahan pesan
    - Satu huruf berubah → verifikasi gagal

    Kesimpulan
    1. Digital signature RSA berhasil diimplementasikan
    2. Tanda tangan:
        - Valid hanya untuk pesan asli
        - Tidak bisa digunakan untuk pesan yang dimodifikasi
    3. Program membuktikan tiga aspek utama keamanan:
        - Authenticity = pesan benar dari pemilik private key
        - Integrity = pesan tidak diubah
        - Non-repudiation = pengirim tidak bisa menyangkal

)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
    1. Enkripsi RSA
        - Tujuan : Untuk menjaga kerahasiaan (confidentiality) pesan.
        - Penggunaan Kunci :
            - Public key penerima → untuk mengenkripsi pesan
            - Private key penerima → untuk mendekripsi pesan
        - Alur sederhana:
            - Pengirim mengenkripsi pesan dengan public key penerima
            - Penerima mendekripsi pesan dengan private key-nya
        - Fungsi Keamanan:
            - Menjamin pesan tidak bisa dibaca pihak lain
            - Tidak menjamin siapa pengirim pesan
    2. Tanda Tangan Digital RSA
        - Tujuan : Untuk menjamin keaslian dan keutuhan (authenticity & integrity) pesan.
        - Pnggunaan Kunci :
            - Private key pengirim = untuk membuat tanda tangan digital
            - Public key pengirim = untuk memverifikasi tanda tangan digital
        - Alur sederhana:
            - Pengirim membuat tanda tangan digital dengan private key-nya
            - Penerima memverifikasi tanda tangan dengan public key pengirim
        - Fungsi Keamanan:
            - Menjamin pesan benar dari pengirim
            - Menjamin pesan tidak diubah
            - Mendukung non-repudiation
- Pertanyaan 2: Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
    1. Menjamin Integritas Pesan
        Integritas berarti pesan tidak diubah sejak ditandatangani.
        Mekanismenya:
        1. Pesan di-hash (misalnya dengan SHA-256) → menghasilkan nilai hash unik.
        2. Hash tersebut ditandatangani menggunakan private key pengirim.
        3. Penerima menghitung ulang hash dari pesan yang diterima.
        4. Jika hash hasil verifikasi sama, maka pesan utuh.

        Jika pesan diubah sedikit saja:
        - Hash akan berubah total
        - Verifikasi tanda tangan langsung gagal
        Inilah alasan tanda tangan digital menjamin integritas pesan.
    2. Menjamin Otentikasi Pengirim
        Otentikasi berarti pesan benar-benar berasal dari pengirim yang sah.
        Mekanismenya:
        - Hanya pemilik private key yang bisa membuat tanda tangan digital
        - Tanda tangan diverifikasi menggunakan public key yang sesuai
        Jika verifikasi berhasil:
        - Berarti pesan memang ditandatangani oleh pemilik private key
        - Identitas pengirim dapat dipercaya
        Inilah alasan tanda tangan digital menjamin otentikasi pengirim.
    3. Hubungan Hash dan Kunci Privat
        - Hash memastikan pesan tidak diubah
        - Kunci privat memastikan hanya pengirim sah yang bisa menandatangani
        Kombinasi ini memberikan jaminan ganda:
        - Integritas pesan
        - Otentikasi pengirim
    4. Kesimpulan
        Tanda tangan digital menjamin integritas karena setiap perubahan pesan akan mengubah nilai hash sehingga verifikasi gagal, dan menjamin otentikasi karena tanda tangan hanya dapat dibuat menggunakan private key milik pengirim dan diverifikasi dengan public key-nya.
-pertanyaan 3: Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?
    Peran Certificate Authority (CA) sangat penting dalam sistem tanda tangan digital modern karena CA bertindak sebagai pihak tepercaya yang menghubungkan identitas dengan public key secara sah dan terverifikasi.
    1. Masalah Tanpa Certificate Authority
        Tanpa CA, siapa pun bisa:
            - Mengaku sebagai pihak lain
            - Membuat pasangan public–private key sendiri
            - Menipu pengguna (serangan man-in-the-middle)
        Public key saja tidak cukup, karena tidak menjamin siapa pemiliknya.
    2. Peran Utama Certificate Authority
        a. Verifikasi Identitas
            CA memverifikasi identitas pemohon sertifikat, misalnya:
                - Individu
                - Organisasi
                - Website (domain)
            Contoh:
            - Validasi domain untuk HTTPS
            - Validasi organisasi untuk tanda tangan dokumen resmi
        b. Penerbitan Sertifikat Digital
            Setelah identitas diverifikasi, CA menerbitkan sertifikat digital yang berisi:
                - Identitas pemilik
                - Public key pemilik
                - Masa berlaku
                - Informasi CA penerbit
            Sertifikat ini ditandatangani secara digital oleh CA.
        c. Menjamin Kepercayaan (Trust Chain)
            Sistem modern menggunakan rantai kepercayaan (chain of trust):
             Root CA → Intermediate CA → Sertifikat Pengguna
            Sistem operasi dan browser sudah menyimpan Root CA tepercaya.
        d. Pencabutan Sertifikat (Revocation)
            Jika private key bocor atau sertifikat disalahgunakan:
            - CA dapat mencabut sertifikat
            - Dicek melalui CRL (Certificate Revocation List) atau OCSP
    3. Peran CA dalam Tanda Tangan Digital
        Dalam konteks tanda tangan digital:
        - CA memastikan bahwa public key benar milik pengirim
        - Penerima dapat memverifikasi tanda tangan dan identitas pengirim
        - Mendukung non-repudiation (tidak bisa menyangkal)
    4. Contoh Penerapan Nyata
        - HTTPS: Sertifikat SSL/TLS diterbitkan oleh CA untuk mengamankan komunikasi web.
        - Dokumen Elektronik: Sertifikat digital
    5. Kesimpulan
        Certificate Authority (CA) berperan sebagai pihak tepercaya yang memverifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital sehingga tanda tangan digital dapat dipercaya, aman dari pemalsuan, dan terhindar dari serangan penyamaran.
)
---

## 8. Kesimpulan
(Berdasarkan percobaan yang dilakukan, tanda tangan digital RSA berhasil digunakan untuk memverifikasi keaslian dan keutuhan pesan menggunakan pasangan kunci publik dan privat. Hasil verifikasi menunjukkan bahwa pesan asli dapat divalidasi dengan benar, sedangkan pesan yang telah dimodifikasi menyebabkan proses verifikasi gagal. Hal ini membuktikan bahwa tanda tangan digital efektif dalam menjamin integritas dan otentikasi pesan.)
---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
1. Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson Education.
2. Katz, J., & Lindell, Y. (2014). Introduction to Modern Cryptography (2nd ed.). CRC Press.
3. Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.
4. PyCryptodome Documentation. (n.d.). Public Key Cryptography and Digital Signatures.
5. Kahn Academy. (n.d.). RSA Encryption and Digital Signatures.)

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
```
commit week9-digital-signature
Author: Fiqri Nur Hidayanto <fiqrinur0801@gmail.com>
Date:   2025-12-28

    week9-digital-signature )
```
