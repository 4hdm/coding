# Dialog dan Message Box (Standard Dialogs)

import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, colorchooser

class DialogContoh:
    def __init__(self, root):
        self.root = root
        self.root.title("Contoh Dialog")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.setup_buttons()
        
    def setup_buttons(self):
        # Frame untuk tombol
        frame_main = tk.Frame(self.root, padx=10, pady=10)
        frame_main.pack(fill=tk.BOTH, expand=True)

        # 1. Message Boxes
        
        # Info
        btn_info = tk.Button(frame_main, text="Info", width=25,
                             command=self.show_info)
        btn_info.pack(pady=3)
        
        # Warning
        btn_warning = tk.Button(frame_main, text="Warning", width=25,
                                command=self.show_warning)
        btn_warning.pack(pady=3)
        
        # Error
        btn_error = tk.Button(frame_main, text="Error", width=25,
                              command=self.show_error)
        btn_error.pack(pady=3)
                              
        # Question
        btn_question = tk.Button(frame_main, text="Question", width=25,
                                 command=self.show_question)
        btn_question.pack(pady=3)
        
        # 2. File Dialogs
        
        # Open File
        btn_open = tk.Button(frame_main, text="Open File", width=25,
                             command=self.open_dialog)
        btn_open.pack(pady=3)
        
        # Save File
        btn_save = tk.Button(frame_main, text="Save File", width=25,
                             command=self.save_dialog)
        btn_save.pack(pady=3)
        
        # 3. Other Dialogs
        
        # Input Dialog
        btn_input = tk.Button(frame_main, text="Input Dialog", width=25,
                              command=self.input_dialog)
        btn_input.pack(pady=3)
        
        # Color Chooser
        btn_color = tk.Button(frame_main, text="Color Chooser", width=25,
                              command=self.choose_color)
        btn_color.pack(pady=3)
                              
    # --- MESSAGE BOX FUNCTIONS ---
    def show_info(self):
        messagebox.showinfo("Informasi", "Ini adalah pesan informasi.")

    def show_warning(self):
        messagebox.showwarning("Peringatan", "Ini adalah pesan peringatan.")

    def show_error(self):
        messagebox.showerror("Kesalahan", "Ini adalah pesan kesalahan.")

    def show_question(self):
        result = messagebox.askquestion("Pertanyaan", "Apakah Anda yakin?")
        
        # Menampilkan hasil dari askquestion
        if result == "yes":
            messagebox.showinfo("Jawaban", "Anda memilih: Ya")
        else:
            messagebox.showinfo("Jawaban", "Anda memilih: Tidak")
            
    # --- FILE DIALOG FUNCTIONS ---
    def open_dialog(self):
        file_path = filedialog.askopenfilename(
            title="Pilih File",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if file_path:
            messagebox.showinfo("File Dipilih", f"Path: {file_path}")

    def save_dialog(self):
        file_path = filedialog.asksaveasfilename(
            title="Simpan File",
            defaultextension=".txt",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if file_path:
            messagebox.showinfo("File Disimpan", f"Path: {file_path}")

    # --- OTHER DIALOG FUNCTIONS ---
    def input_dialog(self):
        result = simpledialog.askstring("Input", "Masukkan nama Anda:")
        
        if result:
            messagebox.showinfo("Nama Anda", f"Halo, {result}!")

    def choose_color(self):
        # Mengembalikan tuple: (('rgb_r', 'rgb_g', 'rgb_b'), '#hexcode')
        color = colorchooser.askcolor(title="Pilih warna") 
        
        # Cek jika pengguna memilih warna (tidak menekan 'Cancel')
        if color[1] is not None:
            messagebox.showinfo("Warna Dipilih", f"Kode warna (color[1]): {color[1]}")
            # Opsional: ubah latar belakang root menjadi warna yang dipilih
            # self.root.config(bg=color[1])
            
    def jalankan(self):
        self.root.mainloop()

# Eksekusi program
if __name__ == "__main__":
    app_root = tk.Tk()
    app = DialogContoh(app_root)
    app.jalankan()