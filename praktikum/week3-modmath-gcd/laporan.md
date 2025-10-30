# Laporan Praktikum Kriptografi
Minggu ke-: 3  
Topik: MOdular Math (Aritmetika Modular, GCD, Bilangan Prima, Logaritma Diskrit)  
Nama: Fiqri Nur Hidayanto  
NIM: 230202754
Kelas: 5IKKA  

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular dasar.
2. Menghitung bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.
---

## 2. Dasar Teori
1. Pengertian

Modular aritmetika (atau aritmetika modulo) adalah sistem perhitungan bilangan bulat di mana hasil operasi dibatasi pada sisa pembagian terhadap suatu bilangan tertentu (modulus).
Konsep ini sering disebut juga sebagai aritmetika sisa.

Secara Matematis ditulis:
a ≡ b (mod m)
dibaca "a kongruen dengan b modulo m" yang berarti bahwa ketika a dibagi dengan m, sisanya adalah b.
Contoh:
Misal a - 17, n = 5 maka 17 mod 5 = 2 karena 17 dibagi 5 sisanya 2.

2. Sifat-sifat Aritmetika Modular
Beberapa sifat dasar dari aritmetika modular meliputi:
- Penjumlahan: (a + b) mod m = [(a mod m) + (b mod m)] mod m
- Pengurangan: (a - b) mod m = [(a mod m) - (b mod m)] mod m mod m
- Perkalian: (a * b) mod m = [(a mod m) * (b mod m)] mod m
- Pemangkatan: (a^k) mod m = [(a mod m)^k] mod m

3. Aplikasi Modular Aritmetika
Modular aritmetika banyak digunakan dalam:
- Kriptografi: Algoritma enkripsi seperti RSA dan Diffie-Hellman menggunakan aritmetika modular untuk keamanan data.
- Sistem komputer: Penghitungan alamat memori, hashing, dan algoritma lainnya.


---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
Langkah 1 - Aritmetika Modular Dasar.
def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))

Langkah 2 - GCD dan Algoritma Euclidean.
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))

Langkah 3 - Extended Euclidean Algorithm.
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4

Langkah 4 - Logaritma Diskrit
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4

---

## 5. Source Code
# ====== Operasi Aritmetika Modular ======
def mod_add(a, b, n): 
    return (a + b) % n

def mod_sub(a, b, n): 
    return (a - b) % n

def mod_mul(a, b, n): 
    return (a * b) % n

def mod_exp(base, exp, n): 
    return pow(base, exp, n)  # eksponensiasi modular cepat


# ====== GCD dan Extended GCD ======
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n


# ====== Logaritma Diskrit (Brute Force) ======
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None


