import statistics
# Data kelas dan frekuensi
kelas = [(21, 25), (26, 30), (31, 35), (36, 40), (41, 45), (46, 50)]
frekuensi = [6, 9, 10, 4, 8, 3]
# Hitung nilai tengah
data_list = []
for (bawah, atas), f in zip(kelas, frekuensi):
    midpoint = (bawah + atas) / 2
    data_list.extend([midpoint] * f)
# Hitung Mean, Median, Modus
mean_value = statistics.mean(data_list)
median_value = statistics.median(data_list)
modus_value = statistics.multimode(data_list)
# Tampilkan hasil
print(f"Mean   : {mean_value}")
print(f"Median : {median_value}")
print(f"Modus  : {modus_value}")