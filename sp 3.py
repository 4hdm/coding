import numpy as np
import scipy.stats as stats

data = [60, 65, 70, 68, 72]
mean = np.mean(data)
std_dev = np.std(data, ddof=1)
n = len(data)

# Gunakan distribusi t karena n < 30
t_critical = stats.t.ppf(0.975, df=n-1)
margin_error = t_critical * (std_dev / np.sqrt(n))

lower = mean - margin_error
upper = mean + margin_error

print(f"Estimasi rata-rata berat badan: {mean:.2f}")
print(f"Interval kepercayaan 95%: ({lower:.2f}, {upper:.2f})")
