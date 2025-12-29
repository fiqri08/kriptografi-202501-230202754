from shamir_mnemonic import generate_mnemonics, combine_mnemonics

# Rahasia yang ingin dibagi
secret = b"KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = generate_mnemonics(
    group_threshold=1,
    groups=[(3, 5)],
    master_secret=secret
)

print("Shares:")
for s in shares[0]:
    print(s)

# Rekonstruksi rahasia dari 3 shares
recovered = combine_mnemonics(shares[0][:3])
print("Recovered secret:", recovered.decode())