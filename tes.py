from datetime import datetime

# Class Buku
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.status_dipinjam = False   # default: belum dipinjam

    def __str__(self):
        status = "Dipinjam" if self.status_dipinjam else "Tersedia"
        return f"{self.judul} - {self.penulis} ({status})"


# Class Anggota
class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.buku_dipinjam = []   # daftar buku yang dipinjam

    def pinjam_buku(self, buku):
        if not buku.status_dipinjam:
            buku.status_dipinjam = True
            self.buku_dipinjam.append(buku)
            print(f"{self.nama} berhasil meminjam buku '{buku.judul}'")
        else:
            print(f"Buku '{buku.judul}' sedang dipinjam orang lain.")

    def __str__(self):
        return f"Anggota: {self.nama}"


# Class Peminjaman
class Peminjaman:
    def __init__(self, anggota, buku):
        self.anggota = anggota
        self.buku = buku
        self.tanggal_pinjam = datetime.now()
        self.tanggal_kembali = None

    def kembalikan_buku(self):
        self.buku.status_dipinjam = False
        self.tanggal_kembali = datetime.now()
        print(f"Buku '{self.buku.judul}' telah dikembalikan oleh {self.anggota.nama}")

    def __str__(self):
        kembali = (
            self.tanggal_kembali.strftime("%Y-%m-%d %H:%M:%S")
            if self.tanggal_kembali else "Belum dikembalikan"
        )
        return f"Peminjaman: {self.anggota.nama} -> {self.buku.judul} (Pinjam: {self.tanggal_pinjam}, Kembali: {kembali})"


# Class Perpustakaan
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []     # daftar semua buku
        self.daftar_anggota = []   # daftar semua anggota
        self.transaksi = []        # daftar semua peminjaman

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)

    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)

    def pinjam_buku(self, anggota, buku):
        if buku in self.koleksi_buku and anggota in self.daftar_anggota:
            if not buku.status_dipinjam:
                anggota.pinjam_buku(buku)
                peminjaman = Peminjaman(anggota, buku)
                self.transaksi.append(peminjaman)
                return peminjaman
            else:
                print(f"Buku '{buku.judul}' sudah dipinjam.")
        else:
            print("Anggota atau buku tidak terdaftar di perpustakaan.")

    def tampilkan_buku(self):
        print(f"\nDaftar Buku di {self.nama}:")
        for buku in self.koleksi_buku:
            print(buku)

    def tampilkan_transaksi(self):
        print(f"\nDaftar Transaksi di {self.nama}:")
        for trx in self.transaksi:
            print(trx)


# Program Utama
if __name__ == "__main__":
    # Membuat perpustakaan
    perpus = Perpustakaan("Perpustakaan Kampus")

    # Menambah buku
    buku1 = Buku("Python untuk Pemula", "Guido van Rossum")
    buku2 = Buku("Algoritma dan Struktur Data", "Donald Knuth")
    perpus.tambah_buku(buku1)
    perpus.tambah_buku(buku2)

    # Menambah anggota
    anggota1 = Anggota("Budi")
    anggota2 = Anggota("Siti")
    perpus.tambah_anggota(anggota1)
    perpus.tambah_anggota(anggota2)

    # Menampilkan daftar buku
    perpus.tampilkan_buku()

    # Anggota meminjam buku
    trx1 = perpus.pinjam_buku(anggota1, buku1)
    trx2 = perpus.pinjam_buku(anggota2, buku2)

    # Menampilkan transaksi
    perpus.tampilkan_transaksi()

    # Pengembalian buku
    if trx1:
        trx1.kembalikan_buku()

    # Menampilkan transaksi lagi
    perpus.tampilkan_transaksi()
