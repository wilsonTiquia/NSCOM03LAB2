# Define the analog signal range
min_value = -20  # Minimum value in volts
max_value = 20  # Maximum value in volts

# Define the number of quantization levels
L = 8  # Number of quantization levels

# Calculate the quantization step size
quantization_step_size = (max_value - min_value) / L

# Print the results
print(f"Analog Signal Range: {min_value} V to {max_value} V")
print(f"Number of Quantization Levels: {L}")
print(f"Quantization Step Size: {quantization_step_size} V")
