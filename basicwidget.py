# Widget-widget Tkinter (Basic Widgets)

import tkinter as tk
from tkinter import messagebox # Pastikan ini diimpor jika menggunakan messagebox

class WidgetsAplikasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Widget Demo")
        self.root.geometry("300x150")
        self.root.resizable(False, False)
        self.setup_widgets()
        
    def setup_widgets(self):
        # 1. Widget Label (Output Teks)
        self.label_control = tk.Label(self.root, 
                                      text="Control Label", 
                                      font=("Arial", 10, "bold"), 
                                      fg='blue', 
                                      bg='yellow')
        self.label_control.pack(pady=10)

        # 2. Widget Entry (Input Teks)
        self.entry_input = tk.Entry(self.root, width=20, bd=3)
        self.entry_input.insert(0, "Teks default") # Mengatur teks awal
        self.entry_input.pack(pady=5)
        
        # 3. Widget Button (Tombol Aksi)
        self.button_aksi = tk.Button(self.root, 
                                     text="Operasikan Label", 
                                     width=15, 
                                     command=self.update_label)
        self.button_aksi.pack(pady=5)

    def update_label(self):
        # Ambil teks dari Entry
        teks_baru = self.entry_input.get()
        
        # Cek apakah Entry kosong
        if not teks_baru:
            messagebox.showwarning("Peringatan", "Input tidak boleh kosong!")
        else:
            # Update teks pada Label
            self.label_control.config(text=teks_baru)
            
    def jalankan(self):
        self.root.mainloop()

# Eksekusi program
if __name__ == "__main__":
    app_root = tk.Tk()
    app = WidgetsAplikasi(app_root)
    app.jalankan()