# Function to calculate minimum sampling rate
def find_minimum_sampling_rate(bandwidth_kHz, max_frequency=None):
    try:
        if max_frequency is None:
            # Raise an exception if max_frequency is not provided
            raise ValueError("Maximum frequency not found")
        
        # Calculate the minimum sampling rate using Nyquist theorem
        minimum_sampling_rate_kHz = 2 * max_frequency  # Nyquist rate
        minimum_sampling_rate_samples_per_sec = minimum_sampling_rate_kHz * 1000  # Convert to samples per second
        
        # Print the results
        print(f"Bandwidth of the signal: {bandwidth_kHz} kHz")
        print(f"Minimum Sampling Rate: {minimum_sampling_rate_kHz} kHz")
        print(f"Minimum Sampling Rate in samples per second: {minimum_sampling_rate_samples_per_sec} samples/second")
    
    except ValueError as e:
        # Handle the case where the max frequency is not found
        print(e)

# Example usage
bandwidth_kHz = 200  # Bandwidth in kHz
max_frequency = None  # Simulate missing max frequency case

find_minimum_sampling_rate(bandwidth_kHz, max_frequency)
