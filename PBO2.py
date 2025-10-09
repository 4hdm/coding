## Kelas Parent
class Karyawan:
    """Parent class yang merepresentasikan seorang karyawan."""
    # 2.a. __init__() untuk inisialisasi atribut
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float):
        # 1.a, 1.b, 1.c. Atribut Karyawan
        self.nama = nama
        self.id_karyawan = id_karyawan
        self.gaji_pokok = gaji_pokok

    # 2.b. Method hitung_gaji()
    def hitung_gaji(self) -> float:
        """Mengembalikan gaji pokok."""
        return self.gaji_pokok

    # 2.c. Method info()
    def info(self) -> str:
        """Mengembalikan string informasi karyawan."""
        # Menghitung gaji aktual menggunakan method hitung_gaji()
        gaji_total = self.hitung_gaji()
        
        # Menggunakan f-string untuk format output
        return f"Nama : {self.nama}, ID: {self.id_karyawan}, Gaji: {gaji_total:.1f}"

# ----------------------------------------------------------------------

## Kelas Child (Manager)
class Manager(Karyawan):
    """
    Class Manager yang mewarisi dari Karyawan.
    """
    # 3.a. Atribut tambahan: tunjangan
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, tunjangan: float):
        # 4.a. Menggunakan super() untuk memanggil constructor parent class
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.tunjangan = tunjangan

    # 4.b. Meng-override method hitung_gaji()
    def hitung_gaji(self) -> float:
        """Menambahkan tunjangan ke gaji pokok."""
        # Memanggil method parent untuk mendapatkan gaji_pokok
        gaji_dasar = super().hitung_gaji()
        return gaji_dasar + self.tunjangan

    # 4.c. Meng-override method info()
    def info(self) -> str:
        """Menampilkan informasi manager."""
        # Mengambil informasi dasar dari parent class
        info_dasar = super().info()
        
        # Format string untuk Manager (Contoh Output)
        return f"Manager : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji():.1f}"

# ----------------------------------------------------------------------

## Kelas Child (Programmer)
class Programmer(Karyawan):
    """
    Class Programmer yang mewarisi dari Karyawan.
    """
    # 5.a. Atribut tambahan: bonus
    def __init__(self, nama: str, id_karyawan: str, gaji_pokok: float, bonus: float):
        # 6.a. Menggunakan super() untuk memanggil constructor parent class
        super().__init__(nama, id_karyawan, gaji_pokok)
        self.bonus = bonus

    # 6.b. Meng-override method hitung_gaji()
    def hitung_gaji(self) -> float:
        """Menambahkan bonus ke gaji pokok."""
        # Memanggil method parent untuk mendapatkan gaji_pokok
        gaji_dasar = super().hitung_gaji()
        return gaji_dasar + self.bonus

    # 6.c. Meng-override method info()
    def info(self) -> str:
        """Menampilkan informasi programmer."""
        # Mengambil informasi dasar dari parent class
        info_dasar = super().info()
        
        # Format string untuk Programmer (Contoh Output)
        return f"Programmer : {self.nama}, ID: {self.id_karyawan}, Gaji: {self.hitung_gaji():.1f}"

# ----------------------------------------------------------------------

## Contoh Penggunaan dan Output
if __name__ == "__main__":
    # Membuat objek Manager
    manager1 = Manager("Ahdam", "M023", 20000000.0, 5000000.0)
    
    # Membuat objek Programmer
    programmer1 = Programmer("Ashari", "P023", 14000000.0, 1000000.0)
    
    # Menggunakan method info() (Demonstrasi Polymorphism)
    print(manager1.info())
    print(programmer1.info())
