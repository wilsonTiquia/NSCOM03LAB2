# Given data
bit_rate = 1_000_000  # Bit rate in bps (1 Mbps)
c = 1  # Case factor for NRZ-I (1 signal transition per bit)
R = 1  # Efficiency for NRZ-I (1 bit per signal level)

# Signal rate (S) using the formula S = c * N * R
signal_rate = c * bit_rate * R  # Signal rate in bps (equal to bit rate in this case)

# Minimum bandwidth for NRZ-I (Bandwidth = Signal Rate / 2)
min_bandwidth = signal_rate / 2  # Minimum bandwidth in Hz

# Print the results
print(f"Bit Rate: {bit_rate / 1_000_000} Mbps")
print(f"Signal Rate (S = c × N × R): {signal_rate / 1_000_000} Mbps")
print(f"Minimum Bandwidth: {min_bandwidth / 1_000_000} MHz")
