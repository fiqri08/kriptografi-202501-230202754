# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: [Public Key Infrastructure (PKI & Certificate Authority)]  
Nama: [Fiqri Nur Hidayanto]  
NIM: [230202754]  
Kelas: [5IKKA]  

---

## 1. Tujuan
(1. Membuat sertifikat digital sederhana.
 2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
 3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).)

---

## 2. Dasar Teori
1. Public Key Infrastructure (PKI)
    Public Key Infrastructure (PKI) adalah suatu kerangka kerja (framework) yang digunakan untuk mengelola, mendistribusikan, memverifikasi, dan mencabut kunci kriptografi berbasis kunci publik secara aman. PKI memungkinkan penggunaan kriptografi kunci publik dalam skala besar dengan tingkat kepercayaan yang tinggi.
    PKI bertujuan untuk memastikan bahwa public key benar-benar dimiliki oleh entitas yang sah, sehingga komunikasi digital dapat berlangsung secara aman dan terpercaya.
    Fungsi utama PKI:
    1. Menjamin keaslian identitas pemilik kunci publik
    2. Menjamin integritas data
    3. Mendukung kerahasiaan komunikasi
    4. Menyediakan non-repudiation (tidak dapat menyangkal tindakan)
2. Komponen Utama PKI
    PKI terdiri dari beberapa komponen utama, yaitu:
    a. Certificate Authority (CA)
        CA adalah pihak tepercaya yang bertugas:
        - Memverifikasi identitas pemohon sertifikat
        - Menerbitkan sertifikat digital
        - Menandatangani sertifikat secara digital
        - Mencabut sertifikat jika diperlukan
    b. Sertifikat Digital
        Sertifikat digital adalah dokumen elektronik yang mengikat:
        - Identitas pemilik
        - Public key
        - Informasi masa berlaku
        - Identitas CA penerbit
        Sertifikat digital ditandatangani oleh CA sehingga dapat dipercaya oleh pihak lain.
    c. Registration Authority (RA)
        RA membantu CA dalam proses:
        - Pendaftaran
        - Validasi identitas pemohon sebelum sertifikat diterbitkan
    d. Repository
        Tempat penyimpanan sertifikat dan informasi pencabutan sertifikat yang dapat diakses publik.
3. Certificate Authority (CA)
    Certificate Authority (CA) merupakan lembaga tepercaya yang menjadi inti dari sistem PKI. CA bertanggung jawab memastikan bahwa public key benar-benar milik entitas yang terdaftar, seperti individu, organisasi, atau server.
    CA menandatangani sertifikat menggunakan private key CA, sehingga sertifikat tersebut dapat diverifikasi menggunakan public key CA.
4. Rantai Kepercayaan (Chain of Trust)
    PKI menggunakan konsep chain of trust, yaitu hierarki kepercayaan sebagai berikut:
    Root CA
       ↓
    Intermediate CA
       ↓
    End Entity (Pengguna / Server)

    - Root CA dipercaya secara default oleh sistem operasi dan browser
    - Intermediate CA bertindak sebagai perantara
    - End Entity adalah pengguna akhir atau layanan
    Jika satu sertifikat valid dalam rantai ini, maka kepercayaan dapat diteruskan.
5. Pencabutan Sertifikat
    Sertifikat digital dapat dicabut apabila:
    - Private key bocor
    - Sertifikat disalahgunakan
    - Informasi pemilik tidak lagi valid
    Metode pencabutan:
    - CRL (Certificate Revocation List)
    - OCSP (Online Certificate Status Protocol)
6. Peran PKI dan CA dalam Tanda Tangan Digital
    Dalam sistem tanda tangan digital:
    - PKI memastikan public key dapat dipercaya
    - CA menjamin identitas penandatangan
    - Penerima dapat memverifikasi keaslian tanda tangan dan identitas pengirim
    Hal ini menjadikan tanda tangan digital sah secara teknis dan, pada banyak kasus, sah secara hukum.
7. Kesimpulan Dasar Teori
    Public Key Infrastructure (PKI) dan Certificate Authority (CA) merupakan fondasi utama keamanan komunikasi digital modern. PKI menyediakan mekanisme pengelolaan kunci publik secara aman, sementara CA bertindak sebagai pihak tepercaya yang menjamin keaslian identitas dan validitas sertifikat digital. Kombinasi keduanya memungkinkan penerapan tanda tangan digital, enkripsi, dan autentikasi yang aman dan andal.
---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (cryptography, cryptography.x509.oid, cryptography.hazmat.primitives, cryptography.hazmat.primitives.asymmetric, datetime)  )

---

## 4. Langkah Percobaan

Langkah 1 — Membuat Sertifikat Digital Sederhana
    Contoh dengan Python cryptography:
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")