# ====== PROGRAM UTAMA ======
def main():
    print("=== PROGRAM ARITMETIKA MODULAR & KRIPTOGRAFI DASAR ===")
    print("1. Penjumlahan Modular")
    print("2. Pengurangan Modular")
    print("3. Perkalian Modular")
    print("4. Eksponensiasi Modular")
    print("5. GCD (Pembagi Bersama Terbesar)")
    print("6. Invers Modular")
    print("7. Logaritma Diskrit (Brute Force)")
    print("0. Keluar")
    
    while True:
        try:
            pilihan = int(input("\nPilih menu (0-7): "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 0:
            print("Terima kasih! Program selesai.")
            break

        # Input sesuai kebutuhan tiap operasi
        if pilihan in [1, 2, 3]:
            a = int(input("Masukkan a: "))
            b = int(input("Masukkan b: "))
            n = int(input("Masukkan modulus n: "))
            if pilihan == 1:
                print(f"Hasil (a + b) mod n = {mod_add(a, b, n)}")
            elif pilihan == 2:
                print(f"Hasil (a - b) mod n = {mod_sub(a, b, n)}")
            else:
                print(f"Hasil (a * b) mod n = {mod_mul(a, b, n)}")

        elif pilihan == 4:
            base = int(input("Masukkan basis: "))
            exp = int(input("Masukkan eksponen: "))
            n = int(input("Masukkan modulus n: "))
            print(f"Hasil (base^exp) mod n = {mod_exp(base, exp, n)}")

        elif pilihan == 5:
            a = int(input("Masukkan a: "))
            b = int(input("Masukkan b: "))
            print(f"GCD(a, b) = {gcd(a, b)}")

        elif pilihan == 6:
            a = int(input("Masukkan a: "))
            n = int(input("Masukkan modulus n: "))
            inv = modinv(a, n)
            if inv is None:
                print("Invers tidak ada (a dan n tidak relatif prima)")
            else:
                print(f"Invers dari {a} mod {n} = {inv}")

        elif pilihan == 7:
            a = int(input("Masukkan a: "))
            b = int(input("Masukkan b: "))
            n = int(input("Masukkan modulus n: "))
            x = discrete_log(a, b, n)
            if x is not None:
                print(f"Nilai x sehingga {a}^x ≡ {b} (mod {n}) adalah x = {x}")
            else:
                print("Tidak ditemukan solusi untuk x dalam rentang 0 hingga n-1.")

        else:
            print("Pilihan tidak valid! Silakan pilih antara 0-7.")

# Jalankan program
if __name__ == "__main__":
    main()


---

## 6. Hasil dan Pembahasan 
- Jelaskan apakah hasil sesuai ekspektasi.  
Semua hasil uji sesuai dengan ekspektasi.
Perhitungan modular bekerja benar untuk operasi penjumlahan, pengurangan, perkalian, dan eksponensiasi.
Fungsi gcd() dan modinv() juga berjalan sesuai teori matematika:

Invers modular hanya ada jika gcd(a, n) = 1.

Jika tidak relatif prima, fungsi mengembalikan None (pesan “invers tidak ada”).
---

## 7. Jawaban Pertanyaan
1. Apa peran aritmetika modular dalam kriptografi modern?
    Aritmetika modular adalah dasar utama dari hampir semua algoritma kriptografi modern, terutama pada kriptografi kunci publik seperti RSA, Diffie-Hellman, dan ECC (Elliptic Curve Cryptography).
Perannya antara lain:

A. Membatasi hasil operasi bilangan besar agar tetap dalam rentang tertentu (mod n).
B. Mendukung operasi yang sulit dibalik, seperti perpangkatan modular, yang menjadi dasar keamanan sistem kriptografi.
C. Menjamin efisiensi komputasi: meskipun menggunakan bilangan besar (ratusan atau ribuan bit), hasil tetap bisa dihitung dengan cepat melalui operasi modular yang efisien.

Kesimpulan:
Aritmetika modular menjaga agar operasi tetap efisien dan aman, sekaligus membuat proses dekripsi sulit dilakukan tanpa kunci yang benar.

2. Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
    Invers modular digunakan untuk mengembalikan hasil operasi eksponensial modular ke bentuk semula — proses yang esensial dalam dekripsi.
3. Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
	1. Tidak ada algoritma efisien (polinomial) yang diketahui untuk menyelesaikannya saat nbesar (misalnya ratusan atau ribuan bit).
	2. Pertumbuhan eksponensial waktu komputasi: semakin besar modulus n, waktu yang dibutuhkan tumbuh sangat cepat.
	3. Keterbatasan daya komputasi dan memori, terutama pada modulus besar (misalnya 2048-bit pada Diffie-Hellman atau ElGamal).
	4. Kompleksitas matematis tinggi: tidak bisa diselesaikan hanya dengan aritmetika biasa; butuh algoritma canggih seperti Baby-step Giant-step atau Index Calculus, yang tetap tidak praktis untuk modulus besar.

---

## 8. Kesimpulan
Berdasarkan hasil percobaan menggunakan program Aritmetika Modular dan Kriptografi Dasar, dapat disimpulkan bahwa:
1. Aritmetika modular merupakan dasar penting dalam matematika diskrit yang berfokus pada operasi bilangan dengan sisa hasil bagi (modulus). Semua operasi seperti penjumlahan, pengurangan, perkalian, dan eksponensiasi dapat dilakukan dengan benar di bawah sistem bilangan modulo.
2. Dari hasil uji, seluruh operasi modular menunjukkan hasil yang sesuai dengan teori matematika, di mana setiap hasil selalu berada dalam rentang 0 ≤ hasil < n (modulus).
3. Fungsi GCD (Greatest Common Divisor) dan invers modular memiliki peran penting dalam kriptografi, khususnya algoritma kunci publik seperti RSA. Invers modular hanya ada jika dua bilangan tersebut relatif prima (memiliki GCD = 1).
4. Percobaan juga menunjukkan bahwa logaritma diskrit sulit diselesaikan untuk modulus besar, karena perhitungannya bersifat satu arah dan memerlukan waktu sangat lama dengan metode brute force. Hal ini menjadi dasar keamanan pada banyak sistem kriptografi modern.
5. Secara keseluruhan, aritmetika modular terbukti menjadi fondasi utama dalam sistem keamanan digital, karena kemampuannya menjaga konsistensi perhitungan, mendukung pembentukan kunci publik–privat, dan mendasari operasi matematika dalam algoritma enkripsi.
---

## 9. Daftar Pustaka
1. Stallings, W. (2017). Cryptography and Network Security: Principles and Practice (7th ed.). Pearson Education.
2. Schneier, B. (1996). Applied Cryptography: Protocols, Algorithms, and Source Code in C (2nd ed.). John Wiley & Sons.
3. Paar, C., & Pelzl, J. (2010). Understanding Cryptography: A Textbook for Students and Practitioners. Springer.
4. Rosen, K. H. (2019). Discrete Mathematics and Its Applications (8th ed.). McGraw-Hill Education.
5. William, S. (2018). Matematika Diskrit untuk Ilmu Komputer. Penerbit Andi, Yogyakarta.
6. Menezes, A. J., van Oorschot, P. C., & Vanstone, S. A. (1996). Handbook of Applied Cryptography. CRC Press.
7. Kurniawan, D. (2021). Pengantar Kriptografi dan Keamanan Informasi. Penerbit Informatika, Bandung.
8. Wikipedia. (2024). Modular arithmetic. Retrieved from https://en.wikipedia.org/wiki/Modular_arithmetic

---

## 10. Commit Log
commit "week3-modmath: implementasi modmath gcd dan laporan "
Author: Fiqri N H <fiqrinur0801@gmail.com>
Date:   2025-10-30
```
