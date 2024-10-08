import numpy as np
import matplotlib.pyplot as plt

# Parameters
data = np.random.randint(0, 2, 16)  # Random binary data (0s and 1s)
bit_duration = 0.75  # Duration of one data element in signal
time_step = 0.01  # Time step for signal visualization

# 4 Data Elements per 3 Signal Elements
def four_data_per_three_signal(data):
    # Split data into quads of 4 elements
    data_quads = np.array_split(data, len(data) // 4)
    
    # Define signal mapping for all 4-bit combinations
    signal_mapping = {
        (0, 0, 0, 0): [-1, -1, -1],
        (0, 0, 0, 1): [-1, -1, 1],
        (0, 0, 1, 0): [-1, 1, -1],
        (0, 0, 1, 1): [-1, 1, 1],
        (0, 1, 0, 0): [1, -1, -1],
        (0, 1, 0, 1): [1, -1, 1],
        (0, 1, 1, 0): [1, 1, -1],
        (0, 1, 1, 1): [1, 1, 1],
        (1, 0, 0, 0): [-1, -1, -1],
        (1, 0, 0, 1): [-1, -1, 1],
        (1, 0, 1, 0): [-1, 1, -1],
        (1, 0, 1, 1): [-1, 1, 1],
        (1, 1, 0, 0): [1, -1, -1],
        (1, 1, 0, 1): [1, -1, 1],
        (1, 1, 1, 0): [1, 1, -1],
        (1, 1, 1, 1): [1, 1, 1]
    }
    
    signal = []
    for quad in data_quads:
        signal += signal_mapping[tuple(quad)]
    return np.array(signal)

# Create signal
signal = four_data_per_three_signal(data)

# Calculate the number of time steps based on the signal length
# Ensure that t_signal covers the full length of the repeated signal
t_signal = np.arange(0, len(signal) * bit_duration, time_step)

# Repeat each signal element to match the number of time steps
# This ensures that each signal value is repeated to correspond with its bit duration
repeated_signal = np.repeat(signal, int(bit_duration / time_step))

# Plotting the signal
plt.figure(figsize=(8, 3))
plt.step(t_signal[:len(repeated_signal)], repeated_signal, where='post')  # Matching time and signal length
plt.title('4 Data Elements per 3 Signal Elements')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.grid(True)
plt.show()
