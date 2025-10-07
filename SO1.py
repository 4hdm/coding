import threading

# Fungsi untuk thread pertama (1–50)
def cetak_1_50():
    hasil = " ".join(str(i) for i in range(1, 51))
    print(f"Thread 1: {hasil}")

# Fungsi untuk thread kedua (51–100)
def cetak_51_100():
    hasil = " ".join(str(i) for i in range(51, 101))
    print(f"Thread 2: {hasil}")

# Membuat dua thread
t1 = threading.Thread(target=cetak_1_50)
t2 = threading.Thread(target=cetak_51_100)

# Menjalankan kedua thread
t1.start()
t2.start()

# Menunggu kedua thread selesai
t1.join()
t2.join()

print("Selesai menjalankan kedua thread.")
