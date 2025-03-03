# Muhammad Nurikhsan
# 123140057

# No 3
nama = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
resolusi = input("Masukkan Resolusi di Tahun ini: ")

with open("Me.txt", "w") as file:
    file.write(f"Nama: {nama}\n")
    file.write(f"NIM: {nim}\n")
    file.write(f"Resolusi: {resolusi}\n")

print("File Me.txt telah berhasil dibuat!")