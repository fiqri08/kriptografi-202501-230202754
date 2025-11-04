import math

def hitung_entropy(teks):
    frekuensi = {}
    for karakter in teks:
        if karakter not in frekuensi:
            frekuensi[karakter] = 0
        frekuensi[karakter] += 1

    total = len(teks)
    entropy = 0

    for count in frekuensi.values():
        probabilitas = count / total
        entropy -= probabilitas * math.log2(probabilitas)

    return entropy

def hitung_unicity_distance(entropy_per_char, key_space):
    return key_space / entropy_per_char

# === INPUT DARI USER ===
ciphertext = input("Masukkan ciphertext / teks yang akan dianalisis: ")

# Hitung entropy
entropy = hitung_entropy(ciphertext)

# Misal keyspace untuk kunci Caesar adalah log2(26) (kunci 0-25)
key_space = math.log2(26)

unicity = hitung_unicity_distance(entropy, key_space)

print("\n=== HASIL ANALISIS ===")
print(f"Entropy Teks       : {entropy:.4f} bit per karakter")
print(f"Key Space (log2)   : {key_space:.4f} bit")
print(f"Unicity Distance   : {unicity:.4f} karakter")
