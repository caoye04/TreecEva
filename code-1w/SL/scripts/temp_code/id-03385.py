from itertools import cycle

# Simulate sensor data with noise and valid readings
data_stream = [15, 0, 23, -5, 42, 0, 11, 99, -1, 7]
noise_filter = [1, -1, 0, 1]

# Initialize tracking variables
clean_readings = []
filtered_noise = []
temp_accum = 0
offset = 10

# Misleading pre-processing: offset adjustment (not actually used later)
for i, reading in enumerate(data_stream):
    adjusted = reading + offset
    if adjusted > 10:
        temp_accum += adjusted // 2
    else:
        temp_accum -= adjusted

# Real processing begins: denoise using cyclic filter
denoise_cycle = cycle(noise_filter)
for val in data_stream:
    noise = next(denoise_cycle)
    corrected = val - noise
    filtered_noise.append(noise)  # Track for debugging, not used in result
    if corrected > 0:
        clean_readings.append(corrected)

# Secondary filtering: remove any still-zero values (redundant check)
clean_readings = [x for x in clean_readings if x != 0]

# Compute weighted checksum using modular arithmetic
checksum = 1

# Use enumerate and zip to pair index with value for weighted sum
for idx, val in enumerate(clean_readings):
    weight = (idx % 4) + 1
    contribution = weight * val
    checksum = (checksum + idx * val) % 97  # Key statement

# Distractor: unused statistical summary
total = sum(clean_readings)
mean_val = total / len(clean_readings) if clean_readings else 0
variance = sum((x - mean_val) ** 2 for x in clean_readings) / len(clean_readings) if clean_readings else 0

# Final output
print(f"Result: {checksum}")