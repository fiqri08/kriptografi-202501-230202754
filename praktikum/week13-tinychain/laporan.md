# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: [TinyChain – Proof of Work (PoW)]  
Nama: [Fiqri Nur Hidayanto]  
NIM: [230202754]  
Kelas: [5IKKA]  

---

## 1. Tujuan
(1. Menjelaskan peran hash function dalam blockchain.
 2. Melakukan simulasi sederhana Proof of Work (PoW).
 3. Menganalisis keamanan cryptocurrency berbasis kriptografi.)

---

## 2. Dasar Teori
1. TinyChain
    TinyChain merupakan implementasi sederhana dari teknologi blockchain yang digunakan untuk tujuan pembelajaran. TinyChain dirancang untuk membantu memahami konsep dasar blockchain seperti:
    - Struktur blok
    - Rantai blok (chain)
    - Hash kriptografis
    - Mekanisme konsensus
    TinyChain biasanya tidak digunakan dalam sistem produksi, tetapi berfungsi sebagai simulasi blockchain skala kecil untuk mempelajari cara kerja sistem terdistribusi secara aman.
2. Konsep Blockchain pada TinyChain
    Blockchain adalah struktur data yang tersusun dari blok-blok yang saling terhubung. Setiap blok pada TinyChain umumnya berisi:
    - Data transaksi
    - Hash blok sebelumnya
    - Timestamp
    - Nonce
    - Hash blok saat ini
    Keterkaitan hash antar blok membuat blockchain sulit dimodifikasi, karena perubahan pada satu blok akan memengaruhi seluruh rantai setelahnya.
3. Proof of Work (PoW)
    Proof of Work (PoW) adalah mekanisme konsensus yang digunakan untuk:
    - Memvalidasi blok baru
    - Menjaga keamanan jaringan blockchain
    - Mencegah manipulasi data
    Pada PoW, penambang (miner) harus menyelesaikan permasalahan komputasi kriptografis yang membutuhkan usaha (work) sebelum blok dapat ditambahkan ke blockchain.
4. Prinsip Kerja Proof of Work
    Prinsip utama PoW adalah mencari nilai nonce sehingga hash blok memenuhi kondisi tertentu, misalnya:
    - Hash diawali dengan sejumlah nol tertentu
    Secara matematis:
     hash(block) < target
    Langkah umum PoW:
    1. Miner membentuk blok baru
    2. Miner mencoba berbagai nilai nonce
    3. Hash blok dihitung berulang kali
    4. Jika hash memenuhi tingkat kesulitan, blok dianggap valid
    5. Blok ditambahkan ke blockchain
5. Proof of Work pada TinyChain
    Dalam TinyChain, PoW diimplementasikan secara sederhana untuk:
    - Mensimulasikan proses mining
    - Menunjukkan hubungan antara nonce, hash, dan tingkat kesulitan
    - Memahami biaya komputasi dalam blockchain
    Tingkat kesulitan (difficulty) biasanya diatur rendah agar proses mining:
    - Cepat
    - Mudah diamati
    - Cocok untuk pembelajaran
6. Fungsi Proof of Work dalam TinyChain
    PoW pada TinyChain memiliki beberapa fungsi utama:
    1. Menjamin Integritas Data
        Perubahan data akan mengubah hash dan membuat blok tidak valid.
    2. Mencegah Serangan Manipulasi
        Penyerang harus menghitung ulang PoW untuk semua blok berikutnya.
    3. Menyediakan Mekanisme Konsensus
        Blok yang sah adalah blok dengan PoW valid.
7. Kelebihan dan Kekurangan Proof of Work
    Kelebihan:
    1. Konsep sederhana dan mudah dipahami
    2. Keamanan tinggi jika tingkat kesulitan memadai
    3. Telah teruji pada blockchain besar seperti Bitcoin
    Kekurangan:
    1. Boros energi dan sumber daya komputasi
    2. Skalabilitas rendah
    3. Waktu konfirmasi relatif lama
8. Relevansi TinyChain – PoW dalam Pembelajaran
    TinyChain dengan PoW sangat relevan digunakan sebagai media pembelajaran karena:
    - Menyederhanakan konsep blockchain kompleks
    - Memudahkan pemahaman mekanisme mining
    - Menjadi dasar untuk mempelajari konsensus lain seperti Proof of Stake (PoS)
