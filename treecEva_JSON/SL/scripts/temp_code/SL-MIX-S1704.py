import math

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def compute_variance(data):
    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

# Sensor readings (raw ADC values)
sensor_readings = [1023, 512, 256, 128, 64, 32, 16]

# Calibration coefficients
calibration_factor = 3.3 / 1023.0
offset_correction = 0.05

# Process readings: scale, apply offset, and filter out low signals
scaled_readings = [
    reading * calibration_factor + offset_correction 
    for reading in sensor_readings 
    if reading > 64
]

# Compute statistical metrics
signal_mean = sum(scaled_readings) / len(scaled_readings)
signal_variance = compute_variance(scaled_readings)

# Quality flag based on variance and mean
quality_flag = 0b1100 if signal_variance < 0.5 else 0b0011
stability_flag = 0b1010 if signal_mean > 1.5 else 0b0101

# Combine flags using bitwise operations
combined_flags = (quality_flag & stability_flag) ^ 0b1111

# Fibonacci-based weighting factor
weight_index = int(math.log(len(scaled_readings)) * 2) % 7
weight_factor = fibonacci(weight_index) if weight_index > 0 else 1

# Final quality metric calculation
weighted_mean = signal_mean * weight_factor
normalized_variance = signal_variance / max(scaled_readings)

# Ternary operation for adjustment
adjustment = 0.1 if combined_flags & 0b1000 else -0.1

# Final signal quality score
final_signal_quality = (
    weighted_mean + normalized_variance + adjustment
) if combined_flags else 0.0

print(f"Result: {final_signal_quality}")