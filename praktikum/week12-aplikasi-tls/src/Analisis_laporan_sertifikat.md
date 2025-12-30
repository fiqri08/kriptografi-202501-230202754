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
5. Isu privasi dan dilema etika dalam penggunaan email terenkripsi (PGP & S/MIME)
    1. Isu Privasi dalam Penggunaan Email Terenkripsi (PGP & S/MIME)
        a. Perlindungan Konten vs Metadata
            PGP dan S/MIME melindungi isi email (body & attachment) melalui enkripsi.
            Namun metadata tidak terenkripsi, seperti:
                1. Alamat pengirim & penerima
                2. Subjek email (seringkali)
                3. Waktu pengiriman
            Metadata ini tetap dapat dianalisis untuk memetakan pola komunikasi pengguna.
            Isu privasi: walaupun isi email aman, aktivitas komunikasi tetap dapat dipantau.
        b. Manajemen Kunci Kriptografi
            PGP:
                Pengguna bertanggung jawab penuh atas manajemen kunci publik & privat.
                Risiko kehilangan kunci privat = email tidak bisa dibuka.
            S/MIME:
                Kunci dikelola oleh Certificate Authority (CA) dan seringkali oleh organisasi/perusahaan.
                Risiko: pihak ketiga (perusahaan/CA) berpotensi memiliki akses ke kunci privat.
            Isu privasi: ketergantungan pada pihak ketiga dapat menimbulkan risiko kebocoran kunci.
        c. False Sense of Security
            Banyak pengguna menganggap email terenkripsi = 100% aman.
            Faktanya:
                - Email bisa dibuka di perangkat yang terinfeksi malware.
                - Screenshot, forward, atau human error tetap terjadi.
            Isu privasi: enkripsi tidak melindungi dari kebocoran di sisi pengguna.
6. Dilema Etika: Apakah Perusahaan Boleh Mendekripsi Email Karyawan?
    Argumen Mendukung (Pro)
        1. Keamanan perusahaan
            - Mencegah kebocoran data rahasia
            - Deteksi insider threat
        2. Kepatuhan hukum
            - Audit internal
            - Investigasi pelanggaran
        3. Email adalah aset perusahaan
            - Akun dan server dimiliki perusahaan
        Secara hukum di banyak negara, diperbolehkan jika tercantum dalam kebijakan internal.
    Argumen Menolak (Kontra)
        1. Pelanggaran privasi individu
            Email bisa mengandung informasi pribadi
        2. Erosi kepercayaan karyawan
            Lingkungan kerja tidak sehat
        3. Penyalahgunaan wewenang
            Audit bisa digunakan untuk pengawasan berlebihan
        Secara etika, dekipsi tanpa persetujuan jelas dianggap melanggar privasi.
    Pendekatan Etis yang Seimbang
        - Transparansi kebijakan (tertulis & disetujui karyawan)
        - Audit hanya dalam kondisi khusus
        - Prinsip least privilege
        - Logging & akuntabilitas
7. Dilema Etika: Kebijakan Pemerintah dalam Pengawasan Komunikasi Terenkripsi
    a. Kepentingan Keamanan Nasional
        Argumen pro pengawasan:
            - Pencegahan terorisme
            - Penegakan hukum
            - Kejahatan siber lintas negara
        Pemerintah sering meminta:
            - Backdoor enkripsi
            - Akses ke private key
            - Dekripsi paksa
    b. Risiko terhadap Hak Privasi & HAM
        Argumen kontra:
            - Backdoor melemahkan keamanan global
            - Potensi penyalahgunaan kekuasaan
            - Melanggar hak privasi dan kebebasan berekspresi
        Prinsip kriptografi modern: “Backdoor for good people is also a backdoor for bad people.”
    c. Pendekatan yang Lebih Etis & Aman
        - Targeted surveillance (bukan mass surveillance)
        - Akses berbasis putusan pengadilan
        - Fokus pada metadata dan endpoint, bukan merusak enkripsi
        - Penguatan regulasi perlindungan data
8. Kesimpulan
    Email terenkripsi seperti PGP dan S/MIME sangat penting untuk melindungi privasi komunikasi, namun tetap menyisakan isu terkait metadata, manajemen kunci, dan kebijakan akses. Secara etika, baik perusahaan maupun pemerintah harus menyeimbangkan keamanan dan hak privasi, dengan menjunjung transparansi, legalitas, dan prinsip minimal intrusi.
