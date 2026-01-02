def analyze_sensor_data(readings):
    # Preprocess: extract even-indexed high-frequency samples
    samples = [readings[i] for i in range(0, len(readings), 2) if readings[i] > 50]
    
    # Irrelevant transformation: frequency normalization (not used later)
    norm_factor = sum(samples) / len(samples) if samples else 1.0
    normalized = [s / norm_factor for s in samples]

    # Extract paired readings using zip and enumerate
    paired_readings = []
    for i, (a, b) in enumerate(zip(readings, readings[1:])):
        if i % 3 == 0 and a < b:
            paired_readings.append((a, b, i))
    
    # Secondary filtering based on index condition
    filtered_pairs = [(x, y, idx) for x, y, idx in paired_readings if idx % 2 == 0]
    
    # Simulate data smoothing with slicing
    smoothed = readings[1:-1]  # remove edges
    edge_correction = abs(readings[0] - readings[-1])

    # Misleading energy calculation (dead end)
    total_energy = 0
    for val in smoothed:
        total_energy += val ** 2
    energy_per_unit = total_energy / len(smoothed) if smoothed else 0

    # Core logic: compute variance-like metric on filtered pairs
    diffs = [b - a for a, b, _ in filtered_pairs]
    if not diffs:
        return 0
    
    mean_diff = sum(diffs) / len(diffs)
    variance_proxy = sum((d - mean_diff) ** 2 for d in diffs) / len(diffs)
    stability_score = 100 / (1 + variance_proxy)  # higher = more stable

    return int(stability_score)


def calculate_diagnostic(pairs):
    # Unpack tuple pairs using enumerate and slicing
    indices = [i for i, _ in enumerate(pairs)]
    mid_point = len(indices) // 2
    left_half = pairs[:mid_point]
    right_half = pairs[mid_point:]
    
    # Dummy alignment score (irrelevant)
    alignment = 0
    for i, (l, r) in enumerate(zip(left_half, right_half)):
        alignment += abs(l[0] - r[0]) * i
    
    # Actual diagnostic based on pair differences
    increments = [b - a for a, b in pairs if b > a]
    decrements = [a - b for a, b in pairs if a > b]
    
    # Complex conditional expression
    trend_bias = len(increments) - len(decrements)
    magnitude_effect = sum(increments) - sum(decrements)
    
    # Distractor: unused statistical moment
    if increments:
        sq_dev = sum((x - sum(increments)/len(increments))**2 for x in increments)
        skew_guess = sq_dev / len(increments) if len(increments) > 1 else 0
    
    # Final heuristic
    if trend_bias > 0:
        base_rating = magnitude_effect * 1.5
    elif trend_bias < 0:
        base_rating = magnitude_effect * 0.8
    else:
        base_rating = abs(magnitude_effect) * 0.5
    
    # Apply modular correction based on count
    pair_count_mod = len(pairs) % 7
    adjusted_rating = (base_rating + pair_count_mod) * 1.1
    
    return int(adjusted_rating)

# Main execution
sensor_readings = [65, 70, 60, 80, 85, 75, 90, 45, 95, 100, 55]

# Step 1: Analyze raw sensor data to get filtered pairs
raw_analysis = analyze_sensor_data(sensor_readings)

# Generate reading pairs from original data
reading_pairs = []
for i in range(len(sensor_readings) - 1):
    if (sensor_readings[i] + sensor_readings[i+1]) % 2 == 0:
        reading_pairs.append((sensor_readings[i], sensor_readings[i+1]))

# Misleading secondary structure (never used)
reversed_pairs = [(b, a) for a, b in reading_pairs]

# Key computation
final_diagnostic = calculate_diagnostic(reading_pairs)

print(f"Result: {final_diagnostic}")