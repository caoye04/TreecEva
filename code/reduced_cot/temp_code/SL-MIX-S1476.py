import math
from functools import reduce

def normalize_readings(readings):
    mean_val = sum(readings) / len(readings)
    return [r - mean_val for r in readings]

def apply_gain_correction(signal, gain_factor):
    return [s * gain_factor for s in signal]

def calculate_envelope(signal):
    return [abs(s) for s in signal]

def compute_rms(values):
    squared = [v**2 for v in values]
    mean_squared = sum(squared) / len(squared)
    return math.sqrt(mean_squared)

# Simulated raw acoustic sensor data
raw_sensor_data = [12.5, -8.3, 15.7, -4.2, 9.1, -11.8, 6.4, -3.9, 14.2, -7.6]

gain_matrix = [
    [1.2, 0.8],
    [1.5, 0.9]
]

depth_compensation_factors = [0.95, 1.05, 0.98, 1.02, 1.01, 0.99, 1.03, 0.97, 1.04, 0.96]

# Processing pipeline
normalized_readings = normalize_readings(raw_sensor_data)

# Apply depth compensation
compensated_signal = [normalized_readings[i] * depth_compensation_factors[i] 
                     for i in range(len(normalized_readings))]

# Calculate adaptive gain factor using matrix determinant
matrix_determinant = gain_matrix[0][0] * gain_matrix[1][1] - gain_matrix[0][1] * gain_matrix[1][0]
adaptive_gain = 1 + (matrix_determinant / 10)

gain_corrected_signal = apply_gain_correction(compensated_signal, adaptive_gain)

# Envelope detection
signal_envelope = calculate_envelope(gain_corrected_signal)

# Apply smoothing using moving average with functional approach
window_size = 3
smoothed_envelope = []
for i in range(len(signal_envelope) - window_size + 1):
    window = signal_envelope[i:i+window_size]
    average = reduce(lambda a, b: a + b, window) / window_size
    smoothed_envelope.append(average)

# Final signal strength calculation
processed_signal_strength = compute_rms(smoothed_envelope) * 100

print(f"Result: {round(processed_signal_strength, 2)}")