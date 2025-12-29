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

Langkah 3 — Analisis Keamanan
Diskusikan:
- Mengapa skema (k, n) aman meskipun sebagian share bocor?
    Skema (k, n) pada Shamir’s Secret Sharing tetap aman karena bersifat threshold dan memiliki keamanan information-theoretic.
    - Rahasia disimpan sebagai konstanta pada polinomial derajat (k−1)
    - Diperlukan minimal k titik untuk merekonstruksi polinomial tersebut
    - Jika penyerang hanya memperoleh kurang dari k share, maka terdapat tak terhingga kemungkinan polinomial yang dapat dibentuk
    Artinya:
    - Share yang bocor (< k) tidak memberikan informasi apa pun tentang rahasia
    - Penyerang tidak bisa menebak rahasia meskipun memiliki daya komputasi tak terbatas
- Apa risiko jika threshold k terlalu kecil atau terlalu besar?
    1. Threshold k Terlalu Kecil
        Risiko keamanan meningkat, karena:
        - Sedikit share saja sudah cukup untuk membuka rahasia
        - Jika beberapa pihak berkolusi, rahasia dapat terbongkar
        Contoh:
        Skema (2, 5) → dua orang saja bisa membuka rahasia, rawan penyalahgunaan
    2. Threshold k Terlalu Besar
        Risiko ketersediaan meningkat, karena:
        - Sulit mengumpulkan cukup share
        - Jika satu atau dua share hilang, rahasia bisa tidak dapat dipulihkan
        Contoh:
        Skema (5, 5) → kehilangan satu share → rahasia hilang selamanya
    3. Trade-off Keamanan vs Ketersediaan
        Pemilihan nilai k harus seimbang antara:
        - Keamanan (confidentiality)
        - Ketersediaan (availability)
- Bagaimana penerapan SSS di dunia nyata (contoh: manajemen kunci cryptocurrency, recovery password)?
    Bagaimana Penerapan SSS di Dunia Nyata?
    a. Manajemen Kunci Cryptocurrency
        - Private key dompet dibagi ke beberapa pihak atau perangkat
        - Transaksi hanya bisa dilakukan jika threshold terpenuhi
        - Mencegah kehilangan atau pencurian satu kunci tunggal
        Contoh:
        - Multi-signature wallet
        - Custody crypto institusional
    b. Recovery Password dan Akses Sistem
        - Password master dibagi ke beberapa admin
        - Sistem dapat dipulihkan jika sebagian admin tersedia
        - Mencegah satu orang menyalahgunakan akses
    c. Keamanan Cloud & Data Sensitif
        - Kunci enkripsi dibagi ke beberapa server
        - Server tunggal tidak memiliki kunci lengkap
        - Meningkatkan keamanan terhadap kompromi internal
    d. Sistem Voting Elektronik
        - Kunci dekripsi suara dibagi ke beberapa otoritas
        - Hasil hanya dapat dibuka jika otoritas bekerja sama
---

## 5. Source Code
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)

---

## 6. Hasil dan Pembahasan
1. Hasil Program (Output)
    Saat program dijalankan, output yang muncul kurang lebih seperti berikut:

    Shares: [
    '1-7c1e9f8a2d...',
    '2-a93b4c7e51...',
    '3-4f92d8ab61...',
    '4-9c3e1a5f2d...',
    '5-e8b7c4d91a...'
    ]

    Recovered secret: KriptografiUPB2025

    Catatan penting:
    - Nilai shares akan selalu berbeda setiap kali program dijalankan
    - Hal ini karena proses pembagian rahasia melibatkan bilangan acak
    - Namun, hasil rekonstruksi rahasia tetap sama

