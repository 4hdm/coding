# Class Perusahaan
class Perusahaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_proyek = []
        self.daftar_tim = []

    def buat_proyek(self, nama_proyek, deskripsi):
        proyek = Proyek(nama_proyek, deskripsi)
        self.daftar_proyek.append(proyek)
        return proyek

    def buat_tim(self, nama_tim):
        tim = Tim(nama_tim)
        self.daftar_tim.append(tim)
        return tim

    def tampilkan_proyek(self):
        print(f"\nDaftar Proyek di {self.nama}:")
        for p in self.daftar_proyek:
            print("-", p)

    def tampilkan_tim(self):
        print(f"\nDaftar Tim di {self.nama}:")
        for t in self.daftar_tim:
            print("-", t)


# Class Proyek
class Proyek:
    def __init__(self, nama, deskripsi):
        self.nama = nama
        self.deskripsi = deskripsi
        self.daftar_tugas = []

    def tambah_tugas(self, deskripsi_tugas):
        tugas = Tugas(deskripsi_tugas)
        self.daftar_tugas.append(tugas)
        return tugas

    def __str__(self):
        return f"Proyek: {self.nama} - {self.deskripsi}"


# Class Tim
class Tim:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_developer = []

    def tambah_developer(self, developer):
        self.daftar_developer.append(developer)

    def __str__(self):
        return f"Tim: {self.nama} (Developer: {len(self.daftar_developer)})"


# Class Developer
class Developer:
    def __init__(self, nama, keahlian):
        self.nama = nama
        self.keahlian = keahlian
        self.tugas = []

    def kerjakan_tugas(self, tugas):
        self.tugas.append(tugas)
        tugas.tugaskan_ke(self)

    def __str__(self):
        return f"Developer: {self.nama} ({self.keahlian})"


# Class Tugas
class Tugas:
    def __init__(self, deskripsi):
        self.deskripsi = deskripsi
        self.developer = None

    def tugaskan_ke(self, developer):
        self.developer = developer

    def __str__(self):
        dev = self.developer.nama if self.developer else "Belum ditugaskan"
        return f"Tugas: {self.deskripsi} -> {dev}"


# =============================
# Contoh Penggunaan Program
# =============================
if __name__ == "__main__":
    # Buat perusahaan
    perusahaan = Perusahaan("Tech Corp")

    # Buat proyek
    proyek1 = perusahaan.buat_proyek("Sistem E-Commerce", )
    proyek2 = perusahaan.buat_proyek("Aplikasi Mobile", "Aplikasi Android untuk manajemen tugas")

    # Buat tim
    tim1 = perusahaan.buat_tim("Backend Team")
    tim2 = perusahaan.buat_tim("Frontend Team")

    # Tambah developer
    dev1 = Developer("Budi", "Python & Django")
    dev2 = Developer("Siti", "React & Frontend")
    dev3 = Developer("Andi", "Database & SQL")

    tim1.tambah_developer(dev1)
    tim1.tambah_developer(dev3)
    tim2.tambah_developer(dev2)

    # Tambah tugas ke proyek
    tugas1 = proyek1.tambah_tugas("Buat API Produk")
    tugas2 = proyek1.tambah_tugas("Desain UI")
    tugas3 = proyek2.tambah_tugas("Integrasi Database")

    # Tugaskan tugas ke developer
    dev1.kerjakan_tugas(tugas1)
    dev2.kerjakan_tugas(tugas2)
    dev3.kerjakan_tugas(tugas3)

    # Tampilkan semua data
    perusahaan.tampilkan_proyek()
    perusahaan.tampilkan_tim()

    print("\nDaftar Tugas Proyek 1:")
    for t in proyek1.daftar_tugas:
        print("-", t)

    print("\nDaftar Tugas Proyek 2:")
    for t in proyek2.daftar_tugas:
        print("-", t)