9. Kesimpulan Dasar Teori
    TinyChain merupakan implementasi blockchain sederhana yang digunakan untuk memahami konsep dasar teknologi blockchain. Proof of Work (PoW) berperan sebagai mekanisme konsensus yang menjamin keamanan dan integritas data melalui proses komputasi kriptografis. Kombinasi TinyChain dan PoW memberikan gambaran nyata tentang cara kerja blockchain sebelum diterapkan pada sistem berskala besar.
---

## 3. Alat dan Bahan
(- Python 3.13  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (hashlib, time)  )

---

## 4. Langkah Percobaan
Langkah 1 — Membuat Struktur Blok
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

Langkah 2 — Membuat Blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))

Langkah 3 — Analisis Proof of Work
- Perhatikan bahwa proses mining membutuhkan waktu (bergantung pada difficulty).
- Analisis: semakin tinggi difficulty, semakin lama proses mining.
- Diskusikan bagaimana hal ini menjamin keamanan blockchain.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

# Uji coba blockchain
my_chain = Blockchain()
print("Mining block 1...")
my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

print("Mining block 2...")
my_chain.add_block(Block(2, "", "Transaksi B → C: 5 Coin"))
```
)

---

## 6. Hasil dan Pembahasan
1. Hasil Program (Output)
    Saat program dijalankan, output yang muncul di terminal kurang lebih seperti berikut:
    
    Mining block 1...
    Block mined: 0000a3f9c1b2e8d7f4a6c9e1b8d2f0c4a7e9b5d3c2a1f8e6d4c7b9a0d2

    Mining block 2...
    Block mined: 00003f7c8e1a9d2b6c4f5e7a0b3d8c9f1e2a4b6d5c7f9e8a0b1d2c3

    Catatan penting:
    - Nilai hash selalu berbeda setiap eksekusi
    - Waktu mining tergantung:
    - Nilai difficulty
    - Performa komputer
    Pola utama yang sama:
    - Hash diawali 4 angka nol (0000)
2. Pembahasan Program
    Program ini merupakan implementasi blockchain sederhana (TinyChain) dengan mekanisme konsensus Proof of Work (PoW) untuk tujuan pembelajaran.
    1. Struktur Kelas Block
        class Block:

        Setiap blok memiliki atribut:
        - index = nomor urut blok
        - timestamp = waktu pembuatan blok
        - data = data transaksi
        - previous_hash = hash blok sebelumnya
        - nonce = angka acak untuk PoW
        - hash = hash blok saat ini
        Struktur ini mencerminkan blok blockchain nyata.
    2. Proses Perhitungan Hash
        def calculate_hash(self):

        - Data blok digabung menjadi satu string
        - Diproses menggunakan SHA-256
        - Hasilnya berupa hash unik 256-bit
        Perubahan kecil pada data membuat hash berubah total yang bertujuan untuk menjamin integritas data
    3. Proof of Work (Mining)
        def mine_block(self, difficulty):

        - Miner mencari nilai nonce agar hash memenuhi syarat:
        hash diawali dengan "0000"
    
        - Semakin besar difficulty, semakin lama proses mining
        Inilah konsep Proof of Work:
        - Membutuhkan usaha komputasi
        - Sulit dicari, mudah diverifikasi
    4. Kelas Blockchain
        class Blockchain:

        Fungsi utama:
        1. Membuat Genesis Block
        2. Menyimpan rantai blok
        3. Mengatur tingkat kesulitan (difficulty = 4)
        4. Menambahkan blok baru ke rantai
        Genesis Block:
        Block(0, "0", "Genesis Block")

    5. Proses Penambahan Blok
        my_chain.add_block(Block(1, "", "Transaksi A → B: 10 Coin"))

        Langkah yang terjadi:
        1. previous_hash diisi dengan hash blok terakhir
        2. Proses mining dijalankan
        3. Blok valid ditambahkan ke blockchain
        Ini membentuk rantai blok yang saling terhubung
    6. Analisis Keamanan Blockchain
        Jika satu blok diubah:
        - Hash berubah
        - Semua blok setelahnya menjadi tidak valid
        Untuk memalsukan data:
        - Penyerang harus menambang ulang semua blok
        - Biaya komputasi sangat besar
        Inilah kekuatan PoW dan hash chaining dalam menjaga keamanan blockchain.
---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: Mengapa fungsi hash sangat penting dalam blockchain?
    Fungsi hash sangat penting dalam blockchain karena berfungsi untuk:
    1. Menjamin Integritas Data
        Setiap blok memiliki hash unik yang mencerminkan isinya. Jika data di dalam blok diubah, hash juga akan berubah secara drastis, sehingga memudahkan deteksi perubahan atau manipulasi data.
    2. Menghubungkan Blok-Blok
        Setiap blok menyimpan hash dari blok sebelumnya, menciptakan rantai yang saling terhubung. Ini membuatnya sulit untuk mengubah satu blok tanpa mempengaruhi seluruh rantai.
    3. Mendukung Mekanisme Konsensus
        Dalam Proof of Work (PoW), fungsi hash digunakan untuk menentukan apakah sebuah blok valid berdasarkan tingkat kesulitan tertentu (misalnya, hash harus diawali dengan sejumlah nol). Ini memastikan bahwa penambahan blok baru memerlukan usaha komputasi yang signifikan, sehingga meningkatkan keamanan jaringan.
- Pertanyaan 2: Bagaimana Proof of Work mencegah double spending?
    Proof of Work (PoW) mencegah double spending dengan cara:
    1. Memerlukan Usaha Komputasi
        Setiap kali seseorang ingin menambahkan transaksi baru ke blockchain, mereka harus menyelesaikan perhitungan PoW yang memerlukan usaha komputasi yang besar. Ini membuatnya mahal
        dan sulit untuk menambahkan blok yang berisi transaksi ganda.
    2. Validasi oleh Jaringan
        Setelah blok baru ditambang, blok tersebut harus divalidasi oleh node lain di jaringan. Jika ada upaya untuk memasukkan transaksi ganda
        dalam blok, node lain akan menolak blok tersebut karena tidak sesuai dengan aturan konsensus.
- Pertanyaan 3: Apa kelemahan dari PoW dalam hal efisiensi energi?
    Kelemahan utama dari Proof of Work (PoW) dalam hal efisiensi energi adalah:
    1. Konsumsi Energi yang Tinggi
        Proses mining dalam PoW memerlukan daya komputasi yang besar, yang pada gilirannya mengonsumsi banyak energi listrik. Ini dapat berdampak negatif pada lingkungan, terutama jika sumber energi yang digunakan berasal dari bahan bakar fosil.
    2. Skalabilitas Terbatas
        Karena PoW memerlukan usaha komputasi yang signifikan, ini dapat membatasi jumlah transaksi yang dapat diproses dalam waktu tertentu. Hal ini dapat menyebabkan kemacetan jaringan dan biaya transaksi yang tinggi.
    3. Sentralisasi Penambangan
        Biaya tinggi untuk menjalankan perangkat keras penambangan dapat menyebabkan sentralisasi penambangan di tangan beberapa entitas besar, yang bertentangan dengan prinsip desentralisasi blockchain.
)
---

## 8. Kesimpulan
(Berdasarkan percobaan yang dilakukan, sistem blockchain sederhana dengan mekanisme Proof of Work berhasil dibuat dan diuji. Proses mining memastikan setiap blok memiliki hash yang memenuhi tingkat kesulitan tertentu sehingga data sulit dimanipulasi. Percobaan ini menunjukkan bahwa penggabungan fungsi hash dan Proof of Work mampu menjaga integritas dan keamanan data pada blockchain.  )

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
1. Nakamoto, S. (2008). Bitcoin: A Peer-to-Peer Electronic Cash System.
2. Antonopoulos, A. M. (2017). Mastering Bitcoin: Programming the Open Blockchain (2nd ed.). O’Reilly Media.
3. Drescher, D. (2017). Blockchain Basics: A Non-Technical Introduction in 25 Steps. Apress.
4. Narayanan, A., Bonneau, J., Felten, E., Miller, A., & Goldfeder, S. (2016). Bitcoin and Cryptocurrency Technologies. Princeton University Press.
5. Python Software Foundation. (n.d.). hashlib — Secure hashes and message digests.
---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
```
commit week13-tinychain
Author: Fiqri Nur Hidayanto <fiqrinur0801@gmail.com>
Date:   2025-11-29

    week13-tinychain )
```
