class Animal:  # Kelas abstrak
    def __init__(self, name, species):
        self.name = name  
        self.__species = species  

    def get_species(self):  # Getter untuk mendapatkan spesies hewan
        return self.__species

    def make_sound(self):  # Metode abstrak
        raise NotImplementedError("Subkelas harus mengimplementasikan metode ini.")


class mamalia(Animal):  # Kelas Mamalia
    def __init__(self, name):
        super().__init__(name, "Mamalia")

    def make_sound(self):
        print(f"{self.name} mengeluarkan suara khas mamalia.\n")


class burung(Animal):  # Kelas Burung
    def __init__(self, name):
        super().__init__(name, "Burung")

    def make_sound(self):
        print(f"{self.name} berkicau dengan merdu.\n")


class reptil(Animal):  # Kelas Reptil
    def __init__(self, name):
        super().__init__(name, "Reptil")

    def make_sound(self):
        print(f"{self.name} mendesis dengan suara pelan.\n")


class amfibi(Animal):  # Kelas Amfibi
    def __init__(self, name):
        super().__init__(name, "Amfibi")

    def make_sound(self):
        print(f"{self.name} mengeluarkan suara khas amfibi, seperti kodok yang berbunyi 'krook'.\n")


class insekta(Animal):  # Kelas Serangga
    def __init__(self, name):
        super().__init__(name, "Serangga")

    def make_sound(self):
        print(f"{self.name} mendengungkan suara khas serangga.\n")


# Exception Handling dan Duck Typing
def animal_interaction(animal):
    try:
        print(f"{animal.name} adalah seekor {animal.get_species()}.")
        animal.make_sound()
    except AttributeError as e:
        print(f"Error: {e}")


# Inisialisasi objek
lion = mamalia("Singa")
dolphin = mamalia("Lumba-lumba")
parrot = burung("Beo")
cobra = reptil("Kobra")
crocodile = reptil("Buaya")
frog = amfibi("Katak")
bee = insekta("Lebah")
grasshopper = insekta("Belalang")

print("===================")
animal_interaction(lion)
animal_interaction(dolphin)
animal_interaction(parrot)
animal_interaction(cobra)
animal_interaction(crocodile)
animal_interaction(frog)
animal_interaction(bee)
animal_interaction(grasshopper)