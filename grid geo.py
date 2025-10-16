# Layout Management (Grid Geometry Manager)

import tkinter as tk
from tkinter import messagebox

class LayoutGrid:
    def __init__(self, root):
        self.root = root
        self.root.title("Form Login - Grid Layout")
        self.root.geometry("300x150")
        self.root.resizable(False, False)
        self.buat_form_login()
        
    def buat_form_login(self):
        # Label dan Entry untuk Username
        lbl_user = tk.Label(self.root, text="Username:", font=("Arial", 10))
        lbl_user.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        
        self.entry_user = tk.Entry(self.root, width=25)
        self.entry_user.grid(row=0, column=1, padx=10, pady=5)
        
        # Label dan Entry untuk Password
        lbl_pass = tk.Label(self.root, text="Password:", font=("Arial", 10))
        lbl_pass.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        
        self.entry_pass = tk.Entry(self.root, width=25, show="*")
        self.entry_pass.grid(row=1, column=1, padx=10, pady=5)
        
        # Frame untuk tombol
        frame_buttons = tk.Frame(self.root)
        frame_buttons.grid(row=2, column=0, columnspan=2, pady=10)
        
        btn_login = tk.Button(frame_buttons, text="Login", width=10, command=self.aksi_login)
        btn_login.pack(side=tk.LEFT, padx=5)
        
        btn_cancel = tk.Button(frame_buttons, text="Cancel", width=10, command=self.root.quit)
        btn_cancel.pack(side=tk.LEFT, padx=5)
        
    def aksi_login(self):
        username = self.entry_user.get()
        password = self.entry_pass.get()
        
        if username == "" or password == "":
            messagebox.showwarning("Peringatan", "Username dan Password harus diisi!")
        else:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")

    def jalankan(self):
        self.root.mainloop()

# Eksekusi program
if __name__ == "__main__":
    app_root = tk.Tk()
    app = LayoutGrid(app_root)
    app.jalankan()