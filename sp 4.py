import numpy as np
import scipy.stats as stats

n = 200
x = 120
p_hat = x / n
z = stats.norm.ppf(0.975)

margin_error = z * np.sqrt(p_hat * (1 - p_hat) / n)

lower = p_hat - margin_error
upper = p_hat + margin_error

print(f"Estimasi proporsi: {p_hat:.2f}")
print(f"Interval kepercayaan 95%: ({lower:.2f}, {upper:.2f})")
