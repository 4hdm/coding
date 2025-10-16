# Object-Oriented GUI Programming

import tkinter as tk
from tkinter import messagebox

class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # Variabel ekspresi dan tampilan
        self.expression = ""
        self.input_var = tk.StringVar(value="0") # Tampilan awal "0"
        
        self.setup_gui()
        
    def setup_gui(self):
        # Frame utama
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Tampilan (Display)
        display_frame = self.buat_display_frame(main_frame)
        display_frame.pack(pady=10)

        # Frame tombol
        button_frame = self.buat_button_frame(main_frame)
        button_frame.pack(pady=10)
        
    def buat_display_frame(self, root_frame):
        frame = tk.Frame(root_frame)
        
        # Entry - Display input/output
        entry = tk.Entry(
            frame, 
            textvariable=self.input_var, 
            font=('Arial', 20, 'bold'),
            fg='black', 
            bg='white',
            bd=5, 
            relief=tk.SUNKEN, 
            state='readonly', # Agar hanya bisa diubah oleh program
            justify=tk.RIGHT
        )
        entry.pack(fill=tk.X, padx=10, pady=10)
        
        return frame

    def buat_button_frame(self, root_frame):
        frame = tk.Frame(root_frame)
        
        # Layout tombol (baris x kolom)
        # C: Clear, CE: Clear Entry
        layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['CE', '=']
        ]

        # Iterasi untuk membuat tombol
        for row, row_in_enumerate in enumerate(layout):
            for col, text in enumerate(row_in_enumerate):
                # Tentukan warna
                if text == '=':
                    bg_color = 'orange'
                    command = lambda x=text: self.hitung_hasil()
                elif text in ('C', 'CE'):
                    bg_color = 'red'
                    command = lambda x=text: self.clear_input(x)
                elif text in ('+', '-', '*', '/'):
                    bg_color = 'gray'
                    command = lambda x=text: self.tekan_input(x)
                else:
                    bg_color = 'lightgray'
                    command = lambda x=text: self.tekan_input(x)
                
                # Buat Tombol
                btn = tk.Button(
                    frame,
                    text=text,
                    fg='black',
                    bg=bg_color,
                    command=command,
                    height=2,
                    width=6,
                    font=('Arial', 12)
                )
                
                # Pengaturan grid
                if text == 'CE':
                    # Tombol 'CE' mengambil 2 kolom (columnspan=2)
                    btn.grid(row=row, column=col, columnspan=2, padx=3, pady=3, sticky="nsew")
                elif text == '=':
                    # Tombol '=' mengambil 2 kolom
                    # Karena 'CE' sudah mengambil col 0 dan 1, '=' harus dimulai dari col 2
                    # Di layout, 'CE' dan '=' ada di baris yang sama.
                    # Kita harus modifikasi grid untuk baris terakhir:
                    # Di baris terakhir layout hanya ada 2 elemen. Kita buat 'CE' ambil 2 kolom, dan '=' ambil 2 kolom.
                    # Jadi: 'CE' (col 0, span 2), '=' (col 2, span 2).
                    
                    # Cek jika baris ini adalah baris terakhir (baris 4)
                    if row == len(layout) - 1 and text == '=':
                        btn.grid(row=row, column=col + 1, columnspan=2, padx=3, pady=3, sticky="nsew")
                    else:
                        btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
                else:
                    # Semua tombol lainnya (1 kolom)
                    btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")
        
        # Konfigurasi grid agar tombol menyesuaikan ukuran frame
        for i in range(4):
            frame.grid_columnconfigure(i, weight=1)
        for i in range(len(layout)):
            frame.grid_rowconfigure(i, weight=1)
            
        return frame

    def tekan_input(self, value):
        # Menambahkan nilai (angka/operator) ke ekspresi
        self.expression += str(value)
        self.input_var.set(self.expression)

    def hitung_hasil(self):
        try:
            # Menggunakan eval untuk menghitung ekspresi
            result = str(eval(self.expression))
            self.input_var.set(result)
            self.expression = result # Mengatur hasil sebagai ekspresi baru
        except ZeroDivisionError:
            messagebox.showerror("Kesalahan", "Pembagian dengan nol!")
            self.expression = ""
            self.input_var.set("Error")
        except:
            messagebox.showerror("Kesalahan", "Ekspresi tidak valid!")
            self.expression = ""
            self.input_var.set("Error")

    def clear_input(self, clear_type):
        if clear_type == 'C':
            # Clear total (mengatur ulang semua)
            self.expression = ""
            self.input_var.set("0")
        elif clear_type == 'CE':
            # Clear Entry (menghapus karakter terakhir)
            self.expression = self.expression[:-1]
            if not self.expression:
                 self.input_var.set("0")
            else:
                 self.input_var.set(self.expression)

    def jalankan(self):
        self.root.mainloop()

# Eksekusi program
if __name__ == "__main__":
    app_root = tk.Tk()
    calculator = Kalkulator(app_root)
    calculator.jalankan()