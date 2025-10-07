# ===========================
# Class Perusahaan
# ===========================
class Perusahaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_proyek = []   # [Composition] Perusahaan punya daftar proyek (proyek "hidup-mati" bersama perusahaan)
        self.daftar_tim = []      # [Composition] Perusahaan punya daftar tim (tim juga bagian dari perusahaan)

    def buat_proyek(self, nama_proyek, deskripsi):
        proyek = Proyek(nama_proyek, deskripsi)  # Membuat objek Proyek baru
        self.daftar_proyek.append(proyek)        # Simpan ke daftar proyek perusahaan
        return proyek

    def buat_tim(self, nama_tim):
        tim = Tim(nama_tim)       # Membuat objek Tim baru
        self.daftar_tim.append(tim) # Simpan ke daftar tim perusahaan
        return tim

    def tampilkan_proyek(self):
        print(f"\nDaftar Proyek di {self.nama}:")
        for p in self.daftar_proyek:  # Loop semua proyek
            print("-", p)             # Panggil __str__ dari Proyek

    def tampilkan_tim(self):
        print(f"\nDaftar Tim di {self.nama}:")
        for t in self.daftar_tim:    # Loop semua tim
            print("-", t)            # Panggil __str__ dari Tim


# ===========================
# Class Proyek
# ===========================
class Proyek:
    def __init__(self, nama, deskripsi):
        self.nama = nama
        self.deskripsi = deskripsi
        self.daftar_tugas = []   # [Composition] Proyek punya daftar tugas (kalau proyek dihapus, tugas ikut hilang)

    def tambah_tugas(self, deskripsi_tugas):
        tugas = Tugas(deskripsi_tugas)   # Membuat objek Tugas baru
        self.daftar_tugas.append(tugas)  # Simpan tugas ke proyek
        return tugas

    def __str__(self):
        return f"Proyek: {self.nama} - {self.deskripsi}"


# ===========================
# Class Tim
# ===========================
class Tim:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_developer = []   # [Association] Tim punya developer, tapi developer bisa saja pindah ke tim lain

    def tambah_developer(self, developer):
        self.daftar_developer.append(developer)  # [Association] Developer dimasukkan ke tim

    def __str__(self):
        return f"Tim: {self.nama} (Developer: {len(self.daftar_developer)})"


# ===========================
# Class Developer
# ===========================
class Developer:
    def __init__(self, nama, keahlian):
        self.nama = nama
        self.keahlian = keahlian
        self.tugas = []   # [Association] Developer bisa mengerjakan banyak tugas (relasi dengan Tugas)

    def kerjakan_tugas(self, tugas):
        self.tugas.append(tugas)   # Developer mengerjakan tugas
        tugas.tugaskan_ke(self)    # [Association dua arah] Developer ↔ Tugas saling tahu

    def __str__(self):
        return f"Developer: {self.nama} ({self.keahlian})"


# ===========================
# Class Tugas
# ===========================
class Tugas:
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi
        self.developer = None   # [Association] Tugas bisa ditugaskan ke developer

    def tugaskan_ke(self, developer):
        self.developer = developer   # Hubungkan tugas dengan developer tertentu

    def __str__(self):
        dev = self.developer.nama if self.developer else "Belum ditugaskan"
        return f"Tugas: {self.deskripsi} -> {dev}"
    

# main program

if __name__ == "__main__":
    # Buat perusahaan
    perusahaan = Perusahaan("Tech Corp")  # Buat objek Perusahaan

    # Buat proyek di perusahaan (Composition: proyek hanya ada di perusahaan ini)
    proyek1 = perusahaan.buat_proyek("Sistem E-Commerce", "Membangun platform belanja online")
    proyek2 = perusahaan.buat_proyek("Aplikasi Mobile", "Aplikasi Android untuk manajemen tugas")

    # Buat tim di perusahaan
    tim1 = perusahaan.buat_tim("Backend Team")
    tim2 = perusahaan.buat_tim("Frontend Team")

    # Buat developer (objek Developer)
    dev1 = Developer("Budi", "Python & Django")
    dev2 = Developer("Siti", "React & Frontend")
    dev3 = Developer("Andi", "Database & SQL")

    # Tambah developer ke tim (Association)
    tim1.tambah_developer(dev1)
    tim1.tambah_developer(dev3)
    tim2.tambah_developer(dev2)

    # Tambah tugas ke proyek (Composition)
    tugas1 = proyek1.tambah_tugas("Buat API Produk")
    tugas2 = proyek1.tambah_tugas("Desain UI")
    tugas3 = proyek2.tambah_tugas("Integrasi Database")

    # Tugaskan tugas ke developer (Association)
    dev1.kerjakan_tugas(tugas1)
    dev2.kerjakan_tugas(tugas2)
    dev3.kerjakan_tugas(tugas3)

    # Cetak semua data
    perusahaan.tampilkan_proyek()
    perusahaan.tampilkan_tim()

    print("\nDaftar Tugas Proyek 1:")
    for t in proyek1.daftar_tugas:
        print("-", t)

    print("\nDaftar Tugas Proyek 2:")
    for t in proyek2.daftar_tugas:
        print("-", t)
