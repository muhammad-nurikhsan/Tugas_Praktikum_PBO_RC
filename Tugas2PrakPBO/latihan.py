# Kelas Induk: Kendaraan
class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum
    
    def info_kendaraan(self):
        return (
            f"Jenis Kendaraan: {self.jenis}\n"
            f"Kecepatan Maksimum: {self.kecepatan_maksimum} km/jam"
        )
    
    def bergerak(self):
        return "Kendaraan sedang bergerak..."

# Kelas Turunan: Mobil
class Mobil(Kendaraan):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu
    
    def info_mobil(self):
        return (
            self.info_kendaraan() + "\n" +
            f"Merk: {self.merk}\n"
            f"Jumlah Pintu: {self.jumlah_pintu}"
        )
    
    def bunyikan_klakson(self):
        return "Beep! Beep! Mobil membunyikan klakson!"

# Kelas Turunan: MobilSport
class MobilSport(Mobil):
    def __init__(self, jenis, kecepatan_maksimum, merk, jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis, kecepatan_maksimum, merk, jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga
    
    def get_tenaga_kuda(self):
        return self.__tenaga_kuda
    
    def set_tenaga_kuda(self, value):
        if value > 0:
            self.__tenaga_kuda = value
        else:
            print("Tenaga kuda harus bernilai positif!")
    
    def get_harga(self):
        return self.__harga
    
    def set_harga(self, value):
        if value > 0:
            self.__harga = value
        else:
            print("Harga harus bernilai positif!")
    
    def info_mobil_sport(self):
        self.info_mobil()
        return f"Tenaga Kuda: {self.__tenaga_kuda} HP"
        return f"Harga: Rp {self.__harga} juta"
    
    def mode_balap(self):
        return "Mobil sport masuk ke mode balap! Kecepatan maksimum meningkat!"

# Contoh Penggunaan
mobil_sport = MobilSport("Darat", 350, "Ferrari", 2, 700, 15000)

# Tampilkan info pakai print kalau mau tampilkan
print(mobil_sport.info_mobil_sport())
print(mobil_sport.mode_balap())

# Getter dan Setter
print("Tenaga Kuda Awal:", mobil_sport.get_tenaga_kuda())
mobil_sport.set_tenaga_kuda(800)
print("Tenaga Kuda Setelah Diubah:", mobil_sport.get_tenaga_kuda())
