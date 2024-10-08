import numpy as np
import matplotlib.pyplot as plt

# Parameters
data = np.random.randint(0, 2, 16)  # Random binary data (0s and 1s)
bit_duration = 0.5  # Each signal element will represent 2 data elements
time_step = 0.01  # Time step for signal visualization
t = np.arange(0, len(data) * bit_duration, time_step)

# 2 Data Elements per 1 Signal Element
def two_data_per_one_signal(data):
    data_pairs = np.array_split(data, len(data) // 2)
    signal_mapping = {
        (0, 0): [-1],  # 00 -> -1
        (0, 1): [-0.5],  # 01 -> -0.5
        (1, 0): [0.5],   # 10 -> 0.5
        (1, 1): [1]      # 11 -> 1
    }
    signal = []
    for pair in data_pairs:
        signal += signal_mapping[tuple(pair)]
    return np.array(signal)

# Create signal
signal = two_data_per_one_signal(data)
t_signal = np.arange(0, len(signal) * bit_duration * 2, time_step)

# Plotting the signal
plt.figure(figsize=(8, 3))
plt.step(t_signal, np.repeat(signal, int(bit_duration / time_step * 2)), where='post')
plt.title('2 Data Elements per 1 Signal Element')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.grid(True)
plt.show()
