from datetime import datetime

# Class Buku
class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.status_dipinjam = False

    def __str__(self):
        status = "Dipinjam" if self.status_dipinjam else "Tersedia"
        return f"{self.judul} - {self.penulis} ({status})"


# Class Anggota
class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if not buku.status_dipinjam:
            buku.status_dipinjam = True
            self.buku_dipinjam.append(buku)
            print(f"{self.nama} berhasil meminjam {buku.judul}")
        else:
            print(f"Maaf, buku {buku.judul} sedang dipinjam orang lain.")

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
        print(f"Buku '{self.buku.judul}' dikembalikan oleh {self.anggota.nama}")

    def __str__(self):
        kembali = self.tanggal_kembali.strftime("%Y-%m-%d %H:%M:%S") if self.tanggal_kembali else "Belum dikembalikan"
        return f"Peminjaman: {self.anggota.nama} -> {self.buku.judul} (Pinjam: {self.tanggal_pinjam}, Kembali: {kembali})"


# Class Perpustakaan
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []
        self.daftar_anggota = []
        self.transaksi = []

    # Aggregation: Perpustakaan memiliki buku
    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)

    # Association: Perpustakaan memiliki daftar anggota
    def tambah_anggota(self, anggota):
        self.daftar_anggota.append(anggota)

    # Composition: Peminjaman terdiri dari detail buku & anggota
    def pinjam_buku(self, anggota, buku):
        if buku in self.koleksi_buku and anggota in self.daftar_anggota:
            if not buku.status_dipinjam:
                anggota.pinjam_buku(buku)
                peminjaman = Peminjaman(anggota, buku)
                self.transaksi.append(peminjaman)
                return peminjaman
        else:
            print("Buku atau anggota tidak terdaftar di perpustakaan.")
            return None

    def tampilkan_buku(self):
        print("\nDaftar Buku:")
        for buku in self.koleksi_buku:
            print("-", buku)

    def tampilkan_anggota(self):
        print("\nDaftar Anggota:")
        for anggota in self.daftar_anggota:
            print("-", anggota)

    def tampilkan_transaksi(self):
        print("\nDaftar Transaksi:")
        for trx in self.transaksi:
            print("-", trx)


# =============================
# Contoh penggunaan program
# =============================
if __name__ == "__main__":
    # Buat perpustakaan
    perpus = Perpustakaan("Perpus Kampus")

    # Tambah buku
    buku1 = Buku("Pemrograman Python", "Guido van Rossum")
    buku2 = Buku("Struktur Data", "Donald Knuth")
    perpus.tambah_buku(buku1)
    perpus.tambah_buku(buku2)

    # Tambah anggota
    anggota1 = Anggota("Budi")
    anggota2 = Anggota("Ani")
    perpus.tambah_anggota(anggota1)
    perpus.tambah_anggota(anggota2)

    # Pinjam buku
    trx1 = perpus.pinjam_buku(anggota1, buku1)

    # Tampilkan data
    perpus.tampilkan_buku()
    perpus.tampilkan_anggota()
    perpus.tampilkan_transaksi()

    # Kembalikan buku
    if trx1:
        trx1.kembalikan_buku()
        perpus.tampilkan_transaksi()