import pandas as pd

# === UNF (Unnormalized Form) ===
print("===== UNF (Unnormalized Form) =====")
unf_df = pd.DataFrame([
    {
        "ID_Pelanggan": "IDX234609",
        "Nama_Pelanggan": "Joko Prayitno",
        "Telp": "08132930358",
        "Email": "atit@sukasukka.id",
        "Alamat": "Jln. Bukit Indah no 76, Pasarturi, Surabaya",
        "No_Transaksi": "DAY29847",
        "Tgl_Transaksi": "11/11/2023",
        "Nama_Barang": "Ballpoint Big, Pensil B, Kertas A4, Ballpoint Pilot, Binder Klip, Cartridge BC-20 Canon",
        "Harga": "36000, 8400, 55000, 24000, 100000, 200000",
        "Jumlah": "3, 4, 5, 4, 10, 4",
        "Subtotal": "108000, 33600, 275000, 96000, 1000000, 800000",
        "Total": 2312600
    }
])
print(unf_df, "\n")

# === 1NF (First Normal Form) ===
print("===== 1NF (First Normal Form) =====")
nf1_df = pd.DataFrame([
    ["IDX234609", "Joko Prayitno", "08132930358", "atit@sukasukka.id",
     "Jln. Bukit Indah no 76, Pasarturi, Surabaya", "DAY29847", "11/11/2023", "Ballpoint Big", 36000, 3, 108000],
    ["IDX234609", "Joko Prayitno", "08132930358", "atit@sukasukka.id",
     "Jln. Bukit Indah no 76, Pasarturi, Surabaya", "DAY29847", "11/11/2023", "Pensil B", 8400, 4, 33600],
    ["IDX234609", "Joko Prayitno", "08132930358", "atit@sukasukka.id",
     "Jln. Bukit Indah no 76, Pasarturi, Surabaya", "DAY29847", "11/11/2023", "Kertas A4", 55000, 5, 275000],
    ["IDX234609", "Joko Prayitno", "08132930358", "atit@sukasukka.id",
     "Jln. Bukit Indah no 76, Pasarturi, Surabaya", "DAY29847", "11/11/2023", "Ballpoint Pilot", 24000, 4, 96000],
    ["IDX234609", "Joko Prayitno", "08132930358", "atit@sukasukka.id",
     "Jln. Bukit Indah no 76, Pasarturi, Surabaya", "DAY29847", "11/11/2023", "Binder Klip", 100000, 10, 1000000],
    ["IDX234609", "Joko Prayitno", "08132930358", "atit@sukasukka.id",
     "Jln. Bukit Indah no 76, Pasarturi, Surabaya", "DAY29847", "11/11/2023", "Cartridge BC-20 Canon", 200000, 4, 800000]
], columns=["ID_Pelanggan", "Nama_Pelanggan", "Telp", "Email", "Alamat", "No_Transaksi",
            "Tgl_Transaksi", "Nama_Barang", "Harga", "Jumlah", "Subtotal"])
print(nf1_df, "\n")

# === 2NF (Second Normal Form) ===
print("===== 2NF (Second Normal Form) =====")
pelanggan_df = pd.DataFrame([{
    "ID_Pelanggan": "IDX234609",
    "Nama_Pelanggan": "Joko Prayitno",
    "Telp": "08132930358",
    "Email": "atit@sukasukka.id",
    "Alamat": "Jln. Bukit Indah no 76, Pasarturi, Surabaya"
}])
print("\nTabel Pelanggan:")
print(pelanggan_df)

barang_df = pd.DataFrame([
    {"ID_Barang": "B001", "Nama_Barang": "Ballpoint Big", "Harga": 36000},
    {"ID_Barang": "B002", "Nama_Barang": "Pensil B", "Harga": 8400},
    {"ID_Barang": "B003", "Nama_Barang": "Kertas A4", "Harga": 55000},
    {"ID_Barang": "B004", "Nama_Barang": "Ballpoint Pilot", "Harga": 24000},
    {"ID_Barang": "B005", "Nama_Barang": "Binder Klip", "Harga": 100000},
    {"ID_Barang": "B006", "Nama_Barang": "Cartridge BC-20 Canon", "Harga": 200000}
])
print("\nTabel Barang:")
print(barang_df)

transaksi_df = pd.DataFrame([{
    "No_Transaksi": "DAY29847",
    "Tgl_Transaksi": "11/11/2023",
    "ID_Pelanggan": "IDX234609",
    "Total": 2312600
}])
print("\nTabel Transaksi:")
print(transaksi_df)

detail_df = pd.DataFrame([
    {"No_Transaksi": "DAY29847", "ID_Barang": "B001", "Jumlah": 3, "Subtotal": 108000},
    {"No_Transaksi": "DAY29847", "ID_Barang": "B002", "Jumlah": 4, "Subtotal": 33600},
    {"No_Transaksi": "DAY29847", "ID_Barang": "B003", "Jumlah": 5, "Subtotal": 275000},
    {"No_Transaksi": "DAY29847", "ID_Barang": "B004", "Jumlah": 4, "Subtotal": 96000},
    {"No_Transaksi": "DAY29847", "ID_Barang": "B005", "Jumlah": 10, "Subtotal": 1000000},
    {"No_Transaksi": "DAY29847", "ID_Barang": "B006", "Jumlah": 4, "Subtotal": 800000}
])
print("\nTabel Detail Transaksi:")
print(detail_df, "\n")

# === 3NF (Third Normal Form) ===
print("===== 3NF (Third Normal Form) =====")
staff_df = pd.DataFrame([{
    "ID_Staff": "S001",
    "Nama_Staff": "Sutarji",
    "Jabatan": "Staff Penjualan"
}])
print("\nTabel Staff:")
print(staff_df)

invoice_df = pd.DataFrame([{
    "No_Transaksi": "DAY29847",
    "Tgl_Transaksi": "11/11/2023",
    "ID_Pelanggan": "IDX234609",
    "ID_Staff": "S001",
    "Total": 2312600
}])
print("\nTabel Invoice:")
print(invoice_df)

print("\n✅ Semua tahap normalisasi (UNF → 3NF) sudah ditampilkan!")