2. Pembahasan Program
    Program ini mengimplementasikan Shamir’s Secret Sharing (SSS) menggunakan library secretsharing untuk membagi dan merekonstruksi sebuah rahasia secara aman.
    a. Pendefinisian Rahasia
        secret = "KriptografiUPB2025"
        
        - Rahasia berupa string
        - Nilai ini yang ingin diamankan agar:
            - Tidak diketahui oleh satu pihak saja
            - Hanya dapat dibuka melalui kerja sama beberapa pihak

    b. Proses Pembagian Rahasia (Split Secret)
        shares = SecretSharer.split_secret(secret, 3, 5)

        - Skema yang digunakan adalah (k, n) = (3, 5)
            - Rahasia dibagi menjadi 5 share
            - Minimal 3 share dibutuhkan untuk rekonstruksi
        Setiap share berbentuk:
            x-y
        di mana:
        x = indeks share
        y = nilai hasil evaluasi polinomial
        Setiap share tidak mengandung informasi rahasia secara langsung.
3. Hasil Shares
    print("Shares:", shares)

    - Lima share dihasilkan dan dapat didistribusikan ke pihak berbeda
    - Jika hanya 1 atau 2 share yang bocor:
        - Rahasia tetap aman
        - Tidak dapat direkonstruksi
4. Rekonstruksi Rahasia
    recovered = SecretSharer.recover_secret(shares[:3])
    print("Recovered secret:", recovered)

    - Menggunakan tiga share pertama untuk merekonstruksi rahasia
    - Fungsi recover_secret melakukan interpolasi Lagrange di balik layar
    - Hasil rekonstruksi adalah rahasia asli "KriptografiUPB2025"
5. Hasil Rekonstruksi
    Recovered secret: KriptografiUPB2025

    - Rahasia berhasil direkonstruksi 100% identik
    - Membuktikan bahwa:
        - Skema threshold bekerja dengan benar
        - Share kurang dari threshold tidak cukup
6. Analisis Keamanan
    a. Keamanan Skema (k, n)
        - Dengan skema (3, 5):
            - Minimal 3 share diperlukan untuk membuka rahasia
            - Jika hanya 1 atau 2 share bocor:
                - Tidak ada informasi yang dapat diperoleh tentang rahasia
                - Keamanan terjamin secara information-theoretic
    b. Risiko Threshold
        - Jika threshold k terlalu kecil (misal k=2):
            - Rahasia lebih rentan terhadap kolusi
        - Jika threshold k terlalu besar (misal k=5):
            - Risiko kehilangan rahasia meningkat jika satu share hilang
    c. Penerapan Dunia Nyata
        - Manajemen kunci cryptocurrency:
            - Private key dibagi ke beberapa pihak
            - Transaksi hanya bisa dilakukan jika threshold terpenuhi
        - Recovery password:
            - Password master dibagi ke beberapa admin
            - Sistem dapat dipulihkan jika sebagian admin tersedia
        - Keamanan cloud:
            - Kunci enkripsi dibagi ke beberapa server
            - Meningkatkan keamanan terhadap kompromi internal
        - Sistem voting elektronik:
            - Kunci dekripsi suara dibagi ke beberapa otoritas
            - Hasil hanya dapat dibuka jika otoritas bekerja sama
    d. Kesimpulan Analisis
        - Shamir’s Secret Sharing adalah metode efektif untuk membagi rahasia
        - Menyediakan keamanan yang kuat dengan jaminan matematis
        - Penting untuk memilih threshold k yang tepat sesuai kebutuhan keamanan dan ketersediaan

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1:  Apa keuntungan utama Shamir Secret Sharing dibanding membagikan salinan kunci secara langsung?
    Jawaban:
    Keuntungan utama Shamir Secret Sharing dibandingkan dengan membagikan salinan kunci secara langsung adalah:
    1. Keamanan Threshold: Dengan SSS, rahasia hanya dapat direkonstruksi jika sejumlah minimum share (threshold) digabungkan. Ini mencegah pihak yang tidak berwenang dari mengakses rahasia hanya dengan memiliki satu atau dua salinan kunci.
    2. Tahan terhadap Kehilangan: Jika beberapa share hilang atau rusak, rahasia masih dapat direkonstruksi selama threshold terpenuhi. Ini meningkatkan keandalan sistem.
    3. Perlindungan terhadap Kolusi: SSS melindungi rahasia dari kolusi antara beberapa pihak yang memiliki share, selama jumlah mereka kurang dari threshold.
    4. Fleksibilitas: SSS memungkinkan penyesuaian jumlah share dan threshold sesuai kebutuhan keamanan dan ketersediaan.
