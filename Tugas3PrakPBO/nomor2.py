class Parent:
    def __init__(self, blood_type):
        self.blood_type = blood_type

class Father(Parent):
    pass

class Mother(Parent):
    pass

class Child:
    def __init__(self, father, mother):
        self.blood_type = self.penentuan_goldar(father.blood_type, mother.blood_type)
    
    # Metode untuk menentukan golongan darah anak berdasarkan golongan darah ayah dan ibu
    def penentuan_goldar(self, father_blood, mother_blood):
        kombinasi_golongan_darah = {
            ("A", "A"):"A", ("A", "O"):"A", ("O", "A"):"A", 
            ("A", "B"):"AB", ("B", "A"):"AB", ("A", "AB"):"A, AB", 
            ("AB", "A"):"A, AB", ("B", "B"):"B", ("B", "O"):"B", 
            ("O", "B"):"B", ("B", "AB"):"B, AB", ("AB", "B"):"B, AB",
            ("O", "O"):"O", ("AB", "O"):"A, B", ("O", "AB"):"A, B",
            ("AB", "AB"):"A, B, AB"
        }
        return kombinasi_golongan_darah.get((father_blood, mother_blood), "unknown")
    
    def __str__(self):
        return f"Kemunginan golongan darah anak adalah : {self.blood_type}"

# Input dari pengguna
father_blood = input("Masukkan golongan darah ayah (A, B, O, AB) : ")
mother_blood = input("Masukkan golongan darah ibu (A, B, O, AB) : ")

# Validasi input dari pengguna
jenis_golongan_darah = {"A", "B", "O", "AB"}

# Jika input tidak valid, tampilkan pesan kesalahan
if father_blood not in jenis_golongan_darah or mother_blood not in jenis_golongan_darah:
    print("Golongan darah yang dimasukkan tidak valid. Gunakan A, B, O, atau AB.")
else:
    child = Child(Father(father_blood), Mother(mother_blood))
    print(child)