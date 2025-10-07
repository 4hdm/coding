import numpy as np
import scipy.stats as stats

# Data
mean = 75           # rata-rata sampel
std_dev = 10        # standar deviasi populasi
n = 50              # ukuran sampel
alpha = 0.05        # tingkat signifikansi

z = stats.norm.ppf(1 - alpha / 2)  # 1.96

margin_error = z * (std_dev / np.sqrt(n))

lower_bound = mean - margin_error
upper_bound = mean + margin_error

print(f"Interval kepercayaan 95% untuk rata-rata populasi: ({lower_bound:.2f}, {upper_bound:.2f})")