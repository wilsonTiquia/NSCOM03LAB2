# Re-importing necessary libraries after environment reset
import matplotlib.pyplot as plt
import numpy as np

# Data to be transmitted (Polar RZ scheme)
data_rz = [0, 1, 0, 0, 1]
# Parameters
bit_duration_rz = 1  # duration of each bit
sampling_rate_rz = 100  # samples per bit duration
mid_point = sampling_rate_rz // 2  # midpoint for the transition
# Time vector
time_rz = np.linspace(0, len(data_rz) * bit_duration_rz, len(data_rz) * sampling_rate_rz)
# Polar RZ signal generation
rz_signal = np.zeros(len(time_rz))
for i in range(len(data_rz)):
    if data_rz[i] == 1:
        rz_signal[i * sampling_rate_rz: i * sampling_rate_rz + mid_point] = 1  # High for first half
        rz_signal[i * sampling_rate_rz + mid_point: (i + 1) * sampling_rate_rz] = 0  # Zero for second half
    else:
        rz_signal[i * sampling_rate_rz: i * sampling_rate_rz + mid_point] = -1  # Low for first half
        rz_signal[i * sampling_rate_rz + mid_point: (i + 1) * sampling_rate_rz] = 0  # Zero for second half

# Plotting the Polar RZ signal
plt.figure(figsize=(10, 4))
plt.step(time_rz, rz_signal, where='post')
plt.title('Polar RZ ')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.show()
