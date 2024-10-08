import numpy as np
import matplotlib.pyplot as plt

# Function to generate a continuous signal (e.g., a sine wave)
def generate_signal(freq, amplitude, time, sampling_rate):
    t = np.arange(0, time, 1/sampling_rate)
    signal = amplitude * np.sin(2 * np.pi * freq * t)
    return t, signal

# Function to perform flat-top sampling
def flat_top_sampling(signal, sampling_interval):
    # Sample every 'sampling_interval' points and hold the value constant
    sampled_signal = []
    for i in range(0, len(signal), sampling_interval):
        sampled_value = signal[i]  # Sample the value
        sampled_signal.extend([sampled_value] * sampling_interval)  # Hold it constant
    return np.array(sampled_signal)

# Main parameters
freq = 5  # Frequency of the sine wave (Hz)
amplitude = 1  # Amplitude of the sine wave
time = 1  # Duration of the signal (seconds)
sampling_rate = 1000  # Sampling rate for continuous signal
sampling_interval = 20  # Flat-top sampling interval

# Generate a continuous sine wave signal
t, continuous_signal = generate_signal(freq, amplitude, time, sampling_rate)

# Perform flat-top sampling
sampled_signal = flat_top_sampling(continuous_signal, sampling_interval)

# Plot the continuous and sampled signals
plt.figure(figsize=(10, 6))
plt.plot(t, continuous_signal, label="Original Signal")
plt.plot(t, sampled_signal, label="Flat-top Sampled Signal", linestyle='--')
plt.title("Flat-top Sampling in PCM")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
