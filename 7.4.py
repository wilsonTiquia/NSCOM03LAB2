# Define bandwidth of the signal in kHz
bandwidth_kHz = 200  # Bandwidth in kHz

# Calculate the minimum sampling rate using Nyquist theorem
minimum_sampling_rate_kHz = 2 * bandwidth_kHz  # Minimum sampling rate in kHz

# Convert the result to samples per second
minimum_sampling_rate_samples_per_sec = minimum_sampling_rate_kHz * 1000  # Convert to samples per second

# Print the result
print(f"Bandwidth of the signal: {bandwidth_kHz} kHz")
print(f"Minimum Sampling Rate: {minimum_sampling_rate_kHz} kHz")
print(f"Minimum Sampling Rate in samples per second: {minimum_sampling_rate_samples_per_sec} samples/second")
