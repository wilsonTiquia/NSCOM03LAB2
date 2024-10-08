import numpy as np
import matplotlib.pyplot as plt

# Function to generate a continuous sine wave signal
def generate_sine_wave(freq, amplitude, time, sampling_rate):
    t = np.arange(0, time, 1/sampling_rate)
    signal = amplitude * np.sin(2 * np.pi * freq * t)
    return t, signal

# Function to sample a signal at a given sampling rate
def sample_signal(signal, sampling_rate, original_rate):
    # Calculate the downsampling step
    step = int(original_rate / sampling_rate)
    return signal[::step]

# Main parameters
f = 5  # Frequency of the sine wave (Hz)
amplitude = 1  # Amplitude of the sine wave
time = 1  # Duration of the signal (seconds)
original_sampling_rate = 1000  # High enough sampling rate for the continuous signal

# Generate the original continuous sine wave signal
t_continuous, continuous_signal = generate_sine_wave(f, amplitude, time, original_sampling_rate)

# Different sampling rates based on the Nyquist theorem
sampling_rate_4f = 4 * f   # 2 times the Nyquist rate
sampling_rate_2f = 2 * f   # Nyquist rate
sampling_rate_f = f        # One-half the Nyquist rate (aliasing happens)

# Sample the signal at each of the three rates
sampled_signal_4f = sample_signal(continuous_signal, sampling_rate_4f, original_sampling_rate)
sampled_signal_2f = sample_signal(continuous_signal, sampling_rate_2f, original_sampling_rate)
sampled_signal_f = sample_signal(continuous_signal, sampling_rate_f, original_sampling_rate)

# Time vectors for sampled signals
t_4f = t_continuous[::int(original_sampling_rate / sampling_rate_4f)]
t_2f = t_continuous[::int(original_sampling_rate / sampling_rate_2f)]
t_f = t_continuous[::int(original_sampling_rate / sampling_rate_f)]

# Plotting the original and sampled signals
plt.figure(figsize=(12, 8))

# Plot continuous signal
plt.subplot(3, 1, 1)
plt.plot(t_continuous, continuous_signal, label="Original Continuous Signal", color='lightgray')
plt.plot(t_4f, sampled_signal_4f, label="Sampled at 4f (2x Nyquist)", marker='o', color='b')
plt.title("Sampling at 2 times the Nyquist Rate (4f)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# Plot sampled at Nyquist rate (2f)
plt.subplot(3, 1, 2)
plt.plot(t_continuous, continuous_signal, label="Original Continuous Signal", color='lightgray')
plt.plot(t_2f, sampled_signal_2f, label="Sampled at 2f (Nyquist)", marker='o', color='g')
plt.title("Sampling at the Nyquist Rate (2f)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# Plot sampled at one-half the Nyquist rate (f)
plt.subplot(3, 1, 3)
plt.plot(t_continuous, continuous_signal, label="Original Continuous Signal", color='lightgray')
plt.plot(t_f, sampled_signal_f, label="Sampled at f (1/2 Nyquist, Aliasing)", marker='o', color='r')
plt.title("Sampling at 1/2 the Nyquist Rate (f)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
