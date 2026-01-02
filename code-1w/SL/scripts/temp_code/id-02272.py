import itertools

# Simulated sensor readings with noise and calibration offsets
data_stream = [18, -5, 22, 47, 3, 66, -14, 29, 38, 51, 4, 12, 63, 55, 31, 44, 7, 25, 16, 33]

calibration_factor = 0.91
offset_adjustment = 7
dummy_threshold = 40  # Irrelevant to final logic but looks important

# Apply calibration (only some values are actually used later)
calibrated_readings = [(x * calibration_factor) + offset_adjustment for x in data_stream]

# Decoy transformation: complex but unused
transformed = []
for i in range(len(calibrated_readings)):
    if i % 3 == 0:
        transformed.append(int(calibrated_readings[i] ** 0.5))
    elif i % 3 == 1:
        transformed.append(int(calibrated_readings[i] // 2))
    else:
        transformed.append(int(calibrated_readings[i] % 29))

# Real processing path begins here — extract every third reading starting from index 2
effective_readings = data_stream[2::3]  # [22, 3, 12, 55, 25]

# Bit manipulation red herring: looks relevant but not used in final result
bit_masked = []
for val in effective_readings:
    masked = val & 0b11111  # Keep lower 5 bits
    rotated = ((masked << 3) | (masked >> 2)) & 0b11111
    bit_masked.append(rotated)

# Case conversion decoy using string operations on numbers (simulates data tagging)
labels = [f'SENSOR_{i}' for i in range(len(data_stream))]
upper_labels = [label.lower().swapcase() for label in labels]  # Fully processed but unused

# Core logic: filter calibrated subset based on original magnitude
reference_subset = [data_stream[i] for i in range(1, len(data_stream), 4)]  # [ -5, 47, 66, 51, 12, 7 ]
threshold = sum(reference_subset) // len(reference_subset)  # 28

# Actual filtering criteria
valid_indices = []
for i, val in enumerate(calibrated_readings):
    raw_val = data_stream[i]
    if raw_val > threshold and i % 2 == 1:
        valid_indices.append(i)

# Extract corresponding raw values (not calibrated ones)
filtered_data = [data_stream[i] for i in valid_indices]  # Only indices where raw > threshold and odd index

# Secondary filter: must be part of a repeating pattern in first half
first_half = data_stream[:10]
repeating = [k for k, g in itertools.groupby(first_half) if first_half.count(k) > 1]

# Final refinement
filtered_data = [x for x in filtered_data if x not in repeating]

# Critical execution point
filtered_sum = sum(filtered_data)

print(f"Result: {filtered_sum}")