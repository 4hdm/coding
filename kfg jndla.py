import tkinter as tk
from tkinter import messagebox

class WindowDasar:
    def __init__(self):
        # Membuat objek jendela utama
        self.root = tk.Tk()
        self.setup_ui()

        # Menjalankan loop utama agar jendela tampil
        self.root.mainloop()

    def setup_ui(self):
        """Konfigurasi jendela utama"""
        self.root.title("Aplikasi GUI")
        self.root.geometry("600x400")
        self.root.resizable(False, False)  # Mencegah ukuran diubah

        # Label sambutan
        label = tk.Label(
            self.root,
            text="Selamat Datang!",
            font=("Arial", 16),
            fg="blue"
        )
        label.pack(pady=20)

        # Tombol interaktif
        button = tk.Button(
            self.root,
            text="Klik Saya!",
            font=("Arial", 12),
            command=self.on_button_click  # Panggil fungsi saat diklik
        )
        button.pack(pady=10)

    def on_button_click(self):
        """Event handler saat tombol ditekan"""
        messagebox.showinfo("Informasi", "Halo! Tombol telah diklik 😊")

# Jalankan program
if __name__ == "__main__":
    WindowDasar()

import tkinter as tk
class LayoutPack:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pack Layout")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.buat_widget()
    def buat_widget(self):# Frame utama sebagai container
        frame_utama = tk.Frame(self.root, bg="lightgray", bd=2, relief=tk.SUNKEN)
        frame_utama.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)    # Tombol-tombol dengan layout pack
        btn1 = tk.Button(frame_utama, text="Button 1", font=("Arial", 12), bg="#d0e1f9")
        btn1.pack(side=tk.TOP, fill=tk.X, pady=5)
        btn2 = tk.Button(frame_utama, text="Button 2", font=("Arial", 12), bg="#f9d0d0")
        btn2.pack(side=tk.TOP, fill=tk.X, pady=5)
        btn3 = tk.Button(frame_utama, text="Button 3", font=("Arial", 12), bg="#d0f9d6")
        btn3.pack(side=tk.BOTTOM, fill=tk.X, pady=5)
    def jalankan(self):
        self.root.mainloop()
    
# Eksekusi program
if __name__ == "__main__":
    app = LayoutPack()
    app.jalankan()