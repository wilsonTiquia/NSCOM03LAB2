import numpy as np
import matplotlib.pyplot as plt

# Parameters
data = np.random.randint(0, 2, 16)  # Random binary data (0s and 1s)
bit_duration = 2  # Each data element will last for 2 signal elements
time_step = 0.01  # Time step for signal visualization
t = np.arange(0, len(data) * bit_duration, time_step)

# 1 Data Element per 2 Signal Elements
def one_data_per_two_signal(data):
    signal_mapping = {0: [-1, -1], 1: [1, 1]}  # Example: 0 -> [-1, -1], 1 -> [1, 1]
    signal = []
    for d in data:
        signal += signal_mapping[d]
    return np.array(signal)

# Create signal
signal = one_data_per_two_signal(data)
t_signal = np.arange(0, len(signal) * bit_duration / 2, time_step)

# Plotting the signal
plt.figure(figsize=(8, 3))
plt.step(t_signal, np.repeat(signal, int(bit_duration / time_step / 2)), where='post')
plt.title('1 Data Element per 2 Signal Elements')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.grid(True)
plt.show()
