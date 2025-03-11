# Muhammad Nurikhsan
# 123140057

# No 2
jumlah_siswa = int (input("Masukkan jumlah siswa: "))
data_siswa = {}

for i in range (1, jumlah_siswa + 1):
    nama = input(f"Masukkan nama siswa ke-{i}: ")
    nilai = int(input(f"Masukkan nilai untuk {nama}: "))
    data_siswa [nama] = nilai

print("\nDictionary = ", data_siswa)