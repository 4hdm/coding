import statistics
data = {
    26: 2,
    27: 4,
    28: 5,
    29: 3,
    30: 5,
    31: 1
}
data_list = []
for tekanan, frekuensi in data.items():
    data_list.extend([tekanan] * frekuensi)
# Hitung Mean, Median, Modus
mean_value = statistics.mean(data_list)
median_value = statistics.median(data_list)
modus_value = statistics.multimode(data_list)  # pakai multimode karena bisa ada lebih dari satu modus
# Tampilkan hasil
print(f"Mean   : {mean_value}")
print(f"Median : {median_value}")
print(f"Modus  : {modus_value}")
