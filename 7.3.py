import numpy as np
import matplotlib.pyplot as plt

# Function to generate a continuous sine wave signal
def generate_sine_wave(freq, amplitude, time, sampling_rate):
    t = np.arange(0, time, 1/sampling_rate)
    signal = amplitude * np.sin(2 * np.pi * freq * t)
    return t, signal

# Function to sample a signal at a given sampling rate
def sample_signal(signal, sampling_rate, original_rate):
    step = int(original_rate / sampling_rate)
    return signal[::step]

# Main parameters
f_max = 4000  # Maximum frequency of the voice signal (Hz)
sampling_rate_nyquist = 2 * f_max  # Nyquist Rate (8000 Hz)
sampling_rate_sub_nyquist = 4000  # Half of the Nyquist Rate (4000 Hz)
sampling_rate_low = 2000  # One-fourth of the Nyquist Rate (2000 Hz)
amplitude = 1  # Amplitude of the sine wave
time = 0.01  # Duration of the signal (seconds)

# Generate the original continuous sine wave signal
original_sampling_rate = 32000  # High enough sampling rate for the continuous signal
t_continuous, continuous_signal = generate_sine_wave(f_max, amplitude, time, original_sampling_rate)

# Sample the signal at different rates
sampled_signal_nyquist = sample_signal(continuous_signal, sampling_rate_nyquist, original_sampling_rate)
sampled_signal_sub_nyquist = sample_signal(continuous_signal, sampling_rate_sub_nyquist, original_sampling_rate)
sampled_signal_low = sample_signal(continuous_signal, sampling_rate_low, original_sampling_rate)

# Time vectors for sampled signals
t_nyquist = t_continuous[::int(original_sampling_rate / sampling_rate_nyquist)]
t_sub_nyquist = t_continuous[::int(original_sampling_rate / sampling_rate_sub_nyquist)]
t_low = t_continuous[::int(original_sampling_rate / sampling_rate_low)]

# Plotting the original and sampled signals
plt.figure(figsize=(12, 8))

# Plot sampled at Nyquist rate
plt.subplot(3, 1, 1)
plt.plot(t_continuous, continuous_signal, label="Original Continuous Signal", color='lightgray')
plt.plot(t_nyquist, sampled_signal_nyquist, label="Sampled at 8000 Hz (Nyquist Rate)", marker='o', color='b')
plt.title("Sampling at the Nyquist Rate (8000 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# Plot sampled at sub-Nyquist rate
plt.subplot(3, 1, 2)
plt.plot(t_continuous, continuous_signal, label="Original Continuous Signal", color='lightgray')
plt.plot(t_sub_nyquist, sampled_signal_sub_nyquist, label="Sampled at 4000 Hz (Half Nyquist)", marker='o', color='g')
plt.title("Sampling at Half the Nyquist Rate (4000 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# Plot sampled at low rate
plt.subplot(3, 1, 3)
plt.plot(t_continuous, continuous_signal, label="Original Continuous Signal", color='lightgray')
plt.plot(t_low, sampled_signal_low, label="Sampled at 2000 Hz (One-Fourth Nyquist)", marker='o', color='r')
plt.title("Sampling at One-Fourth the Nyquist Rate (2000 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
