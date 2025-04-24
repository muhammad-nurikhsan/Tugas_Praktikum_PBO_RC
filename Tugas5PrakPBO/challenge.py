import tkinter as tk
from tkinter import messagebox

# Inisialisasi data
notes = {}

# Fungsi Tambah Catatan
def tambah_catatan():
    title = judul.get()
    content = isi_catatan.get("1.0", tk.END).strip()

    if not title or not content:
        messagebox.showerror("Error", "Judul dan isi catatan tidak boleh kosong.")
        return

    if title in notes:
        messagebox.showerror("Error", "Judul catatan sudah ada.")
        return

    notes[title] = content
    listbox_notes.insert(tk.END, title)
    judul.delete(0, tk.END)

    # Aktifkan Text widget untuk ditulis kembali
    isi_catatan.config(state=tk.NORMAL)
    isi_catatan.delete("1.0", tk.END)


# Fungsi Tampilkan Catatan
def tampilkan_catatan(event):
    selected = listbox_notes.curselection()
    if not selected:
        return

    title = listbox_notes.get(selected[0])
    content = notes.get(title, "")

    isi_catatan.config(state=tk.NORMAL)
    isi_catatan.delete("1.0", tk.END)
    isi_catatan.insert(tk.END, content)
    isi_catatan.config(state=tk.DISABLED)

# Fungsi Hapus Catatan
def hapus_catatan():
    selected = listbox_notes.curselection()
    if not selected:
        return

    title = listbox_notes.get(selected[0])

    confirm = messagebox.askyesno("Konfirmasi", f"Hapus catatan '{title}'?")
    if confirm:
        listbox_notes.delete(selected[0])
        notes.pop(title, None)
        isi_catatan.config(state=tk.NORMAL)
        isi_catatan.delete("1.0", tk.END)
        isi_catatan.config(state=tk.DISABLED)

# Fungsi Edit Catatan
def edit_catatan():
    selected = listbox_notes.curselection()
    if not selected:
        messagebox.showwarning("Peringatan", "Pilih catatan yang ingin diedit.")
        return
    title = listbox_notes.get(selected[0])
    content = notes.get(title, "")

    judul.delete(0, tk.END)
    judul.insert(0, title)

    isi_catatan.config(state=tk.NORMAL)
    isi_catatan.delete("1.0", tk.END)
    isi_catatan.insert(tk.END, content)

    # Hapus dari list dan dict sementara
    listbox_notes.delete(selected[0])
    notes.pop(title, None)


# Fungsi untuk keluar
def keluar():
    root.destroy()

# Fungsi Bantuan
def tentang():
    messagebox.showinfo("Tentang", "Aplikasi Catatan Harian\nVersi 1.0")

# Inisialisasi Window
root = tk.Tk()
root.title("Catatan Harian")

# Menu Bar
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Keluar", command=keluar)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Tentang", command=tentang)
menubar.add_cascade(label="Bantuan", menu=help_menu)

root.config(menu=menubar)

# Input Judul
tk.Label(root, text="Judul:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
judul = tk.Entry(root, width=40)
judul.grid(row=0, column=1, columnspan=2, padx=5, pady=5, sticky="we")

# Tombol Tambah dan Hapus
btn_add = tk.Button(root, text="Tambah Catatan", command=tambah_catatan)
btn_add.grid(row=1, column=1, padx=5, pady=5, sticky="we")

btn_delete = tk.Button(root, text="Hapus Catatan", command=hapus_catatan)
btn_delete.grid(row=1, column=2, padx=5, pady=5, sticky="we")

# Tombol Edit Catatan
btn_edit = tk.Button(root, text="Edit Catatan", command=edit_catatan)
btn_edit.grid(row=1, column=0, padx=5, pady=5, sticky="we")

# Listbox untuk Daftar Judul
listbox_notes = tk.Listbox(root, height=10)
listbox_notes.grid(row=2, column=0, padx=5, pady=5, sticky="ns")
listbox_notes.bind("<<ListboxSelect>>", tampilkan_catatan)

# Scrollbar untuk Listbox
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=2, column=0, sticky="nse")
listbox_notes.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_notes.yview)

# Text Area untuk Isi Catatan
isi_catatan = tk.Text(root, wrap="word")
isi_catatan.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="nsew")

# Konfigurasi Grid
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Jalankan Aplikasi
root.mainloop()