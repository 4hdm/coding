import statistics

#Fungsi untuk mencari bilangan prima
def cari_prima(sampai):
    primes = []
    for num in range(2, sampai + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

#Data bilangan prima dari 1 sampai 200
data = cari_prima(200)

#Menampilkan data
print ("Data bilangan prima 1-200:")
print(data)
print()

#Menghitung statistik
mean = statistics.mean(data)
median = statistics.median(data)
modus = "Tidak ada modus (tidak ada angka kembar)"
range_data = max(data) - min(data)
varian = statistics.variance(data)
std_deviasi = statistics.stdev(data)

#Menampilkan hasil
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Modus: {modus}")
print(f"Range: {range_data}")
print(f"Varian: {varian}")
print(f"Standar Deviasi: {std_deviasi}")