Langkah 2 — Memverifikasi Sertifikat
- Gunakan public key untuk memverifikasi tanda tangan sertifikat.
- Jelaskan bagaimana CA digunakan untuk menjamin keaslian sertifikat.

Langkah 3 — Analisis PKI
Diskusikan kasus nyata:
- Bagaimana browser memverifikasi sertifikat HTTPS?
    Saat pengguna mengakses situs HTTPS, browser melakukan beberapa langkah verifikasi berikut:
    1. Menerima sertifikat dari server
        - Sertifikat berisi domain, public key, masa berlaku, dan tanda tangan CA.
    2. Memeriksa rantai kepercayaan (Chain of Trust)
        - Browser memverifikasi sertifikat server → Intermediate CA → Root CA.
        - Root CA harus ada dalam trust store browser/OS.
    3. Memverifikasi tanda tangan digital
        - Browser memverifikasi tanda tangan sertifikat menggunakan public key CA.
        - Jika valid, berarti sertifikat benar diterbitkan CA tepercaya.
    4. Memeriksa kecocokan domain
        - Domain pada sertifikat harus cocok dengan URL yang diakses.
    5. Memeriksa masa berlaku & status pencabutan
        - Dicek melalui tanggal validitas serta CRL atau OCSP.
    Jika semua tahap lolos, koneksi HTTPS dinyatakan aman dan ikon gembok ditampilkan.
- Apa yang terjadi jika CA palsu menerbitkan sertifikat?
    Jika CA palsu atau CA yang diretas berhasil menerbitkan sertifikat:
    1. Dampak Keamanan
        - Penyerang dapat melakukan Man-in-the-Middle (MITM)
        - Pengguna tidak menyadari bahwa koneksi mereka disadap
        - Data sensitif seperti password dan nomor kartu kredit dapat dicuri
    2. Respons Sistem Modern
        - Browser akan memblokir atau menandai sertifikat
        - Root CA palsu akan:
            - Dihapus dari trust store
            - Dicabut kepercayaannya (distrusted)
    Contoh nyata:
    Kasus DigiNotar (2011) → CA diretas, sertifikat palsu diterbitkan, akhirnya bangkrut dan dihapus dari browser
- Mengapa PKI penting dalam komunikasi aman (misalnya transaksi online)?
    PKI sangat penting karena menyediakan fondasi kepercayaan dalam komunikasi digital.
    Alasan Utama:
    1. Otentikasi
        - Memastikan pengguna terhubung ke server yang benar (bukan palsu)
    2. Kerahasiaan
        - Data dienkripsi selama transmisi (HTTPS / TLS)
    3. Integritas
        - Data tidak diubah selama pengiriman
    4. Non-repudiation
        - Pihak tidak bisa menyangkal transaksi yang dilakukan
    Contoh Transaksi Online:
    - Login internet banking
    - Pembayaran e-commerce
    - Pengiriman data pribadi
    Tanpa PKI:
    - HTTPS tidak bisa dipercaya
    - Transaksi online sangat rentan terhadap penyadapan dan pemalsuan
---

## 6. Hasil dan Pembahasan
1. Hasil Program (Output)
    "Sertifikat digital berhasil dibuat: cert.pem"

    Selain output di terminal, program juga menghasilkan file baru:
    
    "cert.pem"
    
    yang Berisi sertifikat digital dalam format PEM
    Jika file cert.pem dibuka, isinya kurang lebih seperti berikut (dipotong):
    
    -----BEGIN CERTIFICATE-----
    MIIDXTCCAkWgAwIBAgIUQ9...
    ...
    -----END CERTIFICATE-----

    Isi sertifikat berupa data terenkripsi Base64 yang merepresentasikan sertifikat X.509.
2. Pembahasan Program
    Program ini merupakan contoh implementasi Public Key Infrastructure (PKI) sederhana dengan membuat sertifikat digital self-signed menggunakan library cryptography.
    a. Pembuatan Pasangan Kunci RSA
        key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    
        - Dibuat kunci RSA 2048-bit
        - private key digunakan untuk:
            - Menandatangani sertifikat
        - public key akan:
            - Disimpan di dalam sertifikat
        Panjang 2048-bit merupakan standar minimum keamanan RSA saat ini.
    b. Penentuan Subject dan Issuer
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
            x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
        ])
    
        - Subject dan issuer diatur sama karena ini self-signed
        - Berisi informasi identitas pemilik sertifikat

        Karena subject = issuer, maka: Sertifikat ini adalah self-signed certificate
        Dalam sistem PKI nyata: Issuer ≠ Subject (diterbitkan oleh CA resmi)
    c. Proses Pembuatan Sertifikat X.509
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.utcnow())
        .not_valid_after(datetime.utcnow() + timedelta(days=365))
        .sign(key, hashes.SHA256())
    
        - Membangun sertifikat X.509 dengan informasi:
            - subject_name: identitas pemilik
            - issuer_name: identitas penerbit (CA)
            - public_key: kunci publik pemilik
            - serial_number: nomor unik sertifikat
            - validity period: masa berlaku sertifikat (1 tahun)
        - Sertifikat ditandatangani menggunakan private key dengan algoritma SHA-256
    d. Penandatanganan Sertifikat
        .sign(key, hashes.SHA256())
    
        - Menandatangani sertifikat memastikan integritas dan keaslian
        - Penerima dapat memverifikasi tanda tangan menggunakan public key
        - Dalam kasus self-signed: penerima harus mempercayai sertifikat secara manual
        - Dalam PKI nyata: penerima memverifikasi tanda tangan menggunakan public key CA
    e. Penyimpanan Sertifikat
        cert.public_bytes(serialization.Encoding.PEM)

        - Sertifikat disimpan dalam format PEM (Base64 encoded)
        - Format umum untuk pertukaran sertifikat digital
3. Kaitan dengan PKI & Certificate Authority
    Pada percobaan ini:
    - Sistem mensimulasikan Certificate Authority sederhana
    - CA dan pemilik sertifikat adalah entitas yang sama
    Cocok untuk:
    - Pembelajaran
    - Pengujian lokal
    - Praktikum kriptografi
    Namun:
    Sertifikat tidak otomatis dipercaya oleh browser atau sistem operasi karena tidak berasal dari Root CA resmi.
4. Kesimpulan
    Berdasarkan percobaan yang dilakukan, sistem berhasil membuat sertifikat digital X.509 menggunakan algoritma RSA dan SHA-256 secara self-signed. Sertifikat yang dihasilkan memuat identitas pemilik, public key, masa berlaku, serta tanda tangan digital sebagai penjamin integritas. Percobaan ini menunjukkan peran PKI dan Certificate Authority dalam mengelola identitas dan kepercayaan pada sistem keamanan digital.

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Apa fungsi utama Certificate Authority (CA)?
    Fungsi utama Certificate Authority (CA) adalah:
    1. Memverifikasi identitas pemohon sertifikat
    2. Menerbitkan sertifikat digital yang mengikat identitas dengan kunci publik
    3. Menandatangani sertifikat secara digital untuk menjamin keaslian dan integritasnya
    4. Mencabut sertifikat jika diperlukan, misalnya jika kunci bocor atau informasi pemilik tidak lagi valid.
- Pertanyaan 2: Mengapa self-signed certificate tidak cukup untuk sistem produksi?
    Self-signed certificate tidak cukup untuk sistem produksi karena:
    1. Tidak ada pihak ketiga tepercaya (CA) yang memverifikasi identitas pemilik sertifikat, sehingga penerima tidak dapat memastikan keaslian sertifikat tersebut.
    2. Browser dan sistem operasi umumnya tidak mempercayai self-signed certificate secara default, yang dapat menyebabkan peringatan keamanan bagi pengguna.
    3. Risiko keamanan lebih tinggi, karena siapa pun dapat membuat self-signed certificate tanpa proses verifikasi yang ketat.
    Oleh karena itu, untuk komunikasi aman di lingkungan produksi, sertifikat harus diterbitkan oleh CA resmi yang diakui secara luas.
- Pertanyaan 3: Mengapa PKI penting dalam komunikasi aman (misalnya transaksi online)?
    PKI penting dalam komunikasi aman karena:
    1. Menyediakan mekanisme untuk mengelola kunci publik secara aman, memungkinkan enkripsi dan autentikasi yang andal.
    2. Memastikan keaslian identitas pihak yang berkomunikasi melalui sertifikat digital yang diterbitkan oleh CA tepercaya.
    3. Menjamin integritas data yang dikirimkan, sehingga penerima dapat memverifikasi bahwa data tidak diubah selama transmisi.
    4. Mendukung non-repudiation, sehingga pengirim tidak dapat menyangkal tindakan mereka.
)
---

## 8. Kesimpulan
(Berdasarkan percobaan yang dilakukan, sistem berhasil membuat sertifikat digital X.509 menggunakan algoritma RSA dan SHA-256 secara self-signed. Sertifikat yang dihasilkan memuat identitas pemilik, public key, masa berlaku, serta tanda tangan digital sebagai penjamin integritas. Percobaan ini menunjukkan peran Certificate Authority dalam penerbitan dan pengelolaan sertifikat digital pada sistem PKI.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
1. Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson Education.
2. Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.
3. Katz, J., & Lindell, Y. (2014). Introduction to Modern Cryptography (2nd ed.). CRC Press.
4. Rescorla, E. (2018). The Transport Layer Security (TLS) Protocol Version 1.3. IETF RFC 8446.
5. Python Cryptography Documentation. (n.d.). X.509 Certificates.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
```
commit week10-pki
Author: Fiqri Nur Hidayanto <fiqrinur0801@gmail.com>
Date:   2025-12-28

    week10-pki )
```
