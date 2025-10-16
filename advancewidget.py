# Widget-widget Tkinter (Advanced Widgets)

import tkinter as tk
from tkinter import messagebox

class WidgetLanjutan:
    def __init__(self, root):
        self.root = root
        self.root.title("Widget Lanjutan")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.setup_widgets()

    def setup_widgets(self):
        # Frame utama
        frame_main = tk.Frame(self.root)
        frame_main.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # 1. Text Widget dan Scrollbar
        
        # Frame untuk Text dan Scrollbar
        frame_text = tk.Frame(frame_main)
        frame_text.pack(fill=tk.BOTH, expand=True)
        
        # Text widget (multi-line)
        self.text_area = tk.Text(frame_text,
                                 height=8,
                                 width=40,
                                 wrap=tk.WORD)
        self.text_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar untuk Text Widget
        scrollbar = tk.Scrollbar(frame_text,
                                 command=self.text_area.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_area.config(yscrollcommand=scrollbar.set)
        
        # 2. Listbox
        listbox = tk.Listbox(frame_main, height=4)
        for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
            listbox.insert(tk.END, item)
        listbox.pack(pady=5, fill=tk.X)
        
        # 3. Combobox (dari ttk)
        # Perlu import 'ttk' secara terpisah jika digunakan (misal: from tkinter import ttk)
        # Asumsi untuk contoh ini, kita menggunakan widget dasar atau menganggap ttk sudah diimpor.
        # Karena di slide tidak ada 'import ttk', kita akan gunakan tk.Label untuk demonstrasi placeholder Combobox
        # ATAU, yang lebih akurat dengan konteks combobox:
        
        # NOTE: Agar kode berjalan, kita harus import ttk
        try:
            from tkinter import ttk
            self.combo = ttk.Combobox(
                frame_main,
                values=["Pilihan 1", "Pilihan 2", "Pilihan 3"],
                state='readonly'
            )
            self.combo.set("Pilih salah satu")
            self.combo.pack(pady=5, fill=tk.X)
        except ImportError:
            # Fallback jika ttk tidak tersedia (walaupun seharusnya ada di Python standar)
            tk.Label(frame_main, text="Combobox Placeholder (ttk missing)").pack(pady=5)
        
        
        # 4. Tombol interaksi
        btn_show = tk.Button(
            frame_main,
            text="Tampilkan Pilihan",
            command=self.tampilkan_pilihan
        )
        btn_show.pack(pady=10)

    def tampilkan_pilihan(self):
        # Asumsi self.combo adalah ttk.Combobox
        try:
            pilihan = self.combo.get()
            if pilihan == "Pilih salah satu":
                messagebox.showwarning("Peringatan", "Silakan pilih salah satu opsi!")
            else:
                messagebox.showinfo("Pilihan Anda", f"Anda memilih: {pilihan}")
        except AttributeError:
            # Handle jika self.combo tidak terinisialisasi (karena ttk missing)
            messagebox.showerror("Error", "Widget Combobox tidak ditemukan.")

    def jalankan(self):
        self.root.mainloop()

# Eksekusi program
if __name__ == "__main__":
    # Penting: Tambahkan import ttk di atas jika Combobox (ttk) digunakan
    from tkinter import ttk 
    
    app_root = tk.Tk()
    app = WidgetLanjutan(app_root)
    app.jalankan()