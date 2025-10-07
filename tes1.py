# ================================
# SISTEM PERPUSTAKAAN
# ================================

class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.dipinjam = False

    def __str__(self):
        status = "Dipinjam" if self.dipinjam else "Tersedia"
        return f"{self.judul} oleh {self.penulis} ({status})"


class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if not buku.dipinjam:
            buku.dipinjam = True
            self.buku_dipinjam.append(buku)
            return True
        return False

    # 🔹 Tambahan: kembalikan buku
    def kembalikan_buku(self, buku):
        if buku in self.buku_dipinjam:
            buku.dipinjam = False
            self.buku_dipinjam.remove(buku)
            return True
        return False

    # 🔹 Tambahan: daftar buku yang dipinjam
    def daftar_buku_dipinjam(self):
        if not self.buku_dipinjam:
            return f"{self.nama} belum meminjam buku."
        else:
            return f"Buku dipinjam {self.nama}: " + ", ".join([b.judul for b in self.buku_dipinjam])

    def __str__(self):
        return f"Anggota: {self.nama}"


class Peminjaman:
    def __init__(self, anggota, buku):
        self.anggota = anggota
        self.buku = buku

    def __str__(self):
        return f"{self.anggota.nama} meminjam '{self.buku.judul}'"


class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.koleksi_buku = []
        self.daftar_anggota = []
        self.transaksi_peminjaman = []

    def tambah_buku(self, buku):
        self.koleksi_buku.append(buku)

    def daftar_anggota(self, anggota):  # tetap pakai nama asli
        self.daftar_anggota.append(anggota)

    def pinjam_buku(self, anggota, buku):
        if anggota.pinjam_buku(buku):
            peminjaman = Peminjaman(anggota, buku)
            self.transaksi_peminjaman.append(peminjaman)
            return peminjaman
        else:
            return None

    def status_peminjaman(self):
        if not self.transaksi_peminjaman:
            print("Belum ada transaksi peminjaman.")
        else:
            for transaksi in self.transaksi_peminjaman:
                print(transaksi)

    def tampilkan_buku(self):
        print("📚 Daftar Buku:")
        for buku in self.koleksi_buku:
            print(f"- {buku}")

    # 🔹 Tambahan: cari buku
    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        return None

    # 🔹 Tambahan: cari anggota
    def cari_anggota(self, nama):
        for anggota in self.daftar_anggota:
            if anggota.nama.lower() == nama.lower():
                return anggota
        return None

    # 🔹 Tambahan: hapus buku
    def hapus_buku(self, buku):
        if buku in self.koleksi_buku:
            self.koleksi_buku.remove(buku)
            return True
        return False

    # 🔹 Tambahan: hapus anggota
    def hapus_anggota(self, anggota):
        if anggota in self.daftar_anggota:
            self.daftar_anggota.remove(anggota)
            return True
        return False

    # 🔹 Tambahan: laporan ringkas
    def laporan(self):
        print(f"\n📖 Laporan Perpustakaan: {self.nama}")
        print("- Jumlah Buku:", len(self.koleksi_buku))
        print("- Jumlah Anggota:", len(self.daftar_anggota))
        print("- Jumlah Transaksi:", len(self.transaksi_peminjaman))


# ================================
# TESTING
# ================================
if __name__ == "__main__":
    perpustakaan = Perpustakaan("Perpus Kampus")

    # Tambah buku
    b1 = Buku("Python Dasar", "Andi")
    b2 = Buku("Algoritma", "Budi")
    b3 = Buku("Basis Data", "Citra")
    perpustakaan.tambah_buku(b1)
    perpustakaan.tambah_buku(b2)
    perpustakaan.tambah_buku(b3)

    # Tambah anggota (panggil via class agar tidak bentrok)
    a1 = Anggota("Siti")
    a2 = Anggota("Rudi")
    Perpustakaan.daftar_anggota(perpustakaan, a1)
    Perpustakaan.daftar_anggota(perpustakaan, a2)

    # Pinjam buku
    print("\n=== Transaksi Peminjaman ===")
    transaksi1 = perpustakaan.pinjam_buku(a1, b1)
    if transaksi1: print(transaksi1)

    transaksi2 = perpustakaan.pinjam_buku(a2, b2)
    if transaksi2: print(transaksi2)

    # Tampilkan daftar buku
    perpustakaan.tampilkan_buku()

    # Cek status peminjaman
    print("\n=== Status Peminjaman ===")
    perpustakaan.status_peminjaman()

    # Cek daftar buku dipinjam anggota
    print("\n=== Buku Dipinjam Anggota ===")
    print(a1.daftar_buku_dipinjam())
    print(a2.daftar_buku_dipinjam())

    # Kembalikan buku
    print("\n=== Pengembalian Buku ===")
    a1.kembalikan_buku(b1)
    print(a1.daftar_buku_dipinjam())

    # Cari buku
    print("\n=== Cari Buku ===")
    hasil = perpustakaan.cari_buku("Basis Data")
    print("Ketemu:", hasil if hasil else "Tidak ditemukan")

    # Hapus buku
    perpustakaan.hapus_buku(b3)

    # Laporan akhir
    perpustakaan.laporan()
