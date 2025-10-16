# Event Handling (Event Binding)

import tkinter as tk

class EventHandling:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Handling")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        self.setup_events()
        
    def setup_events(self):
        # ... (Kode setup frame dan binding mouse dihilangkan untuk fokus)

        # Frame untuk demo interaksi mouse
        self.frame = tk.Frame(self.root, width=300, height=200,
                              bg="lightblue", relief=tk.RIDGE, bd=2)
        self.frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        self.frame.pack_propagate(False) 
        
        # Binding event mouse ke frame
        self.frame.bind("<Button-1>", self.mouse_click)
        self.frame.bind("<Double-Button-1>", self.mouse_double_click)
        self.frame.bind("<B1-Motion>", self.mouse_drag)
        self.frame.bind("<Enter>", self.mouse_enter)
        self.frame.bind("<Leave>", self.mouse_leave)
        
        # Binding event keyboard ke root - BAGIAN YANG DIPERBAIKI
        self.root.bind("<Key>", self.key_pressed) # Ganti "<Keypress>" menjadi "<Key>"
        
        # Label untuk menampilkan informasi event
        self.lbl_info = tk.Label(
            self.root,
            text="Event akan ditampilkan di sini",
            font=('Arial', 10),
            bg='white',
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.lbl_info.pack(fill=tk.X, padx=20, pady=5)
        
    # ... (Semua definisi fungsi mouse tetap sama)
    def mouse_click(self, event):
        self.lbl_info.config(text=f"Klik di koordinat: ({event.x}, {event.y})")
        
    def mouse_double_click(self, event):
        self.lbl_info.config(text=f"Double click di: ({event.x}, {event.y})")
        
    def mouse_drag(self, event):
        self.lbl_info.config(text=f"Drag ke: ({event.x}, {event.y})")
        
    def mouse_enter(self, event):
        self.lbl_info.config(text="Mouse masuk area biru")
        
    def mouse_leave(self, event):
        self.lbl_info.config(text="Mouse keluar dari area biru")

    def key_pressed(self, event):
        # event.char adalah karakter yang ditekan
        self.lbl_info.config(text=f"Tombol ditekan: {event.char}")
        
    def jalankan(self):
        self.root.mainloop()

# Eksekusi program
if __name__ == "__main__":
    app_root = tk.Tk()
    app = EventHandling(app_root)
    app.jalankan()