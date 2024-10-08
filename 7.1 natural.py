import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a continuous signal (sine wave)
def generate_continuous_signal(frequency, amplitude, duration, sampling_rate):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return t, signal

# Step 2: Perform natural sampling using rectangular pulses
def natural_sampling(t, signal, sampling_rate, pulse_width):
    sampled_signal = np.zeros_like(signal)
    step_size = int(len(t) / (sampling_rate * t[-1]))
    
    for i in range(0, len(signal), step_size):
        # Retain the natural shape of the signal for the width of the pulse
        pulse_end = min(i + pulse_width, len(signal))
        sampled_signal[i:pulse_end] = signal[i:pulse_end]  # Sample for the pulse duration
    
    sampled_t = t[::step_size]  # Sampled time points (at the start of each pulse)
    return sampled_t, sampled_signal

# Parameters
frequency = 5  # frequency of the sine wave in Hz
amplitude = 1  # amplitude of the sine wave
duration = 1   # duration in seconds
continuous_sampling_rate = 1000  # continuous sampling rate (for the continuous signal)
natural_sampling_rate = 10  # sampling rate for natural sampling (in Hz)
pulse_width = 30  # width of the pulse for natural sampling (in number of samples)

# Step 1: Generate continuous signal
t_continuous, continuous_signal = generate_continuous_signal(frequency, amplitude, duration, continuous_sampling_rate)

# Step 2: Perform natural sampling
t_sampled, natural_sampled_signal = natural_sampling(t_continuous, continuous_signal, natural_sampling_rate, pulse_width)

# Step 3: Plot the continuous and naturally sampled signals
plt.figure(figsize=(10, 6))
plt.plot(t_continuous, continuous_signal, label="Continuous Signal", color='blue')
plt.plot(t_continuous, natural_sampled_signal, label="Naturally Sampled Signal", color='red', linestyle='--')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Natural Sampling for PCM')
plt.legend()
plt.grid(True)
plt.show()
