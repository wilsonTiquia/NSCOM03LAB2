import matplotlib.pyplot as plt
import numpy as np

# Dataset
data = [0, 1, 0, 0, 1, 1, 1, 0]

# Time configuration
bit_duration = 1
t = np.linspace(0, bit_duration, 100)  # 100 points per bit
time = np.array([])

# Generate time axis
for i in range(len(data)):
    time = np.concatenate([time, t + i * bit_duration])

# NRZ-L encoding
nrz_l = np.array([])
for bit in data:
    nrz_l = np.concatenate([nrz_l, np.ones(100) * (1 if bit == 1 else -1)])

# NRZ-I encoding
nrz_i = np.array([])
current_voltage = 1
for bit in data:
    if bit == 1:
        current_voltage = -current_voltage  # invert on '1'
    nrz_i = np.concatenate([nrz_i, np.ones(100) * current_voltage])

# Plotting the signals
plt.figure(figsize=(10, 6))

# NRZ-L Plot
plt.subplot(2, 1, 1)
plt.plot(time, nrz_l, drawstyle='steps-post', label="NRZ-L")
plt.ylim([-1.5, 1.5])
plt.title("NRZ-L")
plt.grid(False)

plt.xlabel("Time")

# NRZ-I Plot
plt.subplot(2, 1, 2)
plt.plot(time, nrz_i, drawstyle='steps-post', label="NRZ-I", color='orange')
plt.ylim([-1.5, 1.5])
plt.title("NRZ-I")
plt.grid(False)

plt.xlabel("Time")

plt.tight_layout()
plt.show()
