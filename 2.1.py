# Python code to calculate baud rate for c values between 0 and 1

# Parameters
bit_rate = 100_000  # Bit rate in bps (100 kbps)
r = 1  # 1 data element per 1 signal element

# Average value of c
c_avg = 0.5  # The average case factor

# Calculate baud rate
baud_rate_avg = c_avg * bit_rate / r

# Display the average baud rate
print(f"Average Baud Rate when c = 1/2: {baud_rate_avg:.0f} baud")
