Studi Kasus: Serangan SHA-1 Collision (SHAttered, 2017)
1. Identifikasi Vektor Serangan dan Penyebab Kelemahan
    a. Vektor Serangan: Vektor serangan pada kasus SHAttered adalah collision attack terhadap fungsi hash SHA-1.
    b. Cara Penyerangan:
        1. Membuat dua file PDF berbeda (konten berbeda).
        2. Kedua file menghasilkan nilai hash SHA-1 yang sama.
        3. Sistem yang hanya memverifikasi hash SHA-1 akan menganggap kedua file identik dan sah.
        Ini memungkinkan:
            - Pemalsuan dokumen digital
            - Penyalahgunaan tanda tangan digital
            - Manipulasi integritas data
    c. Penyebab Kelemahan:
        - Desain kriptografi SHA-1 sudah usang
        - Panjang hash 160-bit terlalu pendek untuk standar keamanan modern
        - Adanya kelemahan struktural yang memungkinkan collision dibuat lebih efisien daripada brute-force
2. Analisis Kelemahan Algoritma SHA-1
    a. Cara Kerja Singkat SHA-1
        - Menghasilkan hash 160-bit
        - Menggunakan struktur Merkle–Damgård
        - Dirancang tahun 1995 (era keterbatasan komputasi)
    Kelemahan Teknis
    1. Collision Resistance Melemah
        Idealnya butuh 2⁸⁰ operasi
        SHAttered berhasil menurunkannya menjadi sekitar 2⁶³ operasi
    2. Differential Cryptanalysis
        Penyerang mengeksploitasi pola internal kompresi SHA-1
    3. Advances in Computing Power
        GPU dan cloud computing membuat serangan praktis dilakukan
    Akibatnya, SHA-1 tidak lagi menjamin integritas data.
3. Lokasi Kelemahan: Algoritma, Implementasi, atau Konfigurasi?
    Kelemahan ada pada algoritma kriptografi SHA-1 itu sendiri.
    Penjelasan:
    - Implementasi Google & OpenSSL benar
    - Konfigurasi sistem sesuai standar saat itu
    - Namun algoritma SHA-1 secara matematis sudah tidak aman
    Ini contoh cryptographic design failure, bukan human error.
4. Usulan Algoritma atau Mekanisme yang Lebih Aman
    - Ganti SHA-1 dengan Algoritma Hash yang Lebih Kuat
        - SHA-256 atau SHA-3 (lebih aman, panjang hash lebih besar)
        - Bcrypt, scrypt, atau Argon2 untuk penyimpanan password (memiliki faktor kerja)
5. Alasan Pemilihan
        - SHA-256: Bagian dari keluarga SHA-2, tahan terhadap collision attack saat ini
        - SHA-3: Desain baru, berbeda struktur internalnya
        - Bcrypt/scrypt/Argon2: Dirancang untuk memperlambat brute-force attack
    - Dampak terhadap Keamanan Sistem
        - Meningkatkan integritas data
        - Mengurangi risiko pemalsuan dokumen digital
        - Melindungi sistem tanda tangan digital
        - Meningkatkan kepercayaan pengguna terhadap keamanan data
    Dengan mengganti SHA-1, sistem akan lebih tahan terhadap serangan kriptografi modern.
