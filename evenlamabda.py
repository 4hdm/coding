# Event Handling (Event dengan Lambda)

import tkinter as tk

class EventLambda:
    def __init__(self, root):
        self.root = root
        self.root.title("Event dengan Lambda")
        self.root.geometry("300x250")
        self.root.resizable(False, False)
        
        # Inisialisasi variabel status dan counter
        self.counter = 0 
        self.setup_buttons()

    def setup_buttons(self):
        # Frame untuk tombol
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        # Label untuk menampilkan status
        self.lbl_status = tk.Label(
            self.root,
            text="Belum ada button diklik",
            font=('Arial', 10),
            bg='white',
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.lbl_status.pack(fill=tk.X, padx=20, pady=10)

        # Button dengan fungsi lambda
        for i in range(5):
            button_num = i + 1  # Nomor button 1 sampai 5
            btn = tk.Button(
                frame_buttons,
                text=f"Button {button_num}",
                width=15,
                # Menggunakan lambda untuk meneruskan argumen (nomor button) ke fungsi
                command=lambda x=button_num: self.button_clicked(x)
            )
            btn.pack(pady=5)
            
    def button_clicked(self, button_num):
        self.counter += 1
        self.lbl_status.config(
            text=f"Button {button_num} diklik! Total klik: {self.counter}"
        )

    def jalankan(self):
        self.root.mainloop()

# Eksekusi program
if __name__ == "__main__":
    app_root = tk.Tk()
    app = EventLambda(app_root)
    app.jalankan()