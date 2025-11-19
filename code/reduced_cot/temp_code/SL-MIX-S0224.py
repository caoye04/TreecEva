import math

amplitude_measurements = [0.05, 0.2, 1.5, 0.8, 3.2, 0.1]
max_amplitude = max(amplitude_measurements)
min_amplitude = min(amplitude_measurements)

# Calculate dynamic range in decibels using logarithmic scale
dynamic_range_db = 20 * math.log10(max_amplitude / min_amplitude)

print(f"Result: {dynamic_range_db}")