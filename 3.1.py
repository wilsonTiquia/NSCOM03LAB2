# Python code to calculate extra bits received due to clock mismatch

# Parameters
clock_difference = 0.001  # 0.1% clock difference (0.1% faster)
data_rates = [1_000, 1_000_000]  # Data rates: 1 kbps (1000 bps) and 1 Mbps (1,000,000 bps)

# Calculate extra bits per second for each data rate
for data_rate in data_rates:
    extra_bits_per_second = data_rate * clock_difference
    print(f"Data Rate: {data_rate / 1000:.0f} kbps")
    print(f"Extra bits per second due to 0.1% clock difference: {extra_bits_per_second:.0f} bits/second\n")
