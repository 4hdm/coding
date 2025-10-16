import tkinter as tk
from tkinter import ttk
# Struktur dasar aplikasi Tkinter
class AplikasiDasar:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aplikasi Saya")
        self.root.geometry("400x300")
    def jalankan(self):
        self.root.mainloop()
# Instance dan eksekusi
app = AplikasiDasar()
app.jalankan()