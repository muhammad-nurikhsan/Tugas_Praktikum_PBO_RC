class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        task = task.strip()
        if not task:
            raise ValueError("Tugas tidak boleh kosong.")
        self.tasks.append(task)
        print(f"Tugas '{task}' berhasil ditambahkan!")

    def remove_task(self, task_number):
        if not self.tasks:
            raise IndexError("Daftar tugas masih kosong. Tidak ada yang bisa dihapus.")
        if task_number < 1 or task_number > len(self.tasks):
            raise IndexError(f"Tugas dengan nomor {task_number} tidak ditemukan.")
        removed_task = self.tasks.pop(task_number - 1)
        print(f"Tugas '{removed_task}' berhasil dihapus!")

    def show_tasks(self):
        if not self.tasks:
            print("Daftar tugas kosong.")
        else:
            print("\nDaftar Tugas:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")


def main():
    manager = TaskManager()
    while True:
        print("\nPilih opsi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Lihat daftar tugas")
        print("4. Keluar")

        try:
            pilihan = input("Masukkan pilihan (1/2/3/4): ").strip()
            if pilihan == "1":
                task = input("Masukkan tugas yang ingin ditambahkan: ")
                manager.add_task(task)
                
            elif pilihan == "2":
                task_number = int(input("Masukkan nomor tugas yang ingin dihapus: "))
                manager.remove_task(task_number)

            elif pilihan == "3":
                manager.show_tasks()

            elif pilihan == "4":
                print("Terima kasih! Jangan lupa kerjain tugas!!!")
                break

            else:
                print("Pilihan tidak valid. Silakan masukkan angka antara 1-4.")

        except ValueError:
            print("Input tidak valid. Pastikan Anda memasukkan angka yang benar.")

        except IndexError as e:
            print(f"Kesalahan: {e}")


if __name__ == "__main__":
    main()