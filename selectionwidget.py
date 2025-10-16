# Widget-widget Tkinter (Selection Widgets)

import tkinter as tk
from tkinter import messagebox

class WidgetSeleksi:
    def __init__(self, root):
        self.root = root
        self.root.title("Widget Seleksi")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.setup_widgets()
        
    def setup_widgets(self):
        
        # 1. Checkbutton
        self.var_check = tk.BooleanVar()
        self.var_check.set(False) # Set nilai awal False
        
        self.chk_box = tk.Checkbutton(
            self.root,
            text="Setuju dengan syarat",
            variable=self.var_check,
            command=self.check_changed,
            font=('Arial', 10)
        )
        self.chk_box.pack(pady=5, anchor=tk.W, padx=10)

        # -----------------------------------------------------

        # 2. Radiobuttons
        
        # Frame untuk Radiobuttons
        frame_radio = tk.LabelFrame(self.root, text="Pilih bahasa", padx=10, pady=5)
        frame_radio.pack(pady=10, fill=tk.X, padx=10)
        
        self.var_radio = tk.StringVar(value="python") # Set nilai awal 'python'
        
        bahasa = ["Python", "Java", "JavaScript"]
        for bhs in bahasa:
            rb = tk.Radiobutton(
                frame_radio,
                text=bhs,
                variable=self.var_radio,
                value=bhs.lower(), # Gunakan lowercase untuk value
                font=('Arial', 10)
            )
            rb.pack(anchor=tk.W)

        # -----------------------------------------------------

        # 3. Scale Widget
        self.var_scale = tk.DoubleVar()
        self.var_scale.set(50) # Set nilai awal 50
        
        self.scale = tk.Scale(
            self.root,
            from_=0,
            to=100,
            orient=tk.HORIZONTAL,
            variable=self.var_scale,
            label='Volume',
            font=('Arial', 10)
        )
        self.scale.pack(pady=10, fill=tk.X, padx=10)
        
        # -----------------------------------------------------

        # 4. Tombol untuk menampilkan hasil seleksi
        btn_submit = tk.Button(
            self.root,
            text="Tampilkan Pilihan",
            command=self.tampilkan_hasil,
            font=('Arial', 10, 'bold'),
            bg="#ddeeff"
        )
        btn_submit.pack(pady=10)
        
    def check_changed(self):
        # Contoh sederhana fungsi command untuk Checkbutton
        status = "Setuju" if self.var_check.get() else "Belum setuju"
        print(f"Checkbutton: {status}")

    def tampilkan_hasil(self):
        # Validasi Checkbutton
        if not self.var_check.get():
            messagebox.showwarning("Peringatan", "Anda harus menyetujui syarat terlebih dahulu!")
            return
            
        # Ambil nilai-nilai dari widget
        bahasa = self.var_radio.get().capitalize()
        volume = int(self.var_scale.get())
        
        # Tampilkan hasil
        messagebox.showinfo(
            "Hasil Seleksi", 
            f"Bahasa: {bahasa}\nVolume: {volume}"
        )

    def jalankan(self):
        self.root.mainloop()

# Eksekusi program
if __name__ == "__main__":
    app_root = tk.Tk()
    app = WidgetSeleksi(app_root)
    app.jalankan()