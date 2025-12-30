1. Analisis sertifikat website Tokopedia
    Issuer CA (Certificate Authority): DigiCert inc / Google Trust Services, DigiCert Global G2 TLS RSA SHA256 2020 CA1
    Masa berlaku sertifikat : 1 tahun, berlaku dari Rabu, 11 juni 2025 pukul 07.00 - Sabtu, 04 juli 2026 pukul 06.59
    Algoritma enkripsi yang digunakan : PKCS #1 SHA-256 Dengan Enkripsi RSA

2. Analisis sertifikat website shopee.co.id
    Issuer CA (Certificate Authority): DigiCert Global G2 / GlobalSign nv-sa, GlobalSign GCC R6 AlphaSSL CA 2023
    Masa berlaku sertifikat : 1 tahun, berlaku dari Senin, 24 Maret 2025 pukul 10.13 - Sabtu, 25 April 2026 pukul 10.13
    Algoritma enkripsi yang digunakan : PKCS #1 SHA-256 Dengan Enkripsi RSA

3. Analisis sertifikat website bukalapak.com
    Issuer CA (Certificate Authority): Sectigo Limited / Sectigo RSA Domain Validation Secure Server CA, Sectigo Public Server Authentication CA DV R36
    Masa berlaku sertifikat : 1 tahun, berlaku dari Senin, 02 Juni 2025 pukul 07.00 - Rabu, 03 Juni 2026 pukul 06.59
    Algoritma enkripsi yang digunakan : PKCS #1 SHA-384 Dengan Enkripsi RSA

4. Analisis perbandingan Website HTTPS vs Tanpa HTTPS
    a. Dari segi enkripsi data
         - Website dengan HTTPS menggunakan protokol TLS/SSL untuk mengenkripsi data yang dikirim antara pengguna dan server, sehingga data lebih aman dari penyadapan.
         - Website tanpa HTTPS mengirim data dalam bentuk teks biasa (plaintext), sehingga rentan terhadap serangan penyadapan dan pencurian data.
    b. Dari segi keamanan login
         - Website dengan HTTPS melindungi informasi login pengguna dengan enkripsi, sehingga lebih sulit bagi penyerang untuk mencuri kredensial login.
        - Website tanpa HTTPS memungkinkan informasi login dikirim dalam bentuk plaintext, sehingga mudah bagi penyerang untuk mencuri kredensial login
    c. Dari segi sertifikat digital
        - Website dengan HTTPS memiliki sertifikat digital yang diverifikasi oleh otoritas sertifikat (CA), memberikan jaminan bahwa situs tersebut adalah sah dan dapat dipercaya.
        - Website tanpa HTTPS tidak memiliki sertifikat digital, sehingga pengguna tidak dapat memverifikasi keaslian situs tersebut.
    d. Dari segi integritas data
        - Website dengan HTTPS memastikan integritas data selama transmisi, sehingga data tidak dapat diubah atau dimanipulasi tanpa terdeteksi.
        - Website tanpa HTTPS tidak menjamin integritas data, sehingga data dapat diubah atau dimanipulasi selama transmisi tanpa terdeteksi.
    e. Dari segi indikator browser
        - Website dengan HTTPS menampilkan indikator keamanan di browser (seperti ikon gembok), memberikan kepercayaan kepada pengguna bahwa situs tersebut aman.
        - Website tanpa HTTPS tidak menampilkan indikator keamanan, yang dapat menimbulkan keraguan bagi pengguna tentang keamanan situs tersebut.
    f. Darisegi resiko serangan
        - Website dengan HTTPS mengurangi risiko serangan seperti man-in-the-middle (MITM) dan phishing, karena data dienkripsi dan sertifikat digital diverifikasi.
        - Website tanpa HTTPS lebih rentan terhadap serangan MITM dan phishing, karena data dikirim dalam bentuk plaintext dan tidak ada verifikasi sertifikat digital.