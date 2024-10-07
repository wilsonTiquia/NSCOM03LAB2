import numpy as np
import matplotlib.pyplot as plt

# Define the dataset
data = [0, 1, 0, 0, 1, 0]

# Define parameters
bit_duration = 1  # Duration of one bit
amplitude = 1  # Voltage level (+V or -V)
time = np.arange(0, len(data) * bit_duration, 0.01)

# Initialize voltage signal for AMI
ami_signal = np.zeros(len(time))
last_voltage = -amplitude  # Start with negative voltage for the first "1"

# Generate AMI signal
for i, bit in enumerate(data):
    start = int(i * 100)  # Corresponding start index for each bit in the time array
    if bit == 1:
        last_voltage = -last_voltage  # Alternate voltage
        ami_signal[start:start + 100] = last_voltage
    else:
        ami_signal[start:start + 100] = 0  # Zero voltage for "0"

# Plot the AMI signal
plt.figure(figsize=(10, 4))
plt.plot(time, ami_signal, drawstyle='steps-pre', label='AMI Signal')
plt.title("Bipolar Alternate Mark Inversion (AMI) Signal")
plt.xlabel("Time")

plt.grid(False)
plt.ylim([-1.5, 1.5])
plt.axhline(0, color='black',linewidth=0.5)
plt.legend()
plt.show()
