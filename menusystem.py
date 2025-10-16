# Menu dan Toolbar (Menu System)

import tkinter as tk
from tkinter import messagebox

class MenuToolbar:
    def __init__(self, root):
        self.root = root
        self.root.title("Menu System")
        self.root.geometry("400x300")
        
        self.buat_toolbar()
        self.buat_menubar()
        
    def buat_toolbar(self):
        # Frame untuk Toolbar
        toolbar = tk.Frame(self.root, bg='lightgray', bd=1, relief=tk.RAISED)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        
        # Tombol Toolbar
        
        # New
        btn_new = tk.Button(toolbar, text="New", 
                            command=self.file_new)
        btn_new.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Open
        btn_open = tk.Button(toolbar, text="Open", 
                             command=self.file_open)
        btn_open.pack(side=tk.LEFT, padx=2, pady=2)
        
        # Save
        btn_save = tk.Button(toolbar, text="Save", 
                             command=self.file_save)
        btn_save.pack(side=tk.LEFT, padx=2, pady=2)

        # Tambahkan Text Area
        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def buat_menubar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Menu File
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.file_new)
        file_menu.add_command(label="Open", command=self.file_open)
        file_menu.add_command(label="Save", command=self.file_save)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Menu Edit
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=self.edit_cut)
        edit_menu.add_command(label="Copy", command=self.edit_copy)
        edit_menu.add_command(label="Paste", command=self.edit_paste)
        edit_menu.add_separator()
        edit_menu.add_command(label="Delete All", command=self.file_new) # Menggunakan fungsi new untuk menghapus semua
        menubar.add_cascade(label="Edit", menu=edit_menu)

        # Menu Help
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.help_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    # --- FUNGSI FILE MENU ---
    
    def file_new(self):
        # Menghapus semua teks
        self.text_area.delete('1.0', tk.END)
        print("File -> New / Delete All")

    def file_open(self):
        # Untuk demo, hanya menampilkan pesan
        print("File -> Open")
        # Kode sebenarnya harus menggunakan filedialog.askopenfilename()

    def file_save(self):
        # Untuk demo, hanya menampilkan pesan
        print("File -> Save")
        # Kode sebenarnya harus menggunakan filedialog.asksaveasfilename()

    # --- FUNGSI EDIT MENU ---
    
    def edit_cut(self):
        try:
            # Mengambil teks yang diseleksi
            selected = self.text_area.selection_get()
            # Menyalin teks ke clipboard
            self.root.clipboard_clear()
            self.root.clipboard_append(selected)
            # Menghapus teks
            self.text_area.delete(tk.SEL_FIRST, tk.SEL_LAST)
        except tk.TclError:
            print("Tidak ada teks yang dipilih untuk Cut.")
            
    def edit_copy(self):
        try:
            selected = self.text_area.selection_get()
            # Menyalin teks ke clipboard
            self.root.clipboard_clear()
            self.root.clipboard_append(selected)
            # Mengubah lbl_info menjadi clear agar tidak mengganggu
            # self.root.clipboard_clear() # Ini tidak sesuai dengan yang di slide, tapi lebih benar.
            # Menggunakan print sesuai slide
            print("Teks disalin ke clipboard.")
        except tk.TclError:
            print("Tidak ada teks yang dipilih.")
            
    def edit_paste(self):
        try:
            # Menyisipkan teks dari clipboard pada posisi kursor
            text_to_insert = self.root.clipboard_get()
            self.text_area.insert(tk.INSERT, text_to_insert)
        except tk.TclError:
            # Jika clipboard kosong atau tidak bisa diakses
            print("Clipboard kosong atau terjadi error saat paste.")
        
    # --- FUNGSI HELP MENU ---

    def help_about(self):
        messagebox.showinfo("About", "Aplikasi Contoh Menu System")

    def jalankan(self):
        self.root.mainloop()

# Eksekusi program
if __name__ == "__main__":
    app_root = tk.Tk()
    app = MenuToolbar(app_root)
    app.jalankan()