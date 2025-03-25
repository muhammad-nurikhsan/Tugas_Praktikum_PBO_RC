import math 

def hitung_akar():
    while True:
        try:
            angka = float(input("Masukkan angka: "))

            if angka < 0:
                print("Input tidak valid. Harap masukkan angka positif.")
                continue

            akar = math.sqrt(angka)  # Menggunakan fungsi sqrt()
            print(f"Akar kuadrat dari {angka} adalah {akar:.2f}")
            break

        except ValueError:
            print("Input tidak valid. Harap masukkan angka yang valid.")

hitung_akar()