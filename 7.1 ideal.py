import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a continuous signal (sine wave)
def generate_continuous_signal(frequency, amplitude, duration, sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

# Step 2: Sample the continuous signal at the ideal rate
def ideal_sampling(t, signal, ideal_sampling_rate, continuous_sampling_rate):
    # Calculate the step size for the ideal sampling rate
    step = int(continuous_sampling_rate / ideal_sampling_rate)
    sampled_t = t[::step]
    sampled_signal = signal[::step]
    return sampled_t, sampled_signal

# Parameters
frequency = 5  # frequency of the sine wave in Hz
amplitude = 1  # amplitude of the sine wave
duration = 1   # duration in seconds
continuous_sampling_rate = 1000  # samples per second (high enough to represent a continuous signal)
ideal_sampling_rate = 2 * frequency  # Nyquist rate (2 times the highest frequency)

# Generate the continuous signal
t_continuous, continuous_signal = generate_continuous_signal(frequency, amplitude, duration, continuous_sampling_rate)

# Perform ideal sampling
t_sampled, sampled_signal = ideal_sampling(t_continuous, continuous_signal, ideal_sampling_rate, continuous_sampling_rate)

# Plot the continuous and sampled signals
plt.figure(figsize=(10, 6))
plt.plot(t_continuous, continuous_signal, label="Continuous Signal", color='blue')
plt.stem(t_sampled, sampled_signal, label="Sampled Signal (Ideal Sampling)", linefmt='red', markerfmt='ro', basefmt='black')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Ideal Sampling for PCM')
plt.legend()
plt.grid(True)
plt.show()