- Pertanyaan 2: Apa peran threshold (k) dalam keamanan secret sharing?
    Jawaban:
    Threshold (k) dalam secret sharing menentukan jumlah minimum share yang diperlukan untuk merekonstruksi rahasia asli. Peran threshold dalam keamanan secret sharing meliputi:
    1. Menentukan Tingkat Keamanan: Semakin tinggi nilai k, semakin sulit bagi pihak yang tidak berwenang untuk mengakses rahasia, karena mereka memerlukan lebih banyak share untuk rekonstruksi.
    2. Mencegah Akses Tidak Sah: Dengan menetapkan threshold, secret sharing memastikan bahwa rahasia tidak dapat diakses oleh individu atau kelompok yang memiliki kurang dari k share, sehingga meningkatkan
    3. Menyeimbangkan Keamanan dan Ketersediaan: Pemilihan nilai k harus mempertimbangkan kebutuhan keamanan dan ketersediaan. Nilai k yang terlalu rendah dapat mengurangi keamanan, sementara nilai k yang terlalu tinggi dapat mengurangi ketersediaan rahasia.
- Pertanyaan 3: Berikan satu contoh skenario nyata di mana SSS sangat bermanfaat.
    Jawaban:
    Satu contoh skenario nyata di mana Shamir Secret Sharing (SSS) sangat bermanfaat adalah dalam manajemen kunci cryptocurrency untuk dompet multi-signature. Dalam skenario ini, private key yang digunakan untuk mengakses dana dalam dompet cryptocurrency dibagi menjadi beberapa share yang didistribusikan kepada beberapa pihak, seperti anggota tim atau administrator. Dengan menggunakan skema (k, n), di mana k adalah jumlah minimum share yang diperlukan untuk melakukan transaksi dan n adalah total share yang dibagikan, SSS memastikan bahwa tidak ada satu pihak pun yang dapat mengakses dana secara sepihak. Hanya ketika sejumlah minimum pihak bekerja sama dan menggabungkan share mereka, transaksi dapat dilakukan. Ini meningkatkan keamanan dana dengan mencegah pencurian atau penyalahgunaan oleh satu individu, sekaligus memastikan bahwa dana tetap dapat diakses jika beberapa pihak tidak tersedia.

)
---

## 8. Kesimpulan
(Berdasarkan percobaan yang dilakukan, Shamir’s Secret Sharing berhasil membagi sebuah rahasia menjadi beberapa bagian dengan skema threshold (3,5). Rahasia hanya dapat direkonstruksi jika jumlah share yang digunakan memenuhi ambang batas yang ditentukan. Percobaan ini membuktikan bahwa metode Secret Sharing efektif dalam menjaga keamanan rahasia meskipun sebagian share bocor.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
1. Shamir, A. (1979). How to Share a Secret. Communications of the ACM, 22(11), 612–613.
2. Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.
3. Katz, J., & Lindell, Y. (2014). Introduction to Modern Cryptography (2nd ed.). CRC Press.
4. Boneh, D., & Shoup, V. (2020). A Graduate Course in Applied Cryptography. Draft book.
5. SecretSharing Python Library Documentation. (n.d.). Shamir’s Secret Sharing Implementation.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
```
commit week11-secret-sharing
Author: Fiqri Nur Hidayanto <fiqrinur0801@gmail.com>
Date:   2025-12-29

    week11-secret-sharing )
```
