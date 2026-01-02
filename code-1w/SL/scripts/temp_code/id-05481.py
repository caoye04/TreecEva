def process_sensor_readings(readings):
    adjusted = []
    offset = sum(readings) // len(readings)
    for val in readings:
        adjusted.append((val + offset) ^ 3)  # Apply XOR correction
    return adjusted


def validate_checksum(data):
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= val << (i % 4)
    return checksum % 100


def decode_frequency_pattern(sequence):
    result = 0
    multiplier = 1
    for item in sequence:
        if item % 2 == 0:
            result += item * multiplier
        else:
            result -= item // multiplier if multiplier != 0 else 0
        multiplier += 1
    return abs(result)


def analyze_phase_shift(values):
    shift = 0
    for a, b in zip(values, values[1:]):
        shift += (b - a) * (a & 1)
    return shift

# Main execution
raw_data = [12, 8, 5, 19, 3]
scaled_data = [x * 2 for x in raw_data]

# Irrelevant transformation (distractor)
decoy_transform = [x.lower() for x in ['A', 'B', 'C']]
placeholder_sum = sum([1 for _ in range(len(decoy_transform))])

processed_sensors = process_sensor_readings(scaled_data)

# Simulate redundant data copy
backup_copy = processed_sensors.copy()

# Add noise and filter it out (semi-relevant)
noisy_data = [x + 1 for x in processed_sensors]
filtered_data = [x - 1 for x in noisy_data]  # Restore original

checksum_valid = validate_checksum(filtered_data)

# Generate frequency metric (not used in final answer but looks important)
frequency_metric = decode_frequency_pattern(filtered_data)

# Core logic chain
phase_shift = analyze_phase_shift(filtered_data)
baseline = sum(filtered_data[i] for i in range(0, len(filtered_data), 2))
correction_factor = len([x for x in filtered_data if x > 10])

intermediate = (baseline // correction_factor) + phase_shift

# Final computation
final_phase = (intermediate ^ 257) + (checksum_valid & 15)

print(f"Result: {final_phase}")