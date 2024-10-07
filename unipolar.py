import matplotlib.pyplot as plt
import numpy as np

# Data to be transmitted
data = [1, 0, 1, 1, 0]

# Parameters
bit_duration = 1  # duration of each bit
sampling_rate = 100  # samples per bit duration

# Time vector
time = np.linspace(0, len(data) * bit_duration, len(data) * sampling_rate)

# NRZ signal generation (Unipolar)
nrz_signal = np.zeros(len(time))
for i in range(len(data)):
    if data[i] == 1:
        nrz_signal[i * sampling_rate:(i + 1) * sampling_rate] = 1
    else:
        nrz_signal[i * sampling_rate:(i + 1) * sampling_rate] = 0

# Plotting the NRZ signal
plt.figure(figsize=(10, 4))
plt.step(time, nrz_signal, where='post')
plt.title('Unipolar NRZ Signal (Data: 10110)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim(-0.5, 1.5)
plt.show()
