# ==============================
# Sistem E-Commerce Sederhana
# ==============================

class Pelanggan:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email
        self.keranjang = Keranjang()   # composition → setiap pelanggan punya keranjang sendiri
        self.riwayat_pesanan = []      # menyimpan daftar pesanan

    def buat_pesanan(self):
        # buat pesanan dari isi keranjang
        pesanan = Pesanan(self)
        for item in self.keranjang.item:
            pesanan.tambah_item(item.produk, item.jumlah)
        self.riwayat_pesanan.append(pesanan)
        self.keranjang = Keranjang()   # kosongkan keranjang setelah buat pesanan
        return pesanan


class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok


class Keranjang:
    def __init__(self):
        self.item = []   # list ItemPesanan

    def tambah_produk(self, produk, jumlah):
        if produk.stok >= jumlah:
            self.item.append(ItemPesanan(produk, jumlah))
            produk.stok -= jumlah  # stok berkurang setelah masuk keranjang
        else:
            print(f"Stok {produk.nama} tidak cukup!")


class Pesanan:
    def __init__(self, pelanggan):
        self.pelanggan = pelanggan
        self.item = []  # list ItemPesanan

    def tambah_item(self, produk, jumlah):
        self.item.append(ItemPesanan(produk, jumlah))

    def tampilkan_detail(self):
        print(f"\nPesanan untuk {self.pelanggan.nama}:")
        total = 0
        for item in self.item:
            subtotal = item.produk.harga * item.jumlah
            print(f"- {item.produk.nama} x{item.jumlah} = Rp{subtotal}")
            total += subtotal
        print("Total Harga:", total)


class ItemPesanan:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah


# ==============================
# Testing
# ==============================
if __name__ == "__main__":
    # 1. Membuat beberapa produk
    p1 = Produk("Laptop", 8000000, 5)
    p2 = Produk("Mouse", 150000, 10)
    p3 = Produk("Keyboard", 300000, 7)

    # 2. Membuat pelanggan
    pelanggan1 = Pelanggan("Andi", "andi@email.com")

    # 3. Menambah produk ke keranjang pelanggan
    pelanggan1.keranjang.tambah_produk(p1, 1)  # Laptop 1
    pelanggan1.keranjang.tambah_produk(p2, 2)  # Mouse 2

    # 4. Membuat pesanan dari keranjang
    pesanan1 = pelanggan1.buat_pesanan()

    # 5. Menampilkan detail pesanan dan total harga
    pesanan1.tampilkan_detail()
