import numpy as np
import matplotlib.pyplot as plt

# Function to generate Manchester encoding
def manchester_encoding(data):
    manchester_signal = []
    for bit in data:
        if bit == '0':
            manchester_signal += [1, -1]  # 0 is represented by high-to-low transition
        else:
            manchester_signal += [-1, 1]  # 1 is represented by low-to-high transition
    return manchester_signal

# Function to generate Differential Manchester encoding
def diff_manchester_encoding(data):
    prev_level = 1  # Initial previous level is high
    diff_manchester_signal = []
    for bit in data:
        if bit == '0':
            # For '0', there is a transition at the beginning of the symbol
            prev_level = -prev_level
            diff_manchester_signal += [prev_level, -prev_level]
        else:
            # For '1', there is no transition at the beginning, only in the middle
            diff_manchester_signal += [prev_level, -prev_level]
        prev_level = diff_manchester_signal[-1]  # Update the previous level
    return diff_manchester_signal

# Binary data
data = '010011'

# Generate Manchester and Differential Manchester encoded signals
manchester_signal = manchester_encoding(data)
diff_manchester_signal = diff_manchester_encoding(data)

# Time axis for plotting
t = np.arange(0, len(manchester_signal))

# Plotting
plt.figure(figsize=(10, 6))

# Manchester encoding plot
plt.subplot(2, 1, 1)
plt.step(t, manchester_signal, where='mid', color='b', label='Manchester')
plt.title('Manchester Encoding')
plt.ylim([-2, 2])
plt.grid(False)

# Differential Manchester encoding plot
plt.subplot(2, 1, 2)
plt.step(t, diff_manchester_signal, where='mid', color='r', label='Differential Manchester')
plt.title('Differential Manchester Encoding')
plt.xlabel('Time')
plt.ylim([-2, 2])
plt.grid(False)

# Show plots
plt.tight_layout()
plt.show()
