import math

def analyze_sensor_array(raw_data):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.05 for x in raw_data if x > 0]
    filtered = [x for x in normalized if x < 100]
    aggregate = sum(filtered) / len(filtered) if filtered else 0

    # Relevant transformation: reverse and take magnitude windows
    mirrored = raw_data[::-1]  # slicing operation
    window_size = 3
    processed = []
    for i in range(len(mirrored) - window_size + 1):
        segment = mirrored[i:i + window_size]
        avg = sum(segment) / window_size
        processed.append(int(avg))

    # Decoy function call (never used)
    def calibrate_noise_floor(data):
        return [abs(x - 50) ** 0.5 for x in data]

    # Unused variable (red herring)
    noise_profile = [calibrate_noise_floor(processed)[i] % 7 for i in range(len(processed)) if i % 2 == 0]

    # Key transformation: apply bit manipulation for digital filtering effect
    processed_with_flags = []
    for val in processed:
        shifted = (val << 2) & 255  # artificial saturation at 8-bit
        flipped = shifted ^ 0b10101010
        reverted = (flipped >> 1) | (flipped << 7)  # rotate right by 1
        processed_with_flags.append(reverted if reverted < 200 else 199)

    # Secondary distractor: unused statistical analysis
    mean_raw = sum(raw_data) / len(raw_data)
    variance = sum((x - mean_raw) ** 2 for x in raw_data) / len(raw_data)
    stdev = math.sqrt(variance)
    z_scores = [(x - mean_raw) / stdev for x in raw_data]

    # Another dead path: string-based case conversion (suggested paradigm)
    status_tags = ['OK', 'ERROR', 'WARNING']
    upper_tags = [tag.lower() for tag in status_tags]  # irrelevant
    code_map = {i: ch.lower() for i, ch in enumerate('ABCDE')}

    return processed_with_flags


def calculate_stability_index(readings):
    if not readings:
        return -1

    # Complex aggregation with integer division and rounding
    total_power = 0
    for i, reading in enumerate(readings):
        if i % 2 == 0:
            contribution = (reading ** 2) // (i + 1)  # integer division
        else:
            contribution = int(round(reading * 0.75))  # rounding
        total_power += contribution

    # Apply logarithmic dampening only if threshold met
    if total_power > 100:
        adjusted = math.log(total_power) * 10
    else:
        adjusted = total_power * 1.2

    # Introduce trigonometric weighting (distractor unless critical)
    weights = [math.cos(i * math.pi / len(readings)) for i in range(len(readings)) if readings[i] % 2 == 1]
    weight_sum = sum(weights) if weights else 1.0

    final_index = adjusted / abs(weight_sum) if weight_sum != 0 else adjusted
    return round(final_index, 6)

# Simulated sensor input
initial_readings = [45, 23, 67, 89, 12, 34, 56]

# Step 1: Process sensor array
processed_readings = analyze_sensor_array(initial_readings)

# Step 2: Calculate stability index (key statement)
thermal_gradient = calculate_stability_index(processed_readings)

# Output result
print(f"Result: {thermal_gradient}")